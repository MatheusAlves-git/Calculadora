from mathFunctions import *


def menu():
    print('='*30)
    print("O que deseja fazer?: \n1 - Soma \n2 - Subtração \n3 - Multiplicação ['*'] \n4 - Divisão \n5 - Potênciação ['^'] \n6 - Fatorização \n7 - Raiz Quadrada \n8 - Encerrar")
    print('='*30)


def inserir(txt, opc):
    numbers = txt
    numbers = numbers.replace(',', '.')
    if opc == 1:
        numbers = numbers.split('+')
        result = soma(*numbers)

    if opc == 2:
        numbers = numbers.split('-')
        result = sub(*numbers)

    if opc == 3:
        numbers = numbers.split('-')
        result = mult(*numbers)

    if opc == 4:
        numbers = numbers.split('/')
        result = div(*numbers)

    if opc == 5:
        numbers = numbers.split('^')
        result = pot(*numbers)

    if opc == 6:
        result = fatorial(numbers)

    if opc == 7:
        result = raiz_quadrada(numbers)

    input(f"Resultado: {result}")
