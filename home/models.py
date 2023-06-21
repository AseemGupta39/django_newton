# from django.db import models
from django.db.models import Model,CharField,IntegerField,EmailField,TextField,ImageField,FileField

# Create your models here.

class Student(Model):
    name = CharField(max_length=100)
    age = IntegerField()
    email = EmailField(null=True,blank=True)
    address = TextField(null=True,blank=True)


class Product(Model):
    pass

