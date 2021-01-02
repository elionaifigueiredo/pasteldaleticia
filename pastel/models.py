from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.



class Pastel(models.Model):
    nome = models.CharField(max_length=200)
    desponivel = models.BooleanField(default='True')
    quantidade = models.IntegerField()
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits = 5, decimal_places = 2) 
    foto = CloudinaryField(null=True, blank=True)
       
    
    def __str__(self):
        return self.nome
    
    
    