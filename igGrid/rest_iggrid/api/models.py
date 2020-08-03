from django.db import models

# Create your models here.
class Ordering(models.Model):
    Shop = models.CharField(max_length=100) #出荷名
    Address = models.CharField(max_length=200) #配送先住所
    TotoalNumber = models.IntegerField(default=0) #項目の合計数
    TotalPrice = models.FloatField(default=0) #総額
