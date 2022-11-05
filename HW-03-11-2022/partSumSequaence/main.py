def partSumSequaence(pstr):
    ls_str = pstr.split(' ')
    psrtRez = ''
    sum = 0
    for l in ls_str:
        sum += int(l)
        psrtRez += str(sum) + ' '
    psrtRez ='(' + psrtRez[:-1] + ')'
    return psrtRez

pstr = '2 56 8'
print(partSumSequaence(pstr))