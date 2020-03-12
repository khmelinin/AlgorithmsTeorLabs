import matplotlib.pyplot as plt
import random as r
import copy
import time
#-------------merge--------------------------------------------

def merge_sort(L,begin,end):
    if len(L) < 2:
        return L[:]
    else:
        middle = int((end-begin+1)/2+begin)
        left = merge_sort(L[begin:middle],0,len(L[begin:middle])-1)
        right = merge_sort(L[middle:end+1],0,len(L[middle:end+1])-1)
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i]<right[j]:
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

#-------------merge--------------------------------------------

#--------------insertion------------------------------------------
def insertion_sort(nums,begin,end):  
    nums1=nums[:]
    countt=0
    for i in range(begin+1, end+1):

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
def test(f,data):
    repeats1 = len(data)

    start = time.perf_counter()

    for i in range(repeats1):

        # тут можна вивести поточну вхідну послідовність для сортування

        #print (data[i])

        f(data[i], 0, len(data[i])-1)

        # тут можна вивести поточну відсортовану послідовність

        #print data[i], '\n'

    end = time.perf_counter()

    print((end-start)/repeats1, '\n')

    return (end-start)/repeats1

def compare_ins_and_merge():
     # параметри для проведення експерименту
    repeats = 1000    # кількість запусків для однієї розмірності
    n_begin = 1        # початкова розмірність задачі
    n_end   = 200    # кінцева розмірність задачі
    n_step  = 5        # крок розмірності

    t_ins, t_mer,t_comp=[],[],[]
    for n in range(n_begin,n_end+1,n_step):

        data = [generate_data(n) for i in range(repeats)]
        a=test(insertion_sort, copy.deepcopy(data))
        t_ins.append(a)
        b=test(merge_sort,copy.deepcopy(data))
        t_mer.append(b)
        c= a/b
        t_comp.append(c)
        print( "\nDATA SIZE:",n)
        print("Merge time for size", n, ":", b)
        print("Insertion time for size", n, ":", a)
        print("Ratio insertion/merge:", c)
    x=list(range(n_begin,n_end+1,n_step))
    plt.plot(x,t_ins,"k",
             x,t_mer,"r")
    plt.xlabel("length of list")
    plt.ylabel("time")
    plt.legend(("insertion_sort","merge_sort"))
    plt.show()
    plt.plot(x,t_comp,"k",
             x,[1]*len(x),"r")
    plt.xlabel("length of list")
    plt.ylabel("insertion time / merge time")
    
    plt.show()


def generate_data(kk):
    data123=list(range(kk))
    r.shuffle(data123)
    return data123


compare_ins_and_merge()