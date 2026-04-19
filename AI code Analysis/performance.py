import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5, 2, 9, 1, 5, 6] * 1000

start = time.time()
bubble_sort(arr.copy())
end = time.time()

print("Execution Time:", end - start)