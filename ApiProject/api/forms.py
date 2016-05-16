from django import forms

class CouponForm(forms.Form):

    COUPON_TYPE_CHOICES = (
        ('percentage', 'Percentage'),
        ('fixed_amount', 'Fixed'),
        ('shipping', 'Shipping')
    )

    name = forms.CharField(max_length=60, required=True)
    coupon_type = forms.ChoiceField(choices = COUPON_TYPE_CHOICES)
    value = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    minimum = forms.DecimalField(max_digits=10, decimal_places=2, required=True)