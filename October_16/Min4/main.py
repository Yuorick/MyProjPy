a = input("Input a:")
b = input("Input b:")
c = input("Input c:")
d = input("Input d:")

print('min4 = ', str((lambda a,b,c,d: min(d,(min(c,min(a,b)))))(a,b,c,d)))
q = min(a,b,c,d)
print('q= ', str(q))

