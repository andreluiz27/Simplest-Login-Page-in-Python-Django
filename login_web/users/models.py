# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    cpf = models.CharField(max_length=11,blank=False,unique=True,help_text="Não colocar traços")
    cellNumber=models.CharField(max_length=11,blank=False,unique=True,help_text="Exemplo: 16998801948")
    #email = models.EmailField(max_length=70, blank=True)

    def __str__(self):
        return self.email