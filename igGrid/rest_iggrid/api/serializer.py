# coding: utf-8

from rest_framework import serializers
from .models import Ordering


class orderingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordering
        fields = ('id', 'Shop', 'Address', 'TotoalNumber', 'TotalPrice')