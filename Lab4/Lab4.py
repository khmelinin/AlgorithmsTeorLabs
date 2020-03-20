########## regular quicksort ############
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
########## regular quicksort ############

########## with 3 medians ###############

def compareswap(L, a, b):
    L[a], L[b] = min(L[a], L[b]), max(L[a], L[b])


def medianfirst(L, a, b, c):
    compareswap(L, b, a)  # L[b]<=L[a]
    compareswap(L, b, c)  # L[b]<=L[c] i.e L[b] smallest
    compareswap(L, a, c)


def Partition(L, low, high):
    global count1
    middle = (low + high - 1) // 2
    medianfirst(L, low, middle, high - 1)
    pivot = L[low]
    i = low + 1

    for j in range(low + 1, high, 1):
        count1+=1
        if L[j] < pivot:
            L[i], L[j] = L[j], L[i]
            i += 1
    L[low], L[i - 1] = L[i - 1], L[low]
    return i - 1


def quicksort1(L, low, high):
    global count1
    if low < high:
        pivot_location = Partition(L, low, high)
        quicksort1(L, low, pivot_location)
        quicksort1(L, pivot_location + 1, high)

########## with 3 medians ###############

########## Multi-Pivot ##################

def partition3(A, left, right):
    global count2
    a = left + 2
    b = left + 2
    c = right - 1
    d = right - 1
    p = A[left]
    q = A[left + 1]
    r = A[right]
    while b <= c:
        while A[b] < q and b <= c:
            if A[b] < p:
                A[a], A[b] = A[b], A[a]
                a+=1
            b = b + 1
        while A[c] > q and b <= c:
            if A[c] > r:
                A[c], A[d] = A[d], A[c]
                d = d - 1
            c = c - 1
        if b <= c:
            if A[b] > r:
                if A[c] < p:
                    A[b],A[a] = A[a],A[b]
                    A[a],A[c] = A[c],A[a]
                    a = a + 1
                else:
                    A[b],A[c] = A[c],A[b]
                A[c],A[d] =  A[d],A[c]
                b = b + 1
                c = c - 1
                d = d - 1
            else:
                if A[c] < p:
                    A[b],A[a] = A[a],A[b]
                    A[a],A[c] = A[c],A[a]
                    a = a + 1
                else:
                    A[b],A[c] = A[c],A[b]

                b = b + 1
                c = c - 1
    a -= 1
    b -= 1
    c += 1
    d += 1
    A[left + 1],A[a] = A[a], A[left+1]
    A[a],A[b] = A[b],A[a]
    a -= 1
    A[left],A[a] = A[a],A[left]
    A[right],A[d] = A[d],A[right]


########## Multi-Pivot ##################

#name = input()
count = 0
count1 = 0
count2 = 0
f = open('inputs/input_01_10.txt','r')
l = [line.strip() for line in f]
intl =[]
for i in l:
    intl.append(int(i))
amount = intl.pop(0)

f = open('inputs/input_01_10.txt','r')
l1 = [line.strip() for line in f]
intl1 =[]
for i in l1:
    intl1.append(int(i))
amount1 = intl1.pop(0)

f = open('inputs/input_01_10.txt','r')
l2 = [line.strip() for line in f]
intl2 =[]
for i in l2:
    intl2.append(int(i))
amount2 = intl2.pop(0)

#print(amount)
#print(intl);
quick_sort(intl,0,amount-1)
quicksort1(intl1,0,amount1-1)

print(count," ",count1," ", count2)
#print(intl)


f = open('outputs/Aoutput_01_10.txt','w')
f.write(str(count) + ' ' + str(count1) + ' ' +str(count2))

