def InorderTreePrint(x=0):
    global key, left, right
    if x!=None:
        InorderTreePrint(left[x])
        print(key[x])
        InorderTreePrint(right[x])

def InorderTreeWalk(ar, x=0):
    global key, left, right
    if x!=None:
        InorderTreeWalk(ar, left[x])
        ar.append(key[x])
        #print(key[x])
        InorderTreeWalk(ar, right[x])

def InorderTreeWalk2(ar, x=0):
    global ii
    if x!=None:
        InorderTreeWalk2(ar,left[x])
        key[x]=ar[ii]
        ii+=1
        InorderTreeWalk2(ar,right[x])
        
"""
def TreeSearch(x,k):
    if x == None or k == key[x]:
        return x
    if k < key[x]:
        return TreeSearch(left[x], k)
    else:
        return TreeSearch(right[x],k)

def IterativeTreeSearch(x,k):
    while x!=None and k!=key[x]:
        if k<key[x]:
            x=left[x]
        else:x=right[x]
    return x

def TreeMinimum(x):
    while left[x]!=None:
        x=left[x]
    return x

def TreeMaximum(x):
    while left[x]!=None:
        x=right[x]
    return x

def TreeSuccessor(x):
    if right[x]!=None:
        return TreeMinimum(right[x])
    y=parent[x]
    while y!=None and x == right[y]:
        x=y
        y=parent[y]
    return y
"""

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

def SortTheTree():
    array=[]
    InorderTreeWalk(array)
    array=merge_sort(array,0,len(array)-1)[:]
    #print(array)
    InorderTreeWalk2(array)


def FindSum(S,route,id,sum=0):
    global key,right,left, sums
    if id != None:
        if key[id]!=None:
            sum+=key[id]
            route.append(key[id])
            if sum==S:
                sums.append(route[:])
                return
            if sum >S:
                return
            FindSum(S, route[:], left[id],sum)
            FindSum(S,route[:],right[id],sum)
    

inputname=input("Input file name: ")
with open('Inputs/'+inputname) as f: #считываем input файл
    InputData = f.read().split()

left=[None]*len(InputData)
right=[None]*len(InputData)
parent=[None]*len(InputData)
key=[None]*len(InputData)
sums=[]
S=int(input("Enter sum S: "))
ii=0
for i in range(len(InputData)):
    InputData[i]=int(InputData[i])

def GoGrand(i,j):
    global parent
    if j!=0:
        if i==right[parent[i]]:
            i=parent[i]
        else:
            i=parent[i]
            j-=1

        i=GoGrand(i,j)
    return i

for i in range(len(InputData)):
    if InputData[i]!=0:
        key[i]=InputData[i]
        if i<len(InputData)-1:
            if InputData[i+1]!=0:
                left[i]=i+1
                parent[i+1]=i
    else:
        if i<len(InputData)-1:
            if InputData[i+1]!=0:
                j=0
                while InputData[i-1-j]==0:
                    j+=1
                k=GoGrand(i-1-j,j)
                right[k]=i+1
                parent[i+1]=k
                #FindForRight(i, k)



SortTheTree()

#InorderTreePrint()

for i in range(len(key)):
    FindSum(S,[],i)

print(sums)

with open("Outputs/khmelinin_output"+str(inputname[5:-4])+"_"+str(S)+".txt", 'w') as file:
    for i in range(len(sums)):
        for j in range(len(sums[i])):
            file.write(str(sums[i][j])+" ")
        file.write("\n")

print("The End")