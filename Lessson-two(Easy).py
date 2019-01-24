# Задача № 1

# Первый  метод решения
x = ["яблоко", "банан", "киви", "арбуз"]
print("1.{0}\n2.{1}\n3.{2}\n4.{3}".format("яблоко", "банан", "киви", "арбуз").title())

# Второй метод решения
appel = "яблоко"
banana = "банан"
kiwi = "киви"
watermelon = "арбуз"
print("1.{0}\n2.{1}\n3.{2}\n4.{3}".format(appel, banana, kiwi, watermelon).upper())


# Задача № 2
a = [1, 4, 7, 8, 15, 23, 54, 44, 69]
b = [2, 4, 5, 10, 15, 32, 45, 58, 69]
Bset = frozenset(b)
c = [item for item in a if item not in Bset]  # C = A - B
print(c)


# Задача 3
list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
new_list = []
for i in list_one:
    if i % 2 == 0:
        new_list.append(i * 2)
    else:
        new_list.append(i / 4)
print(new_list)

# 2ую и 3юю задачу пришлось выискиывть метод решения в интернете


