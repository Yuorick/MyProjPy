def sumTwoPositInts(n, m):
    if m == 0:
        return n
    else:
        return sumTwoPositInts(n +1, m - 1)
n = int(input("Введите первое слагаемое:  "))
m = int(input("Введите второе слагаемое:  "))

k = sumTwoPositInts(n, m)
print(str(k))
