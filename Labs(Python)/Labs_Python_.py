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
print("\n","____________________________")
bestT=best

def reset():
    best.clear()
    for i in range(n):
        best.append(i+1)
    bestT=best[:]
    countB=0
    list.clear()
    for i in range(n):
        list.append(i+1)
    r.shuffle(list)
    count=0
    worst.clear()
    for i in range(n):
        worst.append(10-i)
    countW=0
    print()

#----------------------------------------better bouble-----------------
def better_bubble_sort(nums, countt):
    for i in range(n-1):
        sorted = True
        for j in range(n-1):
            countt+=1
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                sorted = False
        
        if sorted==True:
            break
    return countt
#----------------------------------------better bouble-----------------


#--------------insertion------------------------------------------
def insertion_sort(nums, countt):  
    
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        
        j = i - 1
        countt+=1
        while j >= 0 and nums[j] > item_to_insert:
            countt+=1
            nums[j + 1] = nums[j]
            j -= 1
        
        nums[j + 1] = item_to_insert
    return countt
#--------------insertion------------------------------------------

#--------------bubble------------------------------------------
def bubble_sort(nums, countt):
    for i in range(n-1):
        for j in range(n-1):
            countt+=1
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return countt
#--------------bubble------------------------------------------

print("Bubble")
BcountB = bubble_sort(best, countB)
print("\n","Best after counter = ",BcountB)
print(best)
Bcount = bubble_sort(list, count)
print("\n","Random after counter = ",Bcount)
print(list)
BcountW = bubble_sort(worst, countW)
print("\n","Worst after counter = ",BcountW)
print(worst)
print("\n","____________________________")

reset()

print("Better_Bubble")
BBcountB = better_bubble_sort(best, countB)
print("\n","Best after counter = ",BBcountB)
print(best)
BBcount = better_bubble_sort(list, count)
print("\n","Random after counter = ",BBcount)
print(list)
BBcountW = better_bubble_sort(worst, countW)
print("\n","Worst after counter = ",BBcountW)
print(worst)
print("\n","____________________________")

reset()

print("Insertion")
IcountB = insertion_sort(best, countB)
print("\n","Best after counter = ",IcountB)
print(best)
Icount = insertion_sort(list, count)
print("\n","Random after counter = ",Icount)
print(list)
IcountW = insertion_sort(worst, countW)
print("\n","Worst after counter = ",IcountW)
print(worst)
print("\n","____________________________")

#graph1 = plt.plot([0,Bcount,100],[0,Bcount,100])
#plt.show()


