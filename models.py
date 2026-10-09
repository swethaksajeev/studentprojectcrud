from django.db import models

# Create your models here.

#table definition/schema definition

class Student(models.Model):
    Name=models.CharField(max_length=30)
    Age=models.IntegerField()
    Course=models.CharField(max_length=30)
    Marks=models.IntegerField()

class Course(models.Model):
    mode_choices=(('offline','OFFLINE'),('online','ONLINE'))
    course_name=models.CharField(max_length=30)
    fee=models.IntegerField()
    duration=models.IntegerField()
    instructor=models.CharField(max_length=30)
    mode=models.CharField(choices=mode_choices)