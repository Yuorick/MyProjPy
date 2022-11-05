def GetFibonacciList(n0, n1,N):
    if n1 >N:
        return
    else:
        GetFibonacciList(n1, n0 +n1, N)
        print(str(n1))

def GetFibonacciList_(n0, n1,N, lrez):
    if n1 >N:
        lrez = []
        return
    else:
        GetFibonacciList_(n1, n0 +n1, N, lrez)
        lrez.insert(0, n1)
lrez = []
GetFibonacciList_(1, 2,50, lrez)
print(lrez)