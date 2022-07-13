from socket import if_nameindex
from turtle import clear
from unicodedata import name


def contador_palavras(lista_palavras):
    contador = list()
    for i in lista_palavras:
        contador.append(len(i))
    return contador


#if __name__ == '__main__':
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(contador_palavras(fruits))


    # comment: 
# end def