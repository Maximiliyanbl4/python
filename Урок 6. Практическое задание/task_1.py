"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

"""
# Вариант №2
from itertools import cycle
from time import sleep


class TrafficLight:
    __color = cycle([{"signal": "Красный", "duration": 7}, {"signal": "Желтый", "duration": 2},
                     {"signal": "Зеленый", "duration": 5}, ])

    def running(self):
        shade = next(self.__color)
        print(f"Цвет: {shade['signal']} - {shade['duration']}c")
        sleep(shade['duration'])


print("\nСветофор\n")
color_signal = TrafficLight()
color_signal.running()
color_signal.running()
color_signal.running()
"""

from time import sleep


class TrafficLight:
    __color = ["Красный", "Желтый", "Зеленый"]

    def running(self):
        i = 0
        print("\nСветофор:\n")
        while i != 3:
            print(f"Цвет - {TrafficLight.__color[i]}")
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(4)
            i += 1


color_signal = TrafficLight()
color_signal.running()
