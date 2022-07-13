import meusModulos

lista = ['camelo', 'melao', 'laranjado', 'saudita']
lista1 = ['caracolar', 'metralhadoradolarizar','paralelepipedização']

print(meusModulos.contador_palavras(lista1))

contPalavras = lambda lista: [len(i) for i in lista]

print(contPalavras(lista1))