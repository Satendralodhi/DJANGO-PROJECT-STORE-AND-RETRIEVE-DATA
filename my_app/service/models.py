from django.db import models

# Create your models here.
class services(models.Model):
    name=models.CharField(max_length=50)
    contactnumber=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.CharField(max_length=50)
    image=models.FileField(upload_to='services/',max_length=250,null=True,default=None)