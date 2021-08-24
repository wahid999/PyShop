from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)#in models we have class called CharField it is a field that contain textual data
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)#Standard maximum lenght for urls is 2083


class Offer(models.Model):
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    discount = models.FloatField(max_length=50)
