# The lines `import analyze_algorithm` and `import plotting` are importing Python modules named
# `analyze_algorithm` and `plotting`, which contain the code for time calculation and graphing visualization of time complexities respectively.
import analyze_algorithm
import plotting
def bubbleSort(arr):
    """
    The above function implements the bubble sort algorithm in Python to sort a given array in ascending
    order.
    
    :param arr: The code you provided is an implementation of the Bubble Sort algorithm in Python. This
    algorithm repeatedly steps through the list to be sorted, compares each pair of adjacent items, and
    swaps them if they are in the wrong order. The process is repeated until no more swaps are needed,
    indicating that the list is sorted and the loop breaks
    """
    n = len(arr)
    for i in range(0,n):
        flag = 0
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                flag = 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if flag == 0:
            break

# The line `array_sizes, times = analyze_algorithm.time_of_algorithm(bubbleSort)` is calling a
# function `time_of_algorithm` from the `analyze_algorithm` module. This function is designed
# to measure the time taken by a sorting algorithm (in this case, `bubbleSort` function) to sort
# arrays of different sizes.
array_sizes, times = analyze_algorithm.time_of_algorithm(bubbleSort)

# The line `plotting.createPlot(array_sizes, times, 'Bubble Sort')` is calling a function `createPlot`
# from the `plotting` module. This function is designed to create a plot or graph visualizing
# the relationship between the array sizes and the corresponding times taken by the `bubbleSort`
# algorithm to sort arrays of those sizes.
plotting.createPlot(array_sizes, times, 'Bubble Sort')
