from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {}
    context_dict['boldmessage'] = "Olá Mundo!"
    context_dict['Autor'] = "Rafael Mendes"
    print(request)
    print("Dicionário", context_dict)
    texto = '''
    <h1> Rango </h1>
    Essa é a página principal do Rango
    
    <br/><a href='/rango/about/'>Sobre o rango</a>
    '''
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    texto = '''
    <h1> Sobre o Rango </h1>
    Essa é a página sobre o Rango.

    <br/><a href='/rango/'>Index</a>
    '''
    return HttpResponse(texto)

