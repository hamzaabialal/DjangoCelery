from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length= 200, default= '')
    student_age = models.CharField(max_length = 200)

