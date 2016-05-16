from django.conf.urls import url, include
from django.contrib import admin
from tastypie.api import Api
from resources import CouponResource
from views import coupon