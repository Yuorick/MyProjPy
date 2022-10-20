def isPrime(n):
    if n < 4:
        return "YES"
    nc = int(pow(float(n), 0.5))
    for i in range(2, nc + 1):
        if n%i == 0:
            return "NO"
    return "YES"
n = int(input("Введите целое число:  "))
print (isPrime(n))

