def greedy(s, ls):
    ls.sort()
    scur = 0
    i0 = 0
    for i in range(len(ls)):
        scur += ls[i]
        if scur > s:
            return i0
        else:
            i0 += 1

    return len(ls)

ls = [50,30,50]
s = 100
print (str(greedy(s, ls)))