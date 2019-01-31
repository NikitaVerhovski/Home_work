import os
import sys

# Задача - 1

try:
    for i in range(1, 10):
        os.mkdir("dir_" + str(i))
except:
    print("Already exist")

a = input("enter something ")
print(a)

try:
    for i in range(3, 8):
        os.rmdir("dir_" + str(i))
except:
    print("Already removed")

# Задача - 2

list = os.listdir()
for i in list:
    print(i)

# Задача - 3

copy_dir = os.path.abspath("copy_dir")
if not os.path.exists(copy_dir):
    os.makedirs(copy_dir)

dirname, filename = os.path.split(__file__)
content = open(__file__).read()
open(os.path.join(copy_dir, filename), "w").write(content)