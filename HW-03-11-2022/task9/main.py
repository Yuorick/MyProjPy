def quantDifNUms(ls):
    quant = 0
    for i in range (100000):
        m = len(ls)
        for j in range(m -1):
            if ls[m - 1 - j] == ls[0]:
                ls.pop(m - 1 - j)
        quant += 1
        if len(ls) == 1:
            break
        ls = ls[1:]
    return quant
ls = [1, 2, 3, 2, 1,5,5,5,5,6,7,2,2,7,7,7,7]
print(str(quantDifNUms(ls)))