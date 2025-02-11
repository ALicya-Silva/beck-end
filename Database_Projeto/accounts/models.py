from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):  
    # Adicionado um campo de telefone para o usuário
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Número de Telefone")

    def __str__(self):
        return self.username 
