from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def tarefa_listar(request):
    context = {
        "tipos": [
            'Urgente', 'Importante', 'Fim do Dia', 'Delegar',
        ],
        "tarefas": [
            {"id": 1, "descricao": "pagar IPVA", "tipo": "Urgente"},
            {"id": 2, "descricao": "pagar Equatorial", "tipo": "Urgente"},
            {"id": 3, "descricao": "pagar Agespisa", "tipo": "Importante"},
            {"id": 4, "descricao": "lavar o carro", "tipo": "Fim do Dia"},
            {"id": 5, "descricao": "pagar escola", "tipo": "Importante"},
        ]
    }
    return render(request, 'base/tarefa_listar.html', context)

def tarefa_cadastrar(request):
    return render(request, 'base/tarefa_cadastrar.html')

def tarefa_deletar(request):
    return render(request, 'base/tarefa_deletar.html')

def tarefa_editar(request):
    return render(request, 'base/tarefa_editar.html')

