from tastypie.resources import ModelResource
from api.models import Coupon
from tastypie import fields
from tastypie.serializers import Serializer
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from bs4 import BeautifulSoup
import requests

class CouponResource(ModelResource):
	
    class Meta:
        queryset = Coupon.objects.all()
        resource_name = 'coupon'
        allowed_methods = ['post']
        serializer = Serializer()
        authorization = Authorization()
        authentication = Authentication()
        always_return_data = True

    # generate coupon code
    def dehydrate(self, bundle):

        s = requests.Session()

        # gather request parameters
        name = bundle.data['name']
        coupon_type = bundle.data['coupon_type']
        value = bundle.data['value']
        minimum = bundle.data['minimum']

        # set up login params
        params = {
                'redirect': '',
                'highlight': '',
                'subdomain':'austin123',
                'login': 'au.smith7@gmail.com',
                'password': 'password',
                '[remember]': 0
                }
        
        #log in
        r = s.post('https://austin123.myshopify.com/admin/auth/login', data=params)

        if(r.status_code != 200):
            print("Error: invalid Shopify login\n")

        # get authenticate token
        content = BeautifulSoup(r.content, "html.parser")
        auth_token = content.find('input', type='hidden', attrs={'name': 'authenticity_token'})
        authentication_token = auth_token['value']

        # set up coupon form
        form_data = {
            'authenticity_token': authentication_token,
            'discount[code]': name,
            'discount[discount_type]': coupon_type, 
            'discount[value]': value,
            'discount[applies_to_resource]': '',
            'usage_limit_type': minimum, #careful here
            'discount[usage_limit]': '1',
            'discount[applies_once_per_customer]': 0,
            'discount_never_expires': '',
            '_': ''
        }

        #generate coupon
        r = s.post('https://austin123.myshopify.com/admin/discounts', form_data)

        if(r.status_code != 200):
            print("Error: invalid coupon generation request\n")

        return bundle.data