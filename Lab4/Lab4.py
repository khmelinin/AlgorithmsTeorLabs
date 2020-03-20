def quick_sort(A,p,r):

    if p < r:
        q = partition(A,p,r)
        quick_sort(A,p,q-1)
        quick_sort(A,q+1,r)

def partition(A,p,r):
    global count
    x=A[r]
    i=p-1
    for j in range(p,r):
        count+=1
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

########## with 3 medians ###############
def quickSort(L, ascending = True): 
    quicksorthelp(L, 0, len(L), ascending)
    
    


def quicksorthelp(L, low, high, ascending = True): 
    result = 0
    global count1

    if low < high:
        
        pivot_location, result = Partition(L, low, high, ascending)  
        result += quicksorthelp(L, low, pivot_location, ascending)  
        result += quicksorthelp(L, pivot_location + 1, high, ascending)
    return result

def Partition(L, low, high, ascending = True):
    global count1
    #print('Quicksort, Parameter L:')
    #print(L)
    result = 0 
    pivot, pidx = median_of_three(L, low, high)
    L[low], L[pidx] = L[pidx], L[low]
    i = low + 1
    for j in range(low+1, high, 1):
        result += 1
        if (ascending and L[j] < pivot) or (not ascending and L[j] > pivot):
            L[i], L[j] = L[j], L[i]  
            i += 1
    L[low], L[i-1] = L[i-1], L[low] 
    return i - 1, result


def median_of_three(L, low, high):
    mid = (low+high-1)//2
    a = L[low]
    b = L[mid]
    c = L[high-1]
    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, high-1
    if b <= c <= a:
        return c, high-1
    return a, low

########## with 3 medians ###############

#name = input()
count = 0
count1 = 0
f = open('inputs/input_09_100.txt','r')
l = [line.strip() for line in f]
intl =[]
for i in l:
    intl.append(int(i))
amount = intl.pop(0)
#print(amount)
#print(intl);
#quick_sort(intl,0,amount-1)
quickSort(intl)
print(count1)
#print(intl)
#print(count)



f = open('outputs/Aoutput_01_10.txt','w')
f.write(str(count) + ' ')

