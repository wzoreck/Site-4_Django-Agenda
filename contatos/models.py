from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    # Para aparecer o atributo nome no admin ao invés do "nome" do objeto
    def __str__(self):
        return self.nome
    

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
    mostrar = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    