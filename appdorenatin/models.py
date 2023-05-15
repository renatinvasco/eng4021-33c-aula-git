from django.db import models

#cria por meio de uma classe um modelo para um título nacional, como o título, o ano e o tipo dele como um campo de caracteres e se foi invicto ou não como uma caixa para se marcar
class Nacional(models.Model):
  title = models.CharField(max_length = 50)
  ano = models.CharField(max_length = 4)
  tipo = models.CharField(max_length = 10)
  invicto = models.BooleanField()
  
  #cria por meio de uma classe um modelo para as informações dos artilheiros, como o nome, jogos e gols dele como um campo de caracteres e se foi campeão ou não como uma caixa para se marcar
class Artilheiro(models.Model):
  nome = models.CharField(max_length = 30)
  jogos = models.CharField(max_length = 4)
  gols = models.CharField(max_length = 3)
  titulos = models.BooleanField()
# Create your models here.
