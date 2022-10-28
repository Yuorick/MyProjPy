def gcd(a, b):
    if a == 0 or b == 0:
        return max(a,b)
    else:
        if a > b:
            return gcd (a %b,b)
        else:
            return gcd(a, b % a)


def gcd_(a, b):
    if b == 0:
        return a
    else:
        return gcd (b, a %b)


rez = gcd_ (23 *5 *2, 14* 23)
print(str(rez))