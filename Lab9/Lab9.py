import math as m

# длинна между точками
def func(a, b):
    return m.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def greedy(coordinates):
    # массив точек
    way = [coordinates[0]]
    # длинна пути
    size = 0
    first = coordinates.pop(0)
    # проход по всем точкам
    while len(coordinates) != 0:
        # временная переменная для сохранения минимальной длинны
        min_len = func(way[-1], coordinates[0])
        j = 0
        # нахождение минимальной длинны
        for i in range(len(coordinates)):
            # создать переменную, чтобы временно хранить длину пути между двумя вершинами
            tmp = func(way[-1],coordinates[i])
            if tmp < min_len:
                min_len = tmp
                j = i
        # увеличение пройденного пути
        size += min_len
        # обмен текущего и первого элементов
        coordinates[0], coordinates[j] = coordinates[j], coordinates[0]
        way.append(coordinates.pop(0))
    # увеличение пройденного пути между первым и вторым
    size += func(way[-1], first)
    # добавление первой вершины
    way.append(first)
    return [i[2] for i in way], size

def main(): 
    # чтение из файла
    file = open("Inputs\input_08.txt", 'r')
    file.readline()
    points = [[int(j) for j in i.split()] for i in file.readlines()]
    for i in range(len(points)):
        points[i].append(i)
    file.close()

    # запись в файл
    file = open("Outputs\khmelinin_output_08.txt", 'w')
    way, size = greedy(points)
    file.write(str(size) + '\n')
    file.writelines(str(way) + '\n')

if __name__ == '__main__':
    main()
