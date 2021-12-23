"""tarefa_facil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from tarefa_facil.tarefa.views import home, tarefa_listar, tarefa_cadastrar, tarefa_deletar, tarefa_editar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('tarefa/', tarefa_listar, name="tarefa_listar"),
    path('cadastro/', tarefa_cadastrar, name="tarefa_cadastrar"),
    path('deletar/', tarefa_deletar, name="tarefa_deletar"),
    path('editar/', tarefa_editar, name="tarefa_editar"),
]
