from django.shortcuts import render

from django.http import HttpResponse # Tem que importar

def index(request): # Esse aqui é só pra não dá erro

    return render(request, "medalhistas/index.html", {

    })