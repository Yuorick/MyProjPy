def quntElem(ls):
    if len(ls) == 0:
        return 0
    elemCur = ls[0]
    chetchik = 1
    for i in range(1, len(ls) ):
        if ls[i] == elemCur:
            continue
        chetchik += 1
        elemCur = ls[i]
    return chetchik





ls  = [1, 2, 2, 3, 3, 3,5]
print(str(quntElem(ls)))

