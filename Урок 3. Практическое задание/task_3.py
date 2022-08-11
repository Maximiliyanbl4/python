"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(a, b, c):
    if (a + b) > (a + c) and (a + b) > (b + c):
        return a + b
    if (a + c) > (a + b) and (a + c) > (b + c):
        return a + c
    if (b + c) > (a + b) and (b + c) > (a + c):
        return b + c


try:
    num_a = int(input("Введите первое значение: "))
    num_b = int(input("Введите второе значение: "))
    num_c = int(input("Введите третье значение: "))
    print(f"Сумму наибольших двух аргументов:  {my_func(num_a, num_b, num_c)}")
except ValueError as d:
    print(f"{d}")
