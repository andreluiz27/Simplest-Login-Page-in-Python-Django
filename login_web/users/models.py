# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    cpf = models.CharField(max_length=11, blank=True,unique=True)
    cellNumber=models.CharField(max_length=11,blank=True)

    def __str__(self):
        return self.email