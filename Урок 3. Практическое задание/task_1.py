"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""

#Вариант №1:

def posit_argum(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print(f"Вы что? Пытаетесь делить на 0!")


num_a = int(input("Введите первое число: "))
num_b = int(input("Введите второе число: "))
print(f"Результат: {posit_argum(num_a, num_b)}")

"""
Вариант №2:

def posit_argum(a, b):
    if b != 0:
        return a / b
    else:
        return float('nan')


num_a = float(input("Введите первое число: "))
num_b = float(input("Введите второе число: "))
print(f"Результат: {posit_argum(num_a, num_b)}")
"""
