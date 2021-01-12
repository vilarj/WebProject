from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=60)
    age = models.IntegerField(max_length=2)
    message = models.TextField(max_length=254)

class Country(models.Model):
    pass