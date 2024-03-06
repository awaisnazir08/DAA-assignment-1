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

def countingSort(arr):
    max_val = find_max(arr)
    frequency = [0] * (max_val + 1)

    #calulating the frequency
    for num in arr:
        frequency[num] += 1


    #calculating the cumulative frequency
    for i in range(1, len(frequency)):
        frequency[i] += frequency[i - 1]

    result = [0] * len(arr)
    i = len(arr) - 1
    while i >=0:
        result[frequency[arr[i]]-1] = arr[i]
        frequency[arr[i]] -= 1
        i -= 1
    for i in range(len(arr)):
        arr[i] = result[i]


array_sizes, times = analyze_algorithm.time_of_algorithm(countingSort, 'Counting Sort')


plotting.createPlot(array_sizes, times, 'Counting Sort')
# # Example usage:
# arr = [5, 1, 2, 4, 2, 7, 5, 2, 9, 7]
# countingSort(arr)
# print(arr)
