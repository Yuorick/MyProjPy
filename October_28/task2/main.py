def minPositive(ls):
    min = 1001
    for a in ls:
        if a > 0 and a <min:
            min = a
    return a
ls = [5, -4, 3, -2, 1]
print(str(minPositive(ls)))