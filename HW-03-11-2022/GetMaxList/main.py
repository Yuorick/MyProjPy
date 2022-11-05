def GetMaxList(ls):
    if len(ls) == 1:
        return ls[0]
    else:
        return max(ls[0],GetMaxList(ls[1:]))

ls = [ 500, 2300, 800, 114, 36]
print(str(GetMaxList(ls)))