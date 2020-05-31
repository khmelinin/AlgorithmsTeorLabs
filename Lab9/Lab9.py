import math
def equation(x, y):
    return math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)

def solution(points):
    list = [points[0]]
    size = 0
    first = points.pop(0)
    while len(points)!=0:
        min_len = equation(list[-1], points[0])
        j = 0
        for i in range(len(points)):
            tmp = equation(list[-1], points[i])
            if tmp<min_len:
                min_len=tmp
                j=i
        size+=min_len
        points[0],points[j]=points[j],points[0]
        list.append(points.pop(0))
    size+=equation(list[-1],first)
    list.append(first)
    return [i[2] for i in list], size

#name = input("enter file name: ")
f_in=open("Inputs\input_01"+".txt","r")
#f_in.readline()
points = [[int(j) for j in i.split()] for i in f_in.readlines()]
for i in range(len(points)):
    points[i].append(i)
f_out = open("khmelinin_output_01"+".txt","w")
list, size = solution(points)
f_out.write(str(int(size))+'\n'+str(list))