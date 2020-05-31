def InorderTreeWalk(ar, x=0): # записывает дерево в массив
    global key, left, right
    if x!=None:
        InorderTreeWalk(ar, left[x])
        ar.append(key[x])
        InorderTreeWalk(ar, right[x])

def InorderTreeWrite(ar, x=0): # записывает бинарное дерево поиска в прошлое
    global ii
    if x!=None:
        InorderTreeWrite(ar,left[x])
        key[x]=ar[ii]
        ii+=1
        InorderTreeWrite(ar,right[x])

def TreeSort(): # вызывает функцию перевода бинарного дерева в массив, вызывает сортировку для этого массива, и вызывает функцию для записи отсортированого массива в дерево
    array=[]
    InorderTreeWalk(array)
    array.sort() 
    InorderTreeWrite(array)


def SumFind(S,route,id,sum=0): # поиск элементов key которые вместе дают сумму S
    global key,right,left, sums
    if id != None:
        if key[id]!=None:
            sum+=key[id]
            route.append(key[id]) # запись пути элементов в массив
            if sum==S:
                sums.append(route[:])
                return
            if sum >S:
                return
            SumFind(S, route[:], left[id],sum) # идем в левую ветку
            SumFind(S,route[:],right[id],sum) # идем в правую ветку
    

inputname=input("Input file name (10c): ")
with open('Inputs/'+'input_'+inputname+'.txt') as f: #считываем файл
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

def GoGrandParents(i,j): # находит индекс родителя для правого сына
    global parent
    if j!=0:
        if i==right[parent[i]]:
            i=parent[i]
        else:
            i=parent[i]
            j-=1

        i=GoGrandParents(i,j)
    return i

for i in range(len(InputData)): # выставление связей между родителями и ветками
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
                k=GoGrandParents(i-1-j,j)
                right[k]=i+1
                parent[i+1]=k



TreeSort()

for i in range(len(key)):
    SumFind(S,[],i)

print(sums)

with open("Outputs/khmelinin_output_"+str(inputname)+"_"+str(S)+".txt", 'w') as file: # запись в файл
    for i in range(len(sums)):
        for j in range(len(sums[i])):
            file.write(str(sums[i][j])+" ")
        file.write("\n")

print("The End")