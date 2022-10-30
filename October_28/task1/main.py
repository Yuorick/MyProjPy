def sign(a):
    if a < 0:
        return -1
    else:
        if a >0:
            return 1
        else:
            return 0
def CalcSumNumbers(ls):
    for i in range (len(ls)):
        it0 = sign(ls[i])
        if it0 == 0:
            continue
        it1 = sign(ls[i +1])
        if it0 == it1:
            return ls[i:i+2]


ls = [1, 2, -3, -4, -5]
rez = CalcSumNumbers(ls)
print(rez)
