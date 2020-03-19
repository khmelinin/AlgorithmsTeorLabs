def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot
    count=0
    for j in range(low, high):
        ######################################################################################
        count+=2
        if arr[j] <= pivot:
            #count += 1
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    #print("count",count)
    return (i + 1),count

def quickSort(arr, low, high):
    if low < high:
        pi,count = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
        return count

count = 0
f = open('input_01_10.txt','r')
l = [line.strip() for line in f]
intl =[]
for i in l:
    intl.append(int(i))
#amount = intl.pop(0)
#print(amount)
print(intl);


s = quickSort(intl, 0, len(intl)-1)

print(intl)
print(s)

f = open('Aoutput_01_10.txt','w')
f.write(str(s) + '\n')

