def xor(ls0, ls1):
    lsRez = []
    for i in range(len(ls0)):
        lsRez.append((ls0[i] + ls1[i]) % 2)
    return lsRez
def multiXOR(ls):

    if len(ls) == 1:
        return ls[0]
    lsRez = ls[0]
    for i in range(1, len(ls)):
        lsRez = xor(lsRez, ls[i])
    return lsRez
l0 = [0, 0, 0, 0]
l1 = [1, 1, 1, 1]
l2 = [0, 1, 0, 1]
ls = [l0, l1,l2]
print(multiXOR(ls))