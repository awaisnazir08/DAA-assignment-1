# The lines `import analyze_algorithm` and `import plotting` are importing Python modules named
# `analyze_algorithm` and `plotting`, which contain the code for time calculation and graphing visualization of time complexities respectively.
import analyze_algorithm
import plotting

def insertionSort(arr):
    """
    The `insertionSort` function implements the insertion sort algorithm to sort an array in ascending
    order.
    
    :param arr: The `insertionSort` function you provided is an implementation of the Insertion Sort
    algorithm in Python. This algorithm works by iteratively building a sorted portion of the array
    while inserting elements from the unsorted portion into their correct positions
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        #move elements of arr[0..i-1] that are greater than key to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        #insert key at the right place
        arr[j + 1] = key



# The line `array_sizes, times = analyze_algorithm.time_of_algorithm(insertionSort)` is calling a
# function named `time_of_algorithm` from the `analyze_algorithm` module. This function is used to
# measure the time taken by the `insertionSort` function to sort arrays of different sizes.
array_sizes, times = analyze_algorithm.time_of_algorithm(insertionSort, 'Insertion Sort')



# The line `plotting.createPlot(array_sizes, times, 'Insertion Sort')` is calling a function named
# `createPlot` from the `plotting` module. This function is used to create a plot or graph to
# visualize the relationship between the array sizes and the corresponding time taken by the
# `insertionSort` function to sort arrays of those sizes. The plot will help in understanding the time
# complexity of the `insertionSort` algorithm and how it performs as the input size increases. The
# title of the plot will be 'Insertion Sort', indicating that it represents the time complexity
# analysis of the insertion sort algorithm.
plotting.createPlot(array_sizes, times, 'Insertion Sort')