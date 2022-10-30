def sdvig(ls):
    l0 = ls[-1]
    ls[1:] = ls[:-1]
    ls[0] = l0

ls = [1,2,3,4,5]
sdvig(ls)
print(ls)