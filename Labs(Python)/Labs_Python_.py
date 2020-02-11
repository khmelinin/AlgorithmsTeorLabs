import random as r
n=100
list=[]
for i in range(n):
    list.append(round(r.randint(-n,n),2))
print(list)
for i in range(n-1):
    for j in range(n-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print(list)
