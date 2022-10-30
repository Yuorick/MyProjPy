def queens(ls):
    setRows = set()
    setCols = set()
    setSum = set()
    setMin = set()
    for i in range (8):
        setRows.add(ls[i * 2])
        setCols.add(ls[i * 2 +1])
        setSum.add(ls[i * 2 + 1] - ls[i * 2])
        setMin.add(ls[i * 2 + 1] + ls[i * 2])
    if len(setRows) + len(setCols) + len(setSum) + len(setMin)  < 64:
        return False
    return True

ls = [1, 8
,2, 7
,3, 6
,4, 5
,5, 4
,6, 3
,7, 2
,8, 1
]
b = queens(ls)
print(b)