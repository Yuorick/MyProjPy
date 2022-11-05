def minOddNum(ls):
    # поиск первого нечетного элемента
    rez = 0
    for i in range(len(ls)):
        if ls[i]%2 == 1:
            if i == (len(ls) -1):
                return ls[-1]
            rez = ls[i]
            ls = ls[i+1:]
            break
    # поиск минимума
    for i in range(len(ls)):
        if ls[i] % 2 == 1 :
            rez = min(rez, ls[i])

    return rez

ls =[ 0, 10,2 ,3, 4]

print(minOddNum(ls))