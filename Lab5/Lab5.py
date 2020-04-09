import random as r

def counting_sort(A, k, ind):
    B = [0]*len(A)
    C = [0]*k                           #Створюємо масив С розмірністю k
    for j in range(len(A)):
        C[int_indexator(A[j],ind)] = C[int_indexator(A[j],ind)] + 1    #в C[i] зберігається кількість елементів, які дорівнюють i
    for i in range(1, k):
        C[i] = C[i] + C[i-1]            #в C[i] зберігається кількість елементів, які не більші за i 
    for j in range(len(A)-1, -1, -1):
        B[C[int_indexator(A[j],ind)]-1] = A[j]
        C[int_indexator(A[j],ind)] = C[int_indexator(A[j],ind)] - 1
    print(B)
    return B

def int_indexator(num1,ind):
    return int(str(num1)[ind])    #iндексатор для int (повертає певну цифру певного числа)

def radix_sort(A, d, k):
    for i in range(d-1, -1, -1):
        A=counting_sort(A, k, i)[:]  #Стійке сортування масиву A за i-м розрядом

def num_create(k1,d1):
    num=r.randint(1,k1-1)
    for i in range(d1-1):            # створення d-значного чисела, в якому кожна цифра приймає одне з k можливих значень
        num=num*10+r.randint(0,k1-1)
    return num


Arr = []
k = 10
d = 4
n = 15

for i in range(n):
    Arr.append(num_create(k,d))

print(Arr)
radix_sort(Arr,d,k)