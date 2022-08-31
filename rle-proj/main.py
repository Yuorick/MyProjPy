f = open('rle.txt', 'rt')
ls = f.read()
print(ls)
ls1 = ls.strip()
len(ls1)
print(ls1)
print(ls1[1])
str_rez = ""
curPosNum = 0
while True:
    if curPosNum == len(ls1):break
    cur_n = 1
    cur_letter = ls1[curPosNum]
    icur = curPosNum
    for j in range(icur + 1, len(ls1)):
        if ls1[j] != cur_letter:
            break
        else:
            cur_n = cur_n + 1
            curPosNum = curPosNum + 1
    lst_cur = []
    if cur_n == 1:
        str_rez += cur_letter
    else:
        str_rez += str(cur_n)
        str_rez += cur_letter

    curPosNum = curPosNum + 1




print(str_rez)




