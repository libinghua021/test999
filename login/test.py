import random

list = random.choices(range(1, 34), k=6, weights=range(1, 34))
print(list)
n=len(list)
print(n)
for x in range(n-1):
    for y in range(x+1,n):
        if list[x]>list[y]:
            list[x],list[y]=list[y],list[x]
print(list)
