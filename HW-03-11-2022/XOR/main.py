def xor(pstr0, pstr1):
    pstrRez = ''
    ls0 = pstr0.split(' ')
    t = int(ls0[0])
    ls1 = pstr1.split(' ')
    for i in range(len(ls0)- 1):
        pstrRez  = pstrRez + str((int(ls0[i]) + int(ls1[i])) % 2) + ' '

    pstrRez = pstrRez + str((int(ls0[-1]) + int(ls1[-1])) % 2)
    return pstrRez

pstr0 = '1 2 54 123'
pstr1 = '2 3 4 5'
pstr = xor(pstr0, pstr1)
print(pstr)
