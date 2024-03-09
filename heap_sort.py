# The lines `import analyze_algorithm` and `import plotting` are importing Python modules named
# `analyze_algorithm` and `plotting`, which contain the code for time calculation and graphing visualization of time complexities respectively.
import analyze_algorithm
import plotting

def heapify(arr, n, i):
    """
    The function `heapify` takes an array, its size, and an index, and adjusts the elements to maintain
    the max heap property.
    
    :param arr: The `arr` parameter is the input array that represents the binary heap. It is a list of
    elements where the heap property is to be maintained or restored
    :param n: The parameter `n` in the `heapify` function represents the size of the heap or the number
    of elements in the array `arr` that you want to heapify. It is used to determine the boundaries
    within which the heapify operation should be performed on the elements of the array
    :param i: In the `heapify` function, the parameter `i` represents the index of the current node in
    the heap. The function is used to maintain the heap property in a binary tree represented as an
    array. The `heapify` function compares the node at index `i` with its left and
    """
# The code snippet you provided is implementing the `heapify` function in Python. This function is a
# crucial part of the heap sort algorithm. Here's a breakdown of what each part of the code is doing:
# if the parent is smaller than any of its childs, then swap the parent with the child, keep doing this
# until the heap property is achieved!
    largest = i
    while True:
        left_child = 2 * i 
        right_child = 2 * i + 1
        if left_child < n and arr[left_child] > arr[largest]:
            largest = left_child

        if right_child < n and arr[right_child] > arr[largest]:
            largest = right_child

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest
        else:
            break


    """
    The `heap_sort` function in Python implements the heap sort algorithm to sort a given array in
    ascending order.
    
    :param arr: The `arr` parameter in the `heap_sort` function is the input list that you want to sort
    using the Heap Sort algorithm. It contains the elements that need to be sorted in ascending or
    descending order
    """
def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    # calling the heapify function for only n to (n/2) elements which are the non-leaf nodes, 
    # after this, for the leaf nodes, the heapify 
    # propery will automatically be achieved!
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one, and swap them with the last element
    # since the heap property would be disturbed, the heapify function is called again and again
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


# The line `array_sizes, times = analyze_algorithm.time_of_algorithm(heap_sort, 'Heap Sort')` is
# calling a function named `time_of_algorithm` from the `analyze_algorithm` module. This function is
# used to measure the time taken by the `heap_sort` function to sort arrays of different sizes.
array_sizes, times = analyze_algorithm.time_of_algorithm(heap_sort, 'Heap Sort')


# The line `plotting.createPlot(array_sizes, times, 'Heap Sort')` is calling a function named
# `createPlot` from the `plotting` module. This function is used to create a plot or graph to
# visualize the relationship between the array sizes and the corresponding time taken by the
# `heap_sort` algorithm to sort arrays of different sizes. The plot will help in understanding the
# time complexity of the `heap_sort` algorithm and how it scales with different input sizes.
plotting.createPlot(array_sizes, times, 'Heap Sort')
