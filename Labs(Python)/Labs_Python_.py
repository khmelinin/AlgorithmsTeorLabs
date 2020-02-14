import random as r
n=10
list=[]
worst=[]

for i in range(n):
    list.append(i+1)
r.shuffle(list)
print("before")
print(list)
print()
count=0

for i in range(n-1):
    for j in range(n-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
            count+=1
print("after")
print(list)
print()
print(count)
#------------------------
for i in range(n):
    worst.append(10-i)
print("before")
print(worst)
print()
countW=0

for i in range(n-1):
    for j in range(n-1):
        if worst[j]>worst[j+1]:
            worst[j],worst[j+1]=worst[j+1],worst[j]
            countW+=1
print("after")
print(worst)
print()
print(countW)