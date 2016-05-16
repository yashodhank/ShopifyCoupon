from __future__ import unicode_literals
from django.db import models
import uuid

class Coupon(models.Model):
    
    COUPON_TYPE_CHOICES = (
        ('percentage', 'percentage'),
        ('fixed_amount', 'fixed'),
        ('shipping', 'shipping')
    )

    name = models.CharField(max_length=60)
    coupon_type = models.CharField(max_length=40, choices = COUPON_TYPE_CHOICES, default='percentage')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    minimum = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name