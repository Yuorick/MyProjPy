def unicList(ls):
    for i in ls:
        if ls.count(i) == 1:
            print(str(i))


ls = [1,5, 1,2,1,3, 4,3]
a  = ls[-1]
b = ls[0]
unicList(ls)
