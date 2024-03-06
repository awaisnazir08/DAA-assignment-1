# The lines `import analyze_algorithm` and `import plotting` are importing Python modules named
# `analyze_algorithm` and `plotting`, which contain the code for time calculation and graphing visualization of time complexities respectively.
import analyze_algorithm
import plotting

def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

def counting_sort(arr, pos):
    size = len(arr)
    count = [0] * 10
    for i in range(size):
        count[(arr[i] // pos) % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    result = [0] * size
    i = size - 1
    while i >= 0:
        result[count[(arr[i] // pos) % 10] - 1] = arr[i]
        count[(arr[i] // pos) % 10] -= 1
        i -= 1

    for i in range(size):
        arr[i] = result[i]

def radixSort(arr):
    max_val = find_max(arr)
    pos = 1

    while max_val // pos > 0:
        counting_sort(arr, pos)
        pos *= 10


array_sizes, times = analyze_algorithm.time_of_algorithm(radixSort, 'Radix Sort')

plotting.createPlot(array_sizes, times, 'Radix Sort')
# # Example usage:
# arr = [4, 6, 7, 2, 8, 0, 1, 421, 4, 2, 0, 9, 2, 7, 2]
# print("Original array:", arr)

# radix_sort(arr)

# print("Sorted array:", arr)
