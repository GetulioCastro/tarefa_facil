from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def tarefa_listar(request):
    context = {
        "tarefas": [
            {"id": 1, "descricao": "pagar IPVA", "data": "20/12/21"},
            {"id": 2, "descricao": "pagar Equatorial", "data": "20/12/21"},
            {"id": 3, "descricao": "pagar Agespisa", "data": "20/12/21"},
            {"id": 4, "descricao": "lavar o carro", "data": "20/12/21"},
        ]
    }
    return render(request, 'base/tarefa_listar.html', context)

def tarefa_cadastrar(request):
    return render(request, 'base/tarefa_cadastrar.html')

def tarefa_deletar(request):
    return render(request, 'base/tarefa_deletar.html')

def tarefa_editar(request):
    return render(request, 'base/tarefa_editar.html')

