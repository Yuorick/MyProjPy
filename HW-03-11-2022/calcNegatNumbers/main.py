def calcQuantNegativeNumbers(ls):
    if len(ls) ==0:
        return 0
    else:
        rez = calcQuantNegativeNumbers(ls[1:])
        if ls[0] < 0:
            rez += 1
        return rez

ls = [ -2, 3, 8, -11, -4, 6 ]
print(str(calcQuantNegativeNumbers(ls)))
