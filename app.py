from mathFunctions import *
from interface import *

def clear():
    print('\n'*60)

menu()
while True:
    op = int(input('OPÇÂO: '))
    if op == 1:
        numbers = input("Digíte os números a serem calculados: ")
        numbers = numbers.replace(',', '.')
        numbers = numbers.split('+')
        result = soma(*numbers)
        input(f"Resultado: {result}")

    elif op == 2:
        numbers = input("Digíte os números a serem calculados: ")
        numbers = numbers.replace(',', '.')
        numbers = numbers.split('-')
        result = sub(*numbers)
        input(f"Resultado: {result}")

    elif op == 3:
        numbers = input("Digíte os números a serem calculados: ")
        numbers = numbers.replace(',', '.')
        numbers = numbers.split('*')
        result = mult(*numbers)
        input(f"Resultado: {result}")

    elif op == 4:
        numbers = input("Digíte os números a serem calculados: ")
        numbers = numbers.replace(',', '.')
        numbers = numbers.split('/')
        result = div(*numbers)
        input(f"Resultado: {result}")

    elif op == 5:
        numbers = input("Digíte os números a serem calculados: ")
        numbers = numbers.replace(',', '.')
        numbers = numbers.split('^')
        result = pot(*numbers)
        input(f"Resultado: {result}")

    elif op == 6:
        numbers = input("Digíte os números a serem calculados: ")
        numbers = numbers.replace(',', '.')
        result = fatorial(*numbers)
        input(f"Resultado: {result}")

    elif op == 7:
        numbers = input("Digíte os números a serem calculados: ")
        numbers = numbers.replace(',', '.')
        result = raiz_quadrada(numbers)
        input(f"Resultado: {result}")

    elif op == 8:
        print('VOLTE SEMPRE')
        break
    menu()
