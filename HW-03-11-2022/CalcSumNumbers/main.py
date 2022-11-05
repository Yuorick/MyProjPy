def CalcSumNumbers(ls):
    if len(ls) == 0:
        return 0
    else:
        sum = CalcSumNumbers(ls[1:])
        sum += ls[0]
        return sum


ls  = [2, 3, 8]
print(str(CalcSumNumbers(ls)))
