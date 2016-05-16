from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from models import Coupon
from forms import CouponForm
import requests
import json
from django.core.serializers.json import DjangoJSONEncoder


def coupon(request):
    
    #Generate coupon code from form
    if request.method == 'POST':
        
        # create form from request data
        form = CouponForm(request.POST)

        # validate form
        if form.is_valid():
            
            # gather POST params from form
            name = form.cleaned_data['name']
            coupon_type = form.cleaned_data['coupon_type']
            value = form.cleaned_data['value']
            minimum = (form.cleaned_data['minimum'])

            #set up request params
            params = {
                "name" : name,
                "coupon_type" : coupon_type,
                "value" : value,
                "minimum" : minimum
            }

            headers = { 'Content-Type': 'application/json' }

            r = requests.post(
                    'http://127.0.0.1:8000/api/v1/coupon/', #this request is 400'ing
                    headers=headers,
                    data=json.dumps(params, cls=DjangoJSONEncoder)
                    )
            
            if(r.status_code == 201):
                return HttpResponse(name)
            else:
                return HttpResponse("Error: coupon not created.")

    # return blank form by default
    else:
        form = CouponForm()

    #render view with constructed form
    return render(request, 'form.html', {'form': form})
