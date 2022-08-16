"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

# без генератора:
init_list = [234, 43, 2764, 234, 21, 1, 5, 4, 12, 3, 13, 45]
result = []
for i in range(0, len(init_list)):
    if init_list[i] > init_list[i - 1]:
        (result.append(init_list[i]))
print(f"Список элементов: {result}")

# с генератором:

my_new_list = [init_list[i] for i in range(0, len(init_list)) if init_list[i - 1] < init_list[i]]
print(f"Cписок элементов: {my_new_list}")
