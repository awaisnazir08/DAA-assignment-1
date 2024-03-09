# The lines `import analyze_algorithm` and `import plotting` are importing Python modules named
# `analyze_algorithm` and `plotting`, which contain the code for time calculation and graphing visualization of time complexities respectively.
import analyze_algorithm
import plotting

# find the maximum in the array
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# using count sort to sort the elements 
def counting_sort(arr, pos):
    size = len(arr)
    # creating a count array of size 10 because digits can only be from 0-9
    count = [0] * 10
    for i in range(size):
        #sorting the elements, placing them in the count array based on the digit number (starting from the least significant and moving towards left)
        count[(arr[i] // pos) % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    result = [0] * size
    i = size - 1
    while i >= 0:
        
        #placing the digit at its right place based on the digit being used for sorting
        result[count[(arr[i] // pos) % 10] - 1] = arr[i]
        count[(arr[i] // pos) % 10] -= 1
        i -= 1

    for i in range(size):
        arr[i] = result[i]

# radix sort calling function
def radixSort(arr):
    max_val = find_max(arr)
    pos = 1

    # the radix sort sorts values based on integer digits, so for the maximum number of digits, radix sort uses count sort to sort the elements in the array
    while max_val // pos > 0:
        counting_sort(arr, pos)
        pos *= 10


array_sizes, times = analyze_algorithm.time_of_algorithm(radixSort, 'Radix Sort')

plotting.createPlot(array_sizes, times, 'Radix Sort')
