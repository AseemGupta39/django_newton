# from django.db import models
from django.db.models import Model,CharField,IntegerField,\
    EmailField,TextField,ImageField,\
        ForeignKey,SET_NULL,CASCADE,OneToOneField
from django.contrib.auth.models import User
# Create your models here.

class Recepie(Model):
    user = ForeignKey(User,on_delete=SET_NULL,null=True,blank=True)
    receipe_name = CharField(max_length=100)
    receipe_description = TextField()
    receipe_image = ImageField(upload_to='receipe')
    receipe_view_count = IntegerField(default=1)

    # def __str__(self) -> str:
    #     return self.receipe_name

class Department(Model):
    department = CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering = ['department']


class StudentID(Model):
    student_id = CharField(max_length=100)
    
    def __str__(self):
        return self.student_id
    
class Subject(Model):
    subject_name = CharField(max_length=100)

    def __str__(self) -> str:
        return self.subject_name



class Student(Model):
    department = ForeignKey(Department,related_name='depart',on_delete=CASCADE)
    student_id = OneToOneField(StudentID,related_name='studentid',on_delete=CASCADE)
    student_name =CharField(max_length=100)
    student_email =EmailField(unique=True)
    student_age =IntegerField(default=18)
    student_address =TextField()

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = 'student'

class SubjectMarks(Model):
    student = ForeignKey(Student,related_name='studentmarks',on_delete=CASCADE)
    subject = ForeignKey(Subject,on_delete=CASCADE)
    marks = IntegerField()

    def __str__(self) -> str:
        return f'{self.student.student_name}  {self.subject.subject_name}'

    class Meta:
        unique_together  = ['student','subject']
