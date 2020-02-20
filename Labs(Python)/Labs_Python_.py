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
for i in range(n):
    list.append(i+1)
r.shuffle(list)
print("Random before")
print(list)
print()
count=0
for i in range(n):
    worst.append(10-i)
print("Worst before")
print(worst)
print()
countW=0
print()

#----------------------------------------better bouble-----------------
def better_bubble_sort(nums, countt):
    for i in range(n-1):
        for j in range(n-1):
            countt+=1
            if best[j]>best[j+1]:
                best[j],best[j+1]=best[j+1],best[j]
        
        if best==bestT:
            break
#----------------------------------------better bouble-----------------


#--------------insertion------------------------------------------
def insertion_sort(nums, countt):  
    
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        
        j = i - 1
       
        while j >= 0 and nums[j] > item_to_insert:
            countt+=1
            nums[j + 1] = nums[j]
            j -= 1
        
        nums[j + 1] = item_to_insert
#--------------insertion------------------------------------------

#--------------bubble------------------------------------------
def bubble_sort(nums, countt):  
    
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            countt+=1
            if nums[i] > nums[i + 1]:
                
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
               
                swapped = True
#--------------bubble------------------------------------------

insertion_sort(list, count)
print("Random after")
print(list)
print()
print(count,"\n","--------------------")

fig = plt.figure()
graph1 = plt.plot([countB,count,countW],[countB,count,countW])
plt.show()


