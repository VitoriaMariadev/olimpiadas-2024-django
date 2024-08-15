from django.shortcuts import render

from django.http import HttpResponse # Tem que importar

lista_brazil = [
    {'nome': 'Beatriz Souza', 'esporte': 'Judô', 'medalha': '🥇 Ouro'},
    {'nome': 'Rebeca Andrade', 'esporte': 'Ginástica Artística', 'medalha': '🥇 Ouro'},
    {'nome': 'Ana Patrícia e Duda', 'esporte': 'Vôlei de praia', 'medalha': '🥇 Ouro'},
    {'nome': 'Caio Bonfim', 'esporte': 'Atletismo', 'medalha': '🥈 Prata'},
    {'nome': 'Willian Lima', 'esporte': 'Judô', 'medalha': '🥈 Prata'},
    {'nome': 'Rebeca Andrade', 'esporte': 'Ginástica artística', 'medalha': '🥈 Prata'},
    {'nome': 'Rebeca Andrade', 'esporte': 'Ginástica artística', 'medalha': '🥈 Prata'},
    {'nome': 'Tatiana Weston-Webb', 'esporte': 'Surfe', 'medalha': '🥈 Prata'},
    {'nome': 'Isaquias Queiroz', 'esporte': 'Canoagem velocidade', 'medalha': '🥉 Bronze'},
    {'nome': 'Larissa Pimenta', 'esporte': 'Judô', 'medalha': '🥉 Bronze'}
]

lista_eua = [
    {'nome': 'alguem', 'esporte': 'sei la', 'medalha': 'alguma coisa'}
]

def index(request): # Esse aqui é só pra não dá erro

    return render(request, "medalhistas/index.html", {

    })

def brazil(request): # Esse aqui é só pra não dá erro

    return render(request, "medalhistas/medalhas.html", {

        'pais': 'Brazil',
        'informacoes': lista_brazil

    })      

def eua(request): # Esse aqui é só pra não dá erro

    return render(request, "medalhistas/medalhas.html", {

        'pais': 'EUA',
        'informacoes': lista_eua
    })   