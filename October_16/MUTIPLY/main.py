def pow_new(a, n):

    while True:
        if n == 1:
            return  a
        else:
            p = n % 2

            if p == 0:
                return pow_new(a*a, n //2)
            else:
                return a * pow_new(a, n -1)

rez = pow_new(3,5)
print(str(rez))

