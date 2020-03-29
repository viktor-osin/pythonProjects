
# -*- coding: utf-8 -*-
#для создания exe файла нужен wheel и pyinstaller
from colorama import Fore, Back, Style
from colorama import init

init()
print(Fore.BLACK)
print(Back.GREEN)

what = input("Что делаем? (+, -):")

print(Back.BLUE)
a = float(input("Введи первое число:"))
b = float(input("Введи второе число:"))



if what == "+":
    c = a + b
    print(Back.GREEN)
    print("Результат:" + str(c))
elif what == "-":
    c = a - b
    print(Back.GREEN)
    print("Результат" + str(c))
else:
    print(Back.RED)
    print("Неверная операция!")

input()