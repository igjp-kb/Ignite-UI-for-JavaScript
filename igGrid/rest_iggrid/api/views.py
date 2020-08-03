# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

from .models import Ordering
from .serializer import orderingSerializer


class orderingViewSet(viewsets.ModelViewSet):
    queryset = Ordering.objects.all()
    serializer_class = orderingSerializer