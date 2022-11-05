def existZero():
   N = int(input('Введите N:'))
   for i in range(N):
       n = int(input('введите число n: '))
       if n == 0:
           return str("TRUE")

   return "FALSE"

print (existZero())