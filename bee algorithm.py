from generate_graph import generate_arr
from plot_graphs import plot
from matplotlib import pyplot as plt

import random
import sys



def generate_points(size = 300):
    point_1 = random.randint(0,size-1)
    point_2 = random.randint(0,size-1)
    while point_2 == point_1:
        point_2 = random.randint(0,size-1)
    
    return point_1, point_2

def fill_point(graph, start_point, curr_nectar):
    for i in range(len(graph[start_point])):
        if graph[start_point][i]:
            if curr_nectar[i] > graph[start_point][i]+curr_nectar[start_point]:
                curr_nectar[i] = graph[start_point][i]+curr_nectar[start_point]
                curr_nectar = fill_point(graph, i, curr_nectar)

    return curr_nectar

def fill_nectar(graph, start_point):
    start_nectar = [10000]*(len(graph[start_point]))
    start_nectar[start_point] = 0

    start_nectar = fill_point(graph, start_point, start_nectar)
    """ for i in range(300):
        if graph[start_point][i]:
            print(graph[start_point][i], start_nectar[i])
    """
    return start_nectar 

def send_scout(start_point, nectar, checked_points, graph):
    for i in range(len(graph[start_point])):
        if (graph[start_point][i]!=0) and ((graph[start_point][i]) not in [j[0] for j in checked_points]):
            if nectar[i] == 0:
                print("1!!!")
            checked_points.append((i, nectar[i]))
            checked_points.sort(key = lambda x: (x[1], x[0]))
            return i, checked_points

    i = random.randint(0, len(graph[start_point])-1)
    while graph[start_point][i] ==0:
        i=random.randint(0, len(graph[start_point])-1)
    if nectar[i] == 0:
        print("1!!!")
    return i, checked_points


def send_foragers(start_point, nectar, checked_points, graph, m):
    new_arr=[]
    for i in range(len(graph[start_point])):
        if graph[start_point][i] and ((graph[start_point][i]) not in [j[0] for j in checked_points]) and m>0:
            m-=1
            checked_points.append((i, nectar[i]))
            new_arr.append(i)
            if nectar[i] == 0:
                print("1!!!")
            

    checked_points.sort(key = lambda x: (x[1], x[0]))
    return m, checked_points, new_arr

def bee(nectar, start, final, graph):
    per_cent_of_scouts_bee = 0.1
    swarm_numbe=0
    for swarm_numbe in range(1, 5):
        results = [[]]
        number_of_cycles = 0

        colony_1 = 10 * swarm_numbe
        colony_1_finish = False
        check_1 = [(start, nectar[start])]
        colony_1_min = nectar[start]
        colony= []
        scouts_points_1 = [start] * round(colony_1*per_cent_of_scouts_bee)

        
        #plot(graph, [start], [final], [], [])
        scouts=[]
        foragers=[]
        #while not colony_1_finish or not colony_2_finish or not colony_3_finish or not colony_4_finish:
        while not colony_1_finish:

            if not colony_1_finish:
                for i in range(round(colony_1*per_cent_of_scouts_bee)):
                    scouts_points_1[i], check_1 = send_scout(scouts_points_1[i], nectar, check_1, graph)
                    
                    if check_1[0][0] == final:
                        colony_1_finish = True
                        break
                scouts+=(scouts_points_1)
                if number_of_cycles % 2 == 1:
                    m_1 = round(colony_1 * (1-per_cent_of_scouts_bee))
                    while m_1>0:
                        m_1, check_1, foragers = send_foragers(check_1[0][0], nectar, check_1, graph, m_1)
                        if check_1[0][0] == final :
                            colony_1_finish = True
                            break
                        #foragers.append(foragers1)
                        #print(len(foragers))
                
                colony.append(check_1[0][1])
            plot(graph, [start], [final], scouts, foragers)         
            number_of_cycles+=1
        #results[swarm_numbe].append(colony)
    #plot(graph, [start], [final], scouts, foragers)
        print(number_of_cycles)   
        plt.plot(colony, label=(swarm_numbe*10))  
    plt.grid()
    plt.show()

def main():
    sys.setrecursionlimit(300)

    a = generate_arr()
    start, finish = generate_points()
    arr = fill_nectar(a, finish)
    bee(arr, start, finish, a)

if __name__ == "__main__":
    main()
    