import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    start_time = time.time()
    array = random.sample(range(1000, 2000), 50)
    sorted_array = quicksort(array)
    end_time = time.time()
    print("Time taken to sort the array: ", end_time - start_time, " seconds")
    for i in range(len(sorted_array)):
        print(sorted_array[i])
