from django.db import models

# Create your models here.
class Position(models.Model):
    role= models.CharField(max_length=50)

class Employee(models.Model):
    firstname= models.CharField(max_length=50)
    lastname= models.CharField(max_length=50)
    mobile= models.CharField(max_length=10)
    position= models.ForeignKey(Position,on_delete=models.CASCADE)

