
# задан list: ls = [1,2,3,4,5]
# задан новый элемент : elem = 6
# надо создать все перстановки на основе ls и elem
# То есть,создать список из списков:
#[ [6, 1,2,3,4,5], [ 1,6,2,3,4,5], [1,2,6, 3,4,5]...]
def addElem(elem, ls):
    lsExtend = []
    lsCur = [elem]
    lsCur.extend(ls)
    lsExtend.append(lsCur)
    for i in range(len(ls)):
        lsCur = ls[:1 + i]
        lsCur.append(elem)
        lsCur.extend(ls[1 + i:])
        lsExtend.append(lsCur)
    return lsExtend

# Задан список списков типа:
# ls = [ [6, 1,2,3,4,5], [ 1,6,2,3,4,5], [1,2,6, 3,4,5]...]
# задан новый элемент elem, например,elem = 6
# надо для каждого элемента списка ls сделать новый спискок
# в соответствии с функцией addElem(elem, ls)
# и собрать это все в новый список
#
def  newList(elem, ls):
    lsRez = []
    for i in range(len(ls)):
        lsCur = addElem(elem, ls[i])
        lsRez.extend(lsCur)
    return lsRez
################################################
################################################
################################################
################################################

def perestanovki(N):
    lsElem = []
    for i in range(N+1):
        lsElem.append(i +1)
    lsRez = [[1]]
    if N== 1:
        return lsRez
    for i in range(1, N+1):
        lsRez = newList(lsElem[i], lsRez)
    lsRez.sort()
    for el in lsRez:
        pstr = str()
        for l in el:
            pstr += str(l)
        print(pstr)
    return lsRez
    
N = 3

kk = 0
print(perestanovki(N))
