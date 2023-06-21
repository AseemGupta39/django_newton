# from django.db import models
from django.db.models import Model,CharField,IntegerField,EmailField,TextField

# Create your models here.

class Student(Model):
    name = CharField(max_length=100)
    age = IntegerField()
    email = EmailField(null=True,blank=True)
    address = TextField(null=True,blank=True)


class Car(Model):
    car_name = CharField(max_length=500)
    speed = IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name 
    
## create 

# car = Car(car_name="Nexon",speed=110)
# car.save()

# Car.objects.create(car_name=,speed=)

## read

#cars=Car.objects.all()
#for car in cars:
#     print(f"{car.name} {car.speed}")

#  Car.objects.get(id=1)


## update

# car = Car.objects.get(id=1)
# >>> car.car_name = "creta"
# >>> car.speed = 180
# >>> car.save()

# Car.objects.filter(id=1).update(car_name="creta dark edition")

## delete

# 
