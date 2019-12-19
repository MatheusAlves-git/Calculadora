def soma(*numbers):
    result = 0
    for number in numbers:
        result = float(number) + result
    return result


def sub(*numbers):
    result = numbers[0]
    for number in numbers:
        if float(number) == float(numbers[0]): continue
        result = float(result) - float(number)
    return result


def mult(*numbers):
    result = 1
    for number in numbers:
        result = float(result) * float(number)
    return result


def div(*numbers):
    result = numbers[0]
    for number in numbers:
        if number == numbers[0]: continue
        result = float(result) / float(number)
    return result


def raiz_quadrada(number):
    return float(number) ** 0.5


def pot(base, exp):
    result = 1
    for i in range(int(exp)):
        result = result * float(base)
    return result


def fatorial(number):
    result = 1
    for number_ in range(1, int(number) + 1):
        result = float(result) * float(number_)
    return result
