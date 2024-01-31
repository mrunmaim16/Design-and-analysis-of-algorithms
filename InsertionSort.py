import os.path
import random
import time
#create array
def create_array():
    for n in [20, 100, 2000, 6000]:
        filename = f"arr{n}.txt"
        if not os.path.isfile(filename):
            arrays = [[random.randint(0, 99) for _ in range(3)] for _ in range(n)]
            with open(filename, "w") as f:
                for arr in arrays:
                    f.write(" ".join(str(x) for x in arr))
                    f.write("\n")

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def sort_rows(arr):
    for row in arr:
        insertion_sort(row)

def sort_column(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key[-1] < arr[j][-1]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def read_file(filename):
    arr = []
    with open(filename, 'r') as f:
        for line in f:
            arr.append([int(x) for x in line.split()])
    return arr

def write_file(filename, arr, total_time):
    with open(filename, 'w') as f:
        for row in arr:
            f.write(' '.join(str(x) for x in row) + '\n')
        f.write('Total Time taken to sort using insertion sort: {:.6f} seconds'.format(total_time))

for filename in ['arr20.txt', 'arr100.txt', 'arr2000.txt', 'arr6000.txt']:
    create_array()
    arr = read_file(filename)
    start_time = time.time()
    sort_rows(arr)
    sort_column(arr)
    end_time = time.time()
    total_time = end_time - start_time
    output = 'arrIS_O_' + filename
    write_file(output, arr, total_time)
