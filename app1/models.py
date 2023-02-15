from django.db import models

# Create your models here.
class detail:
    name:str
    age:int
    rollno:int

# class stud:
#     name:"str"
#     address:"str"

class student(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
