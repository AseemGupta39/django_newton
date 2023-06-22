# from django.db import models
from django.db.models import Model,CharField,IntegerField,EmailField,TextField,ImageField

# Create your models here.

class Recepie(Model):
    receipe_name = CharField(max_length=100)
    receipe_description = TextField()
    receipe_image = ImageField(upload_to='receipe')

    # def __str__(self) -> str:
    #     return self.receipe_name



