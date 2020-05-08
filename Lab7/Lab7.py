import math

def Hash_divide(hashTableLen, k): # метод деления
    return k % hashTableLen

def Hash_multiply(hashTableLen, k): # метод умножения
    return int(hashTableLen * ((k * ((math.sqrt(5) - 1) / 2)) % 1))


def Hash_searchD(HashTable, k):   # поиск методом деления
    for i in range(len(HashTable)):
        j = Hash_divide(len(HashTable), k)
        if HashTable[j][i] == 0:
            return 0
        elif HashTable[j][i] == k:
            return j

def Hash_searchM(HashTable, k):   # поиск методом умножения
    for i in range(len(HashTable)):
        j = Hash_multiply(len(HashTable), k)
        if HashTable[j][i] == 0:
            return 0
        elif HashTable[j][i] == k:
            return j

with open("Inputs/input_100000.txt") as f: # считывание файла
    data = f.read().split()

N = int(data[0]) # количество чисел
M = int(data[1]) # количество сумм
A = [] # массив чисел
S = [] # массив сумм
HashTableD = [] # хеш таблица для divide method
HashTableM = [] # хеш таблица для multiply method
colisionsD = 0 # коллизии
colisionsM = 0 # коллизии

for i in range(2, len(data) - M): # заполнение массива чисел
    A.append(int(data[i]))

for j in range(2 + N, len(data)): # заполнение массива сумм
    S.append(int(data[j]))

for l in range(N*3): # заполнение хеш таблицы нулями
    HashTableD.append([0])

for l in range(N*3): # заполнение хеш таблицы нулями
    HashTableM.append([0])


for q1 in range(len(A)): 
     HashTableD[Hash_divide(N*3, A[q1])].insert(-1, A[q1])
     if len(HashTableD[Hash_divide(N*3, A[q1])]) > 2: # проверка на коллизию
        colisionsD += 1
           
           

for q2 in range(len(A)):
    HashTableM[Hash_multiply(N*3, A[q2])].insert(-1, A[q2])
    if len(HashTableM[Hash_multiply(N*3, A[q2])]) > 2: # проверка на коллизию
        colisionsM += 1

### D ###
with open("Outputs/khmelinin_output_100000_01.txt", 'w') as file: # запись в файл
    file.write(str(colisionsD) + "\n")
    for kk in range(len(S)):
        for h in range(len(A)):
            if Hash_searchD(HashTableD, S[kk] - A[h]) != 0: # алгоритм поиска элемента в хеш таблице
                for u in range(30):
                    if S[kk] - A[h] == HashTableD[Hash_searchD(HashTableD, S[kk] - A[h])][u]: # если есть элемент сумма - элемент A[h],
                        file.write(str(A[h]) + " " + str(HashTableD[Hash_searchD(HashTableD, S[kk] - A[h])][u]) + "\n") # то записываем элемент A[h] и его ключ
                        break
                break
            elif h == len(A)-1:
                file.write("0 0" + "\n")

### M ###
with open("Outputs/khmelinin_output_100000_02.txt", 'w') as file: # запись в файл
    file.write(str(colisionsM) + "\n")
    for kk in range(len(S)):
        for h in range(len(A)):
            if Hash_searchM(HashTableM, S[kk] - A[h]) != 0: # алгоритм поиска элемента в хеш таблице
                for u in range(30):
                    if S[kk] - A[h] == HashTableM[Hash_searchM(HashTableM, S[kk] - A[h])][u]: # если есть элемент сумма - элемент A[h],
                        file.write(str(A[h]) + " " + str(HashTableM[Hash_searchM(HashTableM, S[kk] - A[h])][u]) + "\n") # то записываем элемент A[h] и его ключ
                        break
                break
            elif h == len(A)-1:
                file.write("0 0" + "\n")