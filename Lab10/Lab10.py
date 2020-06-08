def main():
    name_num = "5" #-------------------------------- input / output name number ------------------------------------------

    def Knapsack(weight, price, MaxWeight, number):
        final = [0] * (MaxWeight+1) # создаем масив для хранения стоимости предметов в рюкзаке
        for i in range(number): # цикл, который итерируеться по всем предметам
            for j in range(MaxWeight,weight[i]-1, -1): # цикл, который итерируеться из обьема рюкзака по весу i-того предмета
                next_v=price[i] + final[j-weight[i]] # записываем в final[j] наибольшую стоимость при условии, что расмотренны только первые "i" предметов и общий размер предметов не превышает MaxWeight
                if next_v>final[j]:
                    final[j]=next_v # если новая стоимость больше чем предыдущая, записываем ее в массив
        return final[MaxWeight] # возвращаем максимально возможную стоимость предметов в рюкзаке


    with open("Inputs/input_"+name_num+".txt", 'r') as f: # Input -----------------------------------------------------
        MaxWeight, number = [int(x) for x in f.readline().split()]
        value = []
        weight =[]
        for i in range(number):
            temp = [int(i) for i in f.readline().split()]
            value.append(temp[0])
            weight.append(temp[1])

    

    asd = Knapsack(weight, value, MaxWeight, number)

    with open("Outputs/khmelinin_output_"+name_num+".txt", 'w') as fi: # Output ---------------------------------------
        fi.write(str(asd))

if __name__ == '__main__':
    main()