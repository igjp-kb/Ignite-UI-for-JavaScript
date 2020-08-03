# coding: utf-8

from rest_framework import routers
from .views import orderingViewSet


router = routers.DefaultRouter()
router.register(r'order', orderingViewSet)