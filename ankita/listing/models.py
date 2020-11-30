from django.db import models

# Create your models here.

class Destination(models.Model):

    name = str
    img = str
    price = int
    offer = bool