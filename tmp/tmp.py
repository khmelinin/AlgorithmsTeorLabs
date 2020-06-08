from collections import namedtuple
import sys
sys.setrecursionlimit(10000)

name = input("File name (without .txt): ")
with open("inputs/"+name + ".txt", 'r') as f:
    max_weight, number = [int(x) for x in f.readline().split()]
    value = []
    weight =[]
    for i in range(number):
        temp = [int(i) for i in f.readline().split()]
        value.append(temp[0])
        weight.append(temp[1])

Item = namedtuple('Item', 'value weight')
items=[]
for i in range(number):
    items.append(Item(value[i],weight[i]))

capacity = max_weight # максимальна вага рюкзака

def best_value(nitems, weight_limit):
    if nitems == 0:  # якщо немає доступних предметів,то найбільша цінність дорівнює нулю
        return 0  # zero value
    elif items[nitems - 1].weight > weight_limit:#якщо вага даного предмета більше дозволеної ваги,то результат дорівнює найбільшій цінності без цього предмата(з залишковими n-1 доступними предметами)
        # new item is heavier than the current weight limit
        return best_value(nitems - 1, weight_limit)  # don't include new item
    else:#в іншому випадку вибираємо максимум із 2-ух варіантів:a) варіант,який виключає даний предмет;б)варіант,який включає даний предмет(найбільша цінність в цьому випадку дорівнює сумі цінності від даного предмета
        # і найбільшій цінності залишкових предметів із дозволеною вагою,зменшеною на вагу даного предмета(тобто в рюкзаку залишилося менше місця) )
        return max(  # max of with and without the new item
            best_value(nitems - 1, weight_limit),  # without
            best_value(nitems - 1, weight_limit - items[nitems - 1].weight)
              + items[nitems - 1].value)  # with the new item

sum=0
result = []
max_value=0
weight_limit = capacity
for i in reversed(range(len(items))):
    if best_value(i + 1, weight_limit) > best_value(i, weight_limit):
        # better with the i-th item
        result.append(items[i])  # include it in the result
        weight_limit -= items[i].weight
print(result)
for i in range(len(result)):
    max_value+=result[i].value
print(max_value)

with open("outputs/output"+name[5:]+".txt", 'w') as fi:
    fi.write(str(max_value))
