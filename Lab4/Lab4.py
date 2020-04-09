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

def quick_sort1(A,p,r):
    global count1
    if p < r:
        if r-p>2:
            q = partition2(A,p,r)
            quick_sort1(A,p,q-1)
            quick_sort1(A,q+1,r)
        elif r-p==2:
            medianfirst(A,p,p+1,r)
            
            count1+=3
        elif r-p==1:
            compareswap(A,p,r)
            count1+=1


            
def partition2(A,p,r):
    global count1
    middle = (p + r) // 2
    medianfirst(A, p, middle, r)
    A[middle], A[r] = A[r], A[middle]
    x=A[r]
    i=p-1
    for j in range(p,r):
        count1+=1

        if  A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1



def compareswap(A, a, b):
    if A[a]>A[b]:
        A[a], A[b] = A[b],A[a]


def medianfirst(A, a, b, c):
    compareswap(A, a, b)  
    compareswap(A, b, c) 
    compareswap(A, a, b)



########## with 3 medians ###############


#name = input()
count = 0
count1 = 0
f = open('inputs/input_16_10000.txt','r')
l = [line.strip() for line in f]
intl =[]
for i in l:
    intl.append(int(i))
amount = intl.pop(0)

f = open('inputs/input_16_10000.txt','r')
l1 = [line.strip() for line in f]
intl1 =[]
for i in l1:
    intl1.append(int(i))
amount1 = intl1.pop(0)


#print(amount)
#print(intl);
quick_sort(intl,0,amount-1)
quick_sort1(intl1,0,amount1-1)

print(count," ",count1)
#print(intl)


f = open('outputs/khmelinin_output_16_10000.txt','w')
f.write(str(count) + ' ' + str(count1))

