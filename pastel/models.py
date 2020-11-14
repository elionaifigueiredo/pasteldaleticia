from django.db import models

# Create your models here.



class Pastel(models.Model):
    nome = models.CharField(max_length=200)
    desponivel = models.BooleanField(default='True')
    quantidade = models.IntegerField()
    
    def __str__(self):
        return self.nome
    
    