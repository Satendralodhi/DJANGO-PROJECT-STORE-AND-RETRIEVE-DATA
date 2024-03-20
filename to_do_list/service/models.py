from django.db import models

# Create your models here.
class service(models.Model):
    name=models.CharField(max_length=50)
    contactnumber=models.CharField(max_length=50)
    email=models.EmailField()
    taskname=models.CharField(max_length=50)
    mark=models.CharField(max_length=50)
    