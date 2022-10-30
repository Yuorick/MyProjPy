def squize(ls):
    quantCur0 = 0
    quantTotal0 = 0
    pcur = 0
    n = len(ls)
    for i in range(n):
        if quantTotal0 + pcur == len(ls):
            return

        if ls[pcur +quantCur0] != 0:
            if quantCur0 == 0:
                pcur += 1
                continue
            i0 = pcur
            i1 = n - pcur - quantCur0 +1
            i2 = pcur + quantCur0
            ls[pcur : n - pcur - quantCur0 +1] = ls[pcur + quantCur0:]
            if quantCur0 > 0:
                ls[n  - quantCur0:] = [0] * quantCur0

            quantTotal0 += quantCur0
            quantCur0 = 0
            pcur += 1
        else:
            quantCur0 += 1



ls = [4, 0, 5, 0, 3, 0, 0, 5]
squize(ls)
print(ls)