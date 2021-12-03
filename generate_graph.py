import random 
from math import sqrt

def shuffle_arr(arr, pivot, control):
    test_before=0
    for i in arr[:pivot+1]:
        if i:
            test_before+=1
    test_after = control-test_before

    temp_arr = [random.randint(5, 150) for i in range(test_after)] + [0 for i in range(len(arr[pivot+1:]) - test_after)]
    random.shuffle(temp_arr)
    final_arr =  arr[:pivot+1] + temp_arr

    return final_arr[:len(arr)]

def generate_arr(size=300, degree = 10):
    arr = [[0] * size for i in range(size)]

    for i in range(0, size):
        n = int(sqrt(random.randint(1, degree*degree)))
        arr[i] = shuffle_arr(arr[i], i, n)
        #print(arr[i])
        for j in range(i+1, size):
            arr[j][i]= arr[i][j]

    return arr

def main():
    generate_arr()

if __name__ == "__main__":
    main()
    
