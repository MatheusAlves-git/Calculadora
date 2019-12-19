from mathFunctions import *
from interface import *

menu()
while True:
    op = int(input('OPÇÂO: '))
    if op == 8:
        print('VOLTE SEMPRE')
        break
    inserir(input("Digíte os números a serem calculados: "), op)
    menu()

