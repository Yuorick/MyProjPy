49n = int(input('Введите натуральное число:'))

def MinDiviser(n):
    if n < 4:
        return n
    nc = int(pow(n,0.5))
    for i in range(2, nc +1):
        if n % i == 0:
            return i
    return n

m = MinDiviser(n)
print("Наименьший делитель =   ",str(MinDiviser(n)))
