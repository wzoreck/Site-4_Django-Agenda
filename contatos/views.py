from django.shortcuts import render
from django.http import Http404
from .models import Contato

# Create your views here.
def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {'contatos' : contatos})

def ver_contato(request, contato_id): # O argumento passado pela URL vai ser passado para a view
    try:
        contato = Contato.objects.get(id=contato_id)
        return render(request, 'contatos/ver_contato.html', {'contato' : contato})
    except Contato.DoesNotExist as e:
        raise Http404() # Caso o id do contato passado não exista, erro 404