from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def tarefa_listar(request):
    return render(request, 'base/tarefa_listar.html')

