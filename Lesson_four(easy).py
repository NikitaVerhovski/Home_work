import random
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

my_list = [random.randint(0, 20) for _ in range(5)]

print("my_list = ", my_list)

list_sq = [num**2 for num in my_list]
print(list_sq)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

a = ["banana", "pear", "melon", "lemon"]
b = ["pineapple", "melon", "tangerine", "banana"]

fruit_list = [fruit for fruit in a if fruit in b]
print(fruit_list)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4



new_list = [random.randint(-10, 100)for _ in range(15)]

new_list = [item for item in list(new_list) if (item % 3 == 0 and item > 0 and item % 4 != 0)]

print(new_list)