import math
import random
# Задача №1

list_one = [1, 4, 7, 9, 12, 16, 37, 53, 56]
new_list = []
for el in  list_one:
     if el > 0 and (math.sqrt(el)) % 2 == 0:
         new_list.append(int(math.sqrt(el)))
print(new_list)

# Задача №2

date = input("Введите дату в формате dd.mm.yyyy: ")
new_date = (date.split("."))

day = {"01": "первое", "02": "второе", "03": "третье", "04": "четвертое", "05": "пятое", "06": "шестое", "07": "седьмое",
       "08": "восьмое", "09": "девятое", "10": "десятое", "11": "одинацатое", "12": "двенадцатое", "13": "тринадцатое",
       "14": "четырнадцатое", "15": "пятнадцатое", "16": "шестнадцатое", "17": "семнадцатое", "18": "восемнадцатое",
       "19": "девятнадцатое", "20": "двадцатое", "21": "двадцать первое", "22": "двадцать второе", "23": "двадцать третье",
       "24": "двадцать четвертое", "25": "двадцать пятое", "26": "двадцать шестое", "27": "двадцать седьмое",
       "28": "двадцать восьмое", "29": "двадцать девятое", "30": "тридцатое", "31": "тридцать первое"}

month = {"01": "января", "02": "февраля", "03": "марта", "04": "апреля", "05": "мая", "06": "июня", "07": "июля",
         "08": "августа", "09": "сентября", "10": "октября", "11": "ноября", "12": "декабря"}

print("Сегодня {} {} {} года.".format(day[new_date[0]], (month[new_date[1]]), new_date[2]))

# Задача №3

count = int(input("Введите количество элементов: "))
my_list = []
n = 0
while n < count:
    my_list.append(random.randint(-100, 100))
    n += 1
print(my_list)

# Задача №4

number = int(input("Введите количество элементов"))
mylist = []
n = 0
while n < number:
    mylist.append(random.randint(0, 100))
    n += 1
print(mylist)

sort_list = set(mylist)
print(sort_list)










