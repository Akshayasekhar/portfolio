from django.db import models

# Create your models here.

class Person(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    landmark = models.CharField(max_length=30)