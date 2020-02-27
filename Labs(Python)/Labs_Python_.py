import matplotlib.pyplot as plt
import numpy as np
import os
import random as r
#--------------bubble------------------------------------------
def bubble_sort(nums):
    nums1=nums[:]
    countt=0
    for i in range(n-1):
        for j in range(n-1):
            countt+=1
            if nums1[j]>nums1[j+1]:
                nums1[j],nums1[j+1]=nums1[j+1],nums1[j]
    return countt
#--------------bubble------------------------------------------
#----------------------------------------better bubble-----------------
def better_bubble_sort(nums):
    countt=0
    nums1=nums[:]
    for i in range(n-1):
        sorted=True
        for j in range(n-1):
            countt+=1
            if nums1[j]>nums1[j+1]:
                nums1[j],nums1[j+1]=nums1[j+1],nums1[j]
                sorted=False
        if sorted==True:
            return countt
    return countt

#----------------------------------------better bubble-----------------
#--------------insertion------------------------------------------
def insertion_sort(nums):  
    nums1=nums[:]
    countt=0
    for i in range(1, len(nums)):
        item_to_insert = nums1[i]
        
        j = i - 1
        countt+=1
        while j >= 0 and nums1[j] > item_to_insert:
            countt+=1
            nums1[j + 1] = nums1[j]
            j -= 1
        
        nums1[j + 1] = item_to_insert
    return countt
#--------------insertion------------------------------------------






n1=list(range(10,1010,10))

count=[]
count2=[]
count3=[]
countB=[]
countB2=[]
countB3=[]
countW=[]
countW2=[]
countW3=[]
for n in n1:


    best=list(range(1,n+1))

    #print("Best before")
    #print(best,"\n")



    list1=best[:]
    r.shuffle(list1)
    #print("Random before")
    #print(list,"\n")


    worst=list(range(n,0,-1))

    #print("Worst before")
    #print(worst,"\n\n")

    countB.append(bubble_sort(best))

    count.append(bubble_sort(list1))

    countW.append(bubble_sort(worst))

    #print("Bubble")
    #print("\nBest after counter = ",a)
    #print(countB)
    #print("\nRandom after counter = ",b)
    #print(count)
    #print("\nWorst after counter = ",c)
    #print(countW)
    #print("\n____________________________")

    countB2.append(better_bubble_sort(best))

    count2.append(better_bubble_sort(list1))

    countW2.append(better_bubble_sort(worst))

    #print("Better_Bubble")
    #print("\nBest after counter = ",a)
    #print(countB2)
    #print("\nRandom after counter = ",b)
    #print(count2)
    #print("\nWorst after counter = ",c)
    #print(countW2)
    #print("\n____________________________")
    countB3.append(insertion_sort(best))

    count3.append(insertion_sort(list1))

    countW3.append(insertion_sort(worst))

    #print("Insertion")
    #print("\nBest after counter = ",a)
    #print(countB3)
    #print("\nRandom after counter = ",b)
    #print(count3)
    #print("\nWorst after counter = ",c)
    #print(countW3)
    #print("\n____________________________")




plt.plot(n1,count, "--y",
         n1,count2, "--k",
         n1,count3, "--r",
         n1, countB, ":y",
         n1, countB2, ":k",
         n1, countB3, ":r",
         n1, countW, "y",
         n1, countW2, "k",
         n1, countW3, "r"
         )
plt.xlabel("length of list")
plt.ylabel("counter")
plt.legend(("random case bubble_sort","random case better_bubble_sort","random case insertion_sort","best case bubble_sort", "best case better_bubble_sort","best case insertion_sort","worst case bubble_sort","worst case better_bubble_sort","worst case insertion_sort"))
plt.show()