def C(n, k):
    if n == 0:
        if k == 0:
            return 1
        else:
            return 0
    if k >n :
        return 0
    if k == n:
        return 1
    return C(n-1, k) + C(n-1, k -1)

rez = C(15, 2)
rez1 = 15 * 14 /2
print(str(rez))