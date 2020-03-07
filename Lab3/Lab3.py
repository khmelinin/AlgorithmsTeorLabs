import matplotlib.pyplot as plt
import numpy as np
import os
import random as r
import operator
#-------------merge--------------------------------------------
def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)

#-------------merge--------------------------------------------

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






n1=list(range(10,110,10))

count=[]
#count2=[]
count3=[]
countB=[]
#countB2=[]
countB3=[]
countW=[]
#countW2=[]
countW3=[]
for n in n1:


    best=list(range(1,n+1))

    #print("Best before")
    print(best,"\n")



    list1=best[:]
    r.shuffle(list1)
    print("Random before")
    print(list,"\n")


    worst=list(range(n,0,-1))

    print("Worst before")
    print(worst,"\n\n")


    #print("Bubble")
    #print("\nBest after counter = ",a)
    #print(countB)
    #print("\nRandom after counter = ",b)
    #print(count)
    #print("\nWorst after counter = ",c)
    #print(countW)
    #print("\n____________________________")


    #print("Better_Bubble")
    #print("\nBest after counter = ",a)
    #print(countB2)
    #print("\nRandom after counter = ",b)
    #print(count2)
    #print("\nWorst after counter = ",c)
    #print(countW2)
    #print("\n____________________________")

    merge_sort(best)

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




plt.plot(#n1,count, "--y",
         #n1,count2, "--k",
         n1,count3, "--r",
         #n1, countB, ":y",
         #n1, countB2, ":k",
         n1, countB3, ":r",
         #n1, countW, "y",
         #n1, countW2, "k",
         n1, countW3, "r"
         )
plt.xlabel("length of list")
plt.ylabel("counter")
plt.legend(("random case bubble_sort","random case better_bubble_sort","random case insertion_sort","best case bubble_sort", "best case better_bubble_sort","best case insertion_sort","worst case bubble_sort","worst case better_bubble_sort","worst case insertion_sort"))
plt.show()