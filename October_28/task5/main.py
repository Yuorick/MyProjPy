def unicList(ls):
    lsRez=[]
    n0 = len(ls)
    for i in range (n0):
        if len(ls) == 0:
            return lsRez
        if len(ls) == 1:
            lsRez.append(ls[0])
            return lsRez
        lsRez.append(ls[0])
        nc = len(ls)
        for j in range (0, nc -2):
            if ls[nc -1 - j] == ls[0]:
                ls.pop(nc -1 - j)
        ls = ls[1:]
    return lsRez

ls = [1,5, 1,2,1,3, 4,3]
a  = ls[-1]
b = ls[0]
lsREz = unicList(ls)
print(unicList(ls))