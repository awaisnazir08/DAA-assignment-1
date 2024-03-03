# The lines `import analyze_algorithm` and `import plotting` are importing Python modules named
# `analyze_algorithm` and `plotting`, which contain the code for time calculation and graphing visualization of time complexities respectively.
import analyze_algorithm
import plotting

def selectionSort(arr):
    """
    The `selectionSort` function implements the selection sort algorithm to sort a given array in
    ascending order.
    
    :param arr: The `selectionSort` function you provided is an implementation of the Selection Sort
    algorithm in Python. This algorithm works by repeatedly finding the minimum element from the
    unsorted part of the array and swapping it with the first unsorted element
    """
    n = len(arr)
    for i in range(0, n):
        min_element_index = i
        for j in range(i+1, n):
            if arr[min_element_index] > arr[j]:
                #if a new index is obtained that contains an element smaller than the initial minimum index element assumed, then reset the new minimum index
                min_element_index = j

        arr[i], arr[min_element_index] = arr[min_element_index], arr[i]


# The line `array_sizes, times = analyze_algorithm.time_of_algorithm(selectionSort)` is calling a
# function named `time_of_algorithm` from the `analyze_algorithm` module. This function is
# designed to measure the time taken to execute the `selectionSort` function for different array
# sizes.
array_sizes, times = analyze_algorithm.time_of_algorithm(selectionSort, 'Selection Sort')


# The line `plotting.createPlot(array_sizes, times, 'Selection Sort')` is calling a function named
# `createPlot` from the `plotting` module. This function is used to create a plot or graph to
# visualize the relationship between the array sizes and the corresponding execution times obtained
# from running the `selectionSort` algorithm. The plot will help in understanding how the time
# complexity of the algorithm scales with different input sizes, in this case, for the Selection Sort
# algorithm. The title of the plot will be 'Selection Sort', indicating the algorithm being analyzed.
plotting.createPlot(array_sizes, times, 'Selection Sort')