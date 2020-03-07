import matplotlib.pyplot as plt
import os
import random as r
import operator
import time
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
        merge(left, right, compare)

#-------------merge--------------------------------------------

#--------------insertion------------------------------------------
def insertion_sort(nums):  
    nums1=nums[:]
    countt=0
    leng=len(nums)
    for i in range(1, leng):
        item_to_insert = nums1[i]
        
        j = i - 1
        #########
        countt+=1
        while j >= 0 and nums1[j] > item_to_insert:
            #############
            countt+=1
            nums1[j + 1] = nums1[j]
            j -= 1
        
        nums1[j + 1] = item_to_insert
#--------------insertion------------------------------------------




from random import shuffle

# def compare_ins_and_merge()
# def test(f,data):
def best_case(n):
    i=0
    arr = [i for i in range(i, n + 1)]
    return arr


def random_case(n):
    i=0
    arr = [i for i in range(i, n + 1)]
    shuffle(arr)
    return arr


def worst_case(n):
    i=0
    arr = [i for i in range(i, n + 1)]
    arr = list(reversed(arr))
    return arr

    


def test(f,data):
    repeats=3
    start = time.perf_counter()
    for i in range (repeats):
        f(data[i])
    end = time.perf_counter()
    return (end-start)/repeats


len = 10
arr1 = best_case(len);
arr3 = worst_case(len);
arr2 = random_case(len);
data = [arr1, arr2, arr3]

value = test(insertion_sort, data);

#plt.plot(#n1,count, "--y",
         #n1,count2, "--k",
         #n1,count3, "--r",
         #n1, countB, ":y",
         #n1, countB2, ":k",
         #n1, countB3, ":r",
         #n1, countW, "y",
         #n1, countW2, "k",
         #n1, countW3, "r"
         #)
#plt.xlabel("length of list")
#plt.ylabel("counter")
#plt.legend(("random case bubble_sort","random case better_bubble_sort","random case insertion_sort","best case bubble_sort", "best case better_bubble_sort","best case insertion_sort","worst case bubble_sort","worst case better_bubble_sort","worst case insertion_sort"))
#plt.show()
