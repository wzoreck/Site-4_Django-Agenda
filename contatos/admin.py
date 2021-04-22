from django.contrib import admin
from .models import Categoria, Contato # models deste app 

# Para fazer com que os campos abaixo aparecam na tabela do admin
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email', 'telefone', 'data_criacao', 'categoria')
    # Aqui pode-se adicionar diversas modificações para customizar a tela de admin

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)