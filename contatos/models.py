from django.db import models
from django.utils import timezone

# Create your models here.
class Contato(models.Model):
    # Atributos de classe
    # Nome atributo e tipo
    nome = models.CharField(max_length=255) # Definindo que receberá no máximo 255 caracteres
    sobrenome = models.CharField(max_length=255, blank=True) # Com blank definimos se é um campo obrigatório ou opcional, neste caso virou opcional
    email = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(default=timezone.now) # Default faz receber uma data padrão
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING) # Criando uma chave estrangeira para categoria, ao Contato ser deletado não faz nada com as categorias

class Categoria(models.Model):
    nome = models.CharField(max_length=255)