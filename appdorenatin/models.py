from django.db import models

class Nacional(models.Model):
  title = models.CharField(max_length = 50)
  ano = models.CharField(max_length = 4)
  tipo = models.CharField(max_length = 10)
  invicto = models.BooleanField()
  
class Artilheiro(models.Model):
  nome = models.CharField(max_length = 30)
  jogos = models.CharField(max_length = 4)
  gols = models.CharField(max_length = 3)
  titulos = models.BooleanField()
# Create your models here.
