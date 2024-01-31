import time

#merge sort algorithm
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i][-1] < right[j][-1]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

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
        f.write('Total Time taken to sort using merge sort: {:.6f} seconds'.format(total_time))

for filename in ['arr20.txt', 'arr100.txt', 'arr2000.txt', 'arr6000.txt']:
    arr = read_file(filename)
    start_time = time.time()
    sort_rows(arr)
    merge_sort(arr)
    end_time = time.time()
    total_time = end_time - start_time
    output = 'arrMR_O_' + filename
    write_file(output, arr, total_time)
