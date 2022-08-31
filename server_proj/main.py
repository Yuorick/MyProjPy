import pandas
import os
import re
# библиотека работы с exlel файлпами
import openpyxl
df = pandas.read_excel("BOOK_KEEP.xlsx")

df= df.fillna(0)

# выбор столбца
print(df['ПРОДУКТЫ'].sum())
seria = df["Unnamed: 0"]
print (seria)
print(type(seria))

list = seria.tolist()
print (list)


# ЗАДАЧА 2
print("\n\n\nBegin task 2\n")
f2 = open("input.txt", 'rt')
lines = f2.readlines()

## 1!

j_sootv = int(lines[0])
print(j_sootv)
i_records_num = int(lines[j_sootv+1])
print("i_records_num =" + str(i_records_num))

list_sootv = ['q' for i in range(0, 2 * j_sootv)]
for i in range(0, j_sootv):
    listcur = re.split(" |\n",lines[i + 1])
    list_sootv[2*i] = listcur[0]
    list_sootv[2*i +1] = listcur[1]

print("начало")

list_rez = [str(-1) for i in range(i_records_num)]


for i in range(0, i_records_num):
    name = re.split(" |\n", lines[2 + j_sootv + i])
    name_cur = name[0]

    try:
        ind = list_sootv.index(name_cur)

    except ValueError:
        a=1
    else:
        list_rez[i] = list_sootv[ind + 1]
        b=1


print(list_rez)




f2.close()
print("The end")