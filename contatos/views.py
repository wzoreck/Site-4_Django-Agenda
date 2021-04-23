from django.shortcuts import render, get_object_or_404 # Este é um atalho para não ter que repitir o código toda vez no try/except
from django.http import Http404
from .models import Contato

# Create your views here.
def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {'contatos' : contatos})

def ver_contato(request, contato_id): # O argumento passado pela URL vai ser passado para a view
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id) # Forma para obter o objeto ou gerar 404
    return render(request, 'contatos/ver_contato.html', {'contato' : contato})