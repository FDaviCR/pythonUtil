from random import randint

def geraListaDecrescente(tam):
    lista = []
    lista = list(range(tam))
    #lista.sort()
    print(lista)
    lista.reverse()
    print(lista)
    return lista

def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    print(lista)
    return lista

geraListaDecrescente(10)
#geraLista(10)
