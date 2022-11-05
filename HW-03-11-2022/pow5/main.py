def multPow5(ls):
    prod =1
    for l in ls:
        prod *= l
    t = prod *prod
    t1 = t * prod
    return t * t1

ls = [1000000,2000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000]


print(str(multPow5(ls)))