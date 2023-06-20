# from django.db import models
from django.db.models import Model,CharField,IntegerField,EmailField,TextField,ImageField,FileField

# Create your models here.

class Student(Model):
    name = CharField(max_length=100)
    age = IntegerField()
    email = EmailField()
    address = TextField()
    image = ImageField()
    file = FileField()

class Product(Model):
    pass

# s = []
# start = end = maxlength = 0
# l = []
# n=len(s)
# while(end<n):
#     if s[end] not in l:
#         l.append[s[end]]
#         end+=1
#         maxlength=max(maxlength,len(l))
#     else:
#         l.pop(l.index(s[start]))
#         start+=1

# print(maxlength)