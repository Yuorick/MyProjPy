def factorials():
    N = int(input('Введите N:'))
    prod = 1
    print (str(prod))
    for i in range(1,N+1):
        prod *= i
        print(str(prod))
    return

factorials()


