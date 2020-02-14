import random as r
n=10
list=[]
worst=[]
best=[]

for i in range(n):
    best.append(i+1)
print("Best before")
print(best)
print()
countB=0

for i in range(n-1):
    for j in range(n-1):
        if best[j]>best[j+1]:
            best[j],best[j+1]=best[j+1],best[j]
            countB+=1
print("Best after")
print(best)
print()
print(countB)

for i in range(n):
    list.append(i+1)
r.shuffle(list)
print("Random before")
print(list)
print()
count=0

for i in range(n-1):
    for j in range(n-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
            count+=1
print("Random after")
print(list)
print()
print(count)
#------------------------
for i in range(n):
    worst.append(10-i)
print("Worst before")
print(worst)
print()
countW=0

for i in range(n-1):
    for j in range(n-1):
        if worst[j]>worst[j+1]:
            worst[j],worst[j+1]=worst[j+1],worst[j]
            countW+=1
print("Worst after")
print(worst)
print()
print(countW)