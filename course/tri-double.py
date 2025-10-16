import time as t
from random import randint

numbers = [randint(0,100) for _ in range(200)]

start = t.time()

def sortAndDelDuos(alist:list)->list :
    newlist = []
    for ele in alist:
        if ele not in newlist :
            newlist.append(ele)
    return newlist

print(sortAndDelDuos(numbers))
stop = t.time()
print(stop-start)