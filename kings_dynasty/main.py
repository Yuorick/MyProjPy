#import pandas
import time
import re
import os

# 0. ФУНКЦИЯ СПАВНЕНИЯ СТРОК
def MyFn(s):
    names = re.split(" |\n", s)
    return s[0]
## 0 !

# 1. ЧТЕНИЕ ИНФОРМАЦИИ ИЗ TXT AFQKF
f = open("tree.txt", 'r')
lines = f.readlines()
## 1!

# 2. ПРОВЕРКА
for line in lines:
    print(line.strip())
## 2!

# 3. ЧИСТКА ПУСТЫХ СТРОК
num = len(lines)
for i in range(0, num):
    Str = lines[num - 1 - i]
    if lines[num - 1 -i] == '\n':
        lines.pop(num - 1 - i)
## 3!

# 4. СОРТИРОВКА СПИСКА
lines.sort(key = MyFn)
## 4!


# 5 СОЗДАНИЕ КОПИИ
rez_line = lines
## 5 !


# 6 ОСНОВНОЙ 3-ой ЦИКЛ
num = len(lines)
for i in range(0, num):
    names = re.split(" |\n", rez_line[i]) # каждую строку разбиваем на 2
    count = 1
    ancestor_name = names[1]  # это имя предка
    for k in range(0, num):
        bstop = True
        for j in range(0, num):
            cur_names = re.split(" |\n", lines[j])
            if cur_names[0] == ancestor_name:
                count = count + 1
                ancestor_name = cur_names[1]
                bstop = False
                break
        if bstop:
            break
    rez_line[i] = names[0] + ' '
    rez_line[i] = rez_line[i] + str(count)

print("##############################################################")
print("######### REZULTS   ###########################################")
print("##############################################################")

for line in rez_line:
    print(line.strip())

print("HELLO!")
time.sleep(10)
# ВОПРОС. КОГДА ЗАПУСКАЮ EXE ПОЧЕМУ НЕ ВЫВОДИТ НА КОНСОЬ СТРОКИ?
# ВОПРОС. ПРОСТО ТАК НЕ СПЛИТИСЯ надо через re. ЧТО ЭТО ТАКОЕ?
# ВОПРОС. ЗАПИХАТЬ В ФАЙЛ
# ВОПРОС. НЕ РАБОТАЕТ time.sleep()
f.close()

os.remove('rezults.txt')
f1 = open('rezults.txt', 'a')

for i in range (0, len(rez_line)):
    f1.write(rez_line[i] +'\n')
f1.close()

print("The end")

