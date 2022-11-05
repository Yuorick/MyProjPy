def eratosfen(N):
    ls = []
    for i in range(2, N+1):
        ls.append(i)
    for i in range (N):
        m = len(ls)
        for j in range (0, m -1 ):
            if ls[m - 1 - j]%ls[0] == 0:
                ls.pop(m - 1 - j )
        print(str(ls[0]))
        if len(ls) == 1:
            break
        ls = ls[1:]

eratosfen(15)