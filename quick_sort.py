# The lines `import analyze_algorithm` and `import plotting` are importing Python modules named
# `analyze_algorithm` and `plotting`, which contain the code for time calculation and graphing visualization of time complexities respectively.
import analyze_algorithm
import plotting


def medianOfThree(arr, low, high):
    """
    The function `medianOfThree` calculates the median of three elements in an array and rearranges the
    elements in ascending order.
    
    :param arr: The `arr` parameter in the `medianOfThree` function represents the list of elements for
    which you want to find the median of the three values at indices `low`, `mid`, and `high`
    :param low: The `low` parameter in the `medianOfThree` function represents the index of the first
    element in the array segment that you want to find the median of. It is the starting index of the
    subarray
    :param high: High is the index of the last element in the array
    :return: The function `medianOfThree` is finding the median value among the elements at indices
    `low`, `mid`, and `high` in the input array `arr`.
    It is swapping the median value with the first (left) element in the array and then returning it!
    """
    mid = low + (high - low) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]

    arr[mid], arr[low] = arr[low], arr[mid]
    return arr[low]


def partition(arr, left, right):
    """
    The function `partition` takes an array `arr`, a left index `left`, and a right index `right`, and
    partitions the array based on a pivot chosen using the median of three method.
    
    :param arr: It seems like the code snippet you provided is a partition function for quicksort
    algorithm. The `partition` function takes an array `arr`, a left index `left`, and a right index
    `right` as parameters. The function chooses a pivot element using the `medianOfThree` function and
    then
    :param left: The `left` parameter in the `partition` function represents the index of the leftmost
    element in the array `arr` that you want to partition. It is used as a reference point for the
    partitioning process within the specified range
    :param right: The `right` parameter in the `partition` function represents the index of the
    rightmost element in the subarray being partitioned. It helps in determining the range of elements
    within which the partitioning operation will take place
    :return: The `partition` function is returning the index of the pivot element after rearranging the
    elements in the array such that all elements less than or equal to the pivot are on the left side,
    and all elements greater than the pivot are on the right side.
    """
    pivot = medianOfThree(arr, left, right)
    lb = left
    while left < right:
        while arr[left] <= pivot:
            left += 1

        while arr[right] > pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    
    arr[lb], arr[right] = arr[right], arr[lb]
    return right



def quickSort(arr, left, right):
    """
    The above function is an implementation of the quicksort algorithm in Python.
    
    :param arr: The `arr` parameter in the `quickSort` function represents the array that you want to
    sort using the quicksort algorithm. It contains the elements that need to be sorted
    :param left: The `left` parameter in the `quickSort` function represents the index of the leftmost
    element of the subarray being sorted. It is used to keep track of the starting point of the subarray
    within the overall array that is being sorted
    :param right: The `right` parameter in the `quickSort` function represents the index of the
    rightmost element in the subarray that is being sorted. It helps in determining the range of
    elements that need to be sorted within the array
    """
    if left < right:
        location = partition(arr, left, right)
        quickSort(arr, left, location - 1)
        quickSort(arr, location + 1, right)
        



# The line `array_sizes, times = analyze_algorithm.time_of_algorithm(quickSort, 'Quick Sort')` is
# calling a function named `time_of_algorithm` from the `analyze_algorithm` module. This function is
# designed to measure the execution time of the `quickSort` function for different array sizes.
array_sizes, times = analyze_algorithm.time_of_algorithm(quickSort, 'Quick Sort')


# The line `plotting.createPlot(array_sizes, times, 'Quick Sort')` is calling a function named
# `createPlot` from the `plotting` module. This function is designed to create a plot or graph
# to visualize the relationship between the array sizes and the corresponding times taken to execute
# the Quick Sort algorithm.
plotting.createPlot(array_sizes, times, 'Quick Sort')