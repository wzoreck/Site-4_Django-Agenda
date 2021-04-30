from django.shortcuts import render, get_object_or_404 # Este é um atalho para não ter que repitir o código toda vez no try/except
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator # Para criar paginação em listas/tabelas com vários dados
from django.contrib import messages

# Create your views here.
def index(request):
    # Exibir uma mensagem
    messages.add_message(request, messages.ERROR, 'Ocorre um erro')

    contatos = Contato.objects.order_by('nome') # Para ordenar por nome a lista
    paginator = Paginator(contatos, 2)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {'contatos' : contatos})

def ver_contato(request, contato_id): # O argumento passado pela URL vai ser passado para a view
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id) # Forma para obter o objeto ou gerar 404
    if not contato.mostrar:
        raise Http404()
        
    return render(request, 'contatos/ver_contato.html', {'contato' : contato})

def busca(request):
    termo = request.GET.get('termo')
    contatos = Contato.objects.order_by().filter(
        nome = termo
    )
    paginator = Paginator(contatos, 2)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html', {'contatos' : contatos})