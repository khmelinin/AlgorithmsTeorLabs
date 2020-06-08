name_num = "100" #-------------------------------- input / output name number ------------------------------------------

def main():
    def Knapsack(weight, price, MaxWeight, number):
        final = [0] * (MaxWeight+1)
        for i in range(number):
            for j in range(MaxWeight,weight[i]-1, -1):
                next_v=price[i] + final[j-weight[i]]
                if next_v>final[j]:
                    final[j]=next_v
        return final[MaxWeight]


    with open("Inputs/input_"+name_num+".txt", 'r') as f: # Input -----------------------------------------------------
        MaxWeight, number = [int(x) for x in f.readline().split()]
        value = []
        weight =[]
        for i in range(number):
            temp = [int(i) for i in f.readline().split()]
            value.append(temp[0])
            weight.append(temp[1])

    T=[[-1 for i in range(MaxWeight+1)] for j in range(number+1)]

    asd = Knapsack(weight, value, MaxWeight, number)

    with open("Outputs/khmelinin_output_"+name_num+".txt", 'w') as fi: # Output ---------------------------------------
        fi.write(str(asd))

if __name__ == '__main__':
    main()