# Задание - 1

def my_round(n = float(input("Введите число с десятичной точкой: "))):
    if float(n) - int(n) > 0.5:
        print(int(n) + 1)
    else:
        print(int(n))

my_round()

# Задание - 2

def lucky_ticket(ticket):
   ticket = str(ticket)
   t1 = ticket[:3]
   t2 = ticket[3:]
   sum1 = 0
   sum2 = 0
   for i in t1:
    sum1 = sum1 + int(i)
   for i in t2:
    sum2 = sum2 + int(i)
   if sum1 == sum2:
       print("BINGO")
   else:
       print("No destiny")

x = lucky_ticket(109226)
x = lucky_ticket(673924)





