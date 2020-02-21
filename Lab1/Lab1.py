
import matplotlib.pyplot as plt
import numpy as np
import os
import random as r
n=10
list=[]
worst=[]
best=[]
bestT=[]

for i in range(n):
    best.append(i+1)
print("Best before")
print(best)
bestT=best
print()
countB=0

for i in range(n-1):
    for j in range(n-1):
        countB+=1
        if best[j]>best[j+1]:
            best[j],best[j+1]=best[j+1],best[j]
        
    if best==bestT:
        break

print("Best after")
print(best)
print()
print(countB,"\n","--------------------")
#------------------------
for i in range(n):
    list.append(i+1)
r.shuffle(list)
print("Random before")
print(list)
listT=list
print()
count=0

for i in range(n-1):
    for j in range(n-1):
        count+=1
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
        
    if list==bestT:
        break
print("Random after")
print(list)
print()
print(count,"\n","--------------------")
#------------------------
for i in range(n):
    worst.append(10-i)
print("Worst before")
print(worst)
worstT=worst
print()
countW=0

for i in range(n-1):
    for j in range(n-1):
        countW+=1
        if worst[j]>worst[j+1]:
            worst[j],worst[j+1]=worst[j+1],worst[j]
        
    if worst==bestT:
        break
print("Worst after")
print(worst)
print()
print(countW,"\n","--------------------")




fig = plt.figure()
graph1 = plt.plot([countB,count,countW],[countB,count,countW])
plt.show()
