from statistics import mode
from venv import create
from django.db import models

# Create your models here.

class signup(models.Model):
    create=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zipcode=models.IntegerField()

    def __str__(self):
        return self.firstname