import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid()

def ExtendPoints(array):
    for point in array:
        point.append(1)

    return array


def MultiplyRez(point, weight):
    print("Here", point, weight)
    sum=0
    for i in range(len(point)):
        sum+=point[i]*weight[i]

    print(f"{point} * {weight} = {sum}")

    return sum



def SumRez(point, weight):
    vector=[weight[i]+point[i] for i in range(len(point))]
    print(f"{weight} + {point} = {vector}\n")
    return vector


def SubstrRez(point, weight):
    vector=[weight[i]-point[i] for i in range(len(point))]
    print(f"{weight} - {point} = {vector}\n")
    return vector


def Unite(not_include, arrays):
    union_array=[i for i in arrays if(i!=not_include)]
    return union_array





if(__name__=="__main__"):
    array_of_equations=[]
    number_of_clusters=4

    #     P1      P2
    A1 = [[0, 4]]
    #     P3      P4
    A2 = [[2, 2]]
    #     P1      P2
    A3 = [[4, 4]]
    #     P3      P4
    #A4 = [[-1, 1], [-1, 2]]

    W = [0, 0, 0]

    for i in A1:
        plt.plot(i[0], i[1], marker="o", markersize=5, markeredgecolor="blue", markerfacecolor="blue")

    for i in A2:
        plt.plot(i[0], i[1], marker="o", markersize=5, markeredgecolor="green", markerfacecolor="green")

    for i in A3:
        plt.plot(i[0], i[1], marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")

    #for i in A4:
    #    plt.plot(i[0], i[1], marker="o", markersize=5, markeredgecolor="yellow", markerfacecolor="yellow")

    A1 = ExtendPoints(A1)
    A2 = ExtendPoints(A2)
    A3 = ExtendPoints(A3)
    #A4 = ExtendPoints(A4)

    my_points=[A1, A2, A3]      #Додати всі класи

    for index in my_points:
        W = [0, 0, 0]
        cluster_1=index
        cluster_2=Unite(index, my_points)

        for k in range(100):
            print(f"Iteration {k+1}")
            counter = 0
            for i in cluster_1:
                if(MultiplyRez(i, W)<=0):
                    print("Корегуємо ваговий вектор\n")
                    W=SumRez(i, W)
                    counter+=1
                else:
                    print("Корекція не потрібна\n")

            for pair in cluster_2:
                for i in pair:
                    if(MultiplyRez(i, W)>=0):
                        print("Корегуємо ваговий вектор\n")
                        W=SubstrRez(i, W)
                        counter+=1
                    else:
                        print("Корекція не потрібна\n")


            if(counter==0):
                break

            print("____________________\n\n\n")
        array_of_equations.append(W)


    #___________________________________________________________________#Вивід графіка

    for i in array_of_equations:
        W=i
        x = np.linspace(-10, 10, 100)
        y=None
        if(W[1]!=0):
            y = ( (W[2]+(W[0]*x))/(-W[1]) )
        else:
            y=[(-W[2]/W[0]) for i in range(100)]
            x, y = y, x
        plt.plot(x, y, 'r')

    plt.show()



















