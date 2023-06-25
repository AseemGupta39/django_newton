# from django.db import models
from django.db.models import Model,CharField,IntegerField,\
    EmailField,TextField,ImageField,ForeignKey,SET_NULL
from django.contrib.auth.models import User
# Create your models here.

class Recepie(Model):
    user = ForeignKey(User,on_delete=SET_NULL,null=True,blank=True)
    receipe_name = CharField(max_length=100)
    receipe_description = TextField()
    receipe_image = ImageField(upload_to='receipe')

    # def __str__(self) -> str:
    #     return self.receipe_name



