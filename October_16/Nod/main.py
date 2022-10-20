def gcd(a, b):
    if a == 0 or b == 0:
        return max(a,b)
    else:
        if a > b:
            return gcd (a %b,b)
        else:
            return gcd(a, b % a)

rez = gcd (23 *5, 14* 5)
print(str(rez))