import os.path
import random
import time



def quicksort(left, right, arr):
    if len(arr) == 1:  # Condition Terminating for recursion. 
        return arr
    if left < right:
        pt = partition(left, right, arr)
        quicksort(left, pt-1, arr)  # sorting the left values recursively 
        quicksort(pt+1, right, arr)  #  sorting the right values Recursively
    return arr 
 
def partition(l, right, nums):
    # Last element will be the pivot 
    # the first element is the pointer
    pivot = nums[right][2]
    pointer = l
    for i in range(l, right):
        if nums[i][2] <= pivot:
            # values smaller than the pivot getting Swapped to the front
            nums[i], nums[pointer] = nums[pointer], nums[i]
            pointer += 1
    # swapping the last element with the pointer indexed number
    nums[pointer], nums[right] = nums[right], nums[pointer]
    return pointer

def sort_rows(arr):
    for row in arr:
        row.sort()

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
        f.write('Total Time taken to sort using quick sort: {:.6f} seconds'.format(total_time))

for filename in ['arr20.txt', 'arr100.txt', 'arr2000.txt', 'arr6000.txt']:
    arr = read_file(filename)
    start_time = time.time()
    sort_rows(arr)
    quicksort(0, len(arr)-1, arr)
    end_time = time.time()
    total_time = end_time - start_time
    output = 'arrQK_O_' + filename
    write_file(output, arr, total_time)
