def task7():
    n = int(input('input digit:'))
    if n != 0:
        task7()
    print('out = ',str(n))

task7()


