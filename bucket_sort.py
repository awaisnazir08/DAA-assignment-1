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

    """
    The `bucketSort` function implements the bucket sort algorithm to sort an input array of elements.
    
    :param arr: It looks like the code you provided is an implementation of the Bucket Sort algorithm in
    Python. The function `bucketSort` takes a list `arr` as input and sorts it using the Bucket Sort
    algorithm
    :return: The `bucketSort` function is returning a sorted list of elements after applying the bucket
    sort algorithm.
    """
def bucketSort(arr):
    n = len(arr)
    buckets = []

    # creating an empty bucket
    for _ in range(n):
        buckets.append([])

    # inserting elements in the buckets
    for i in range(n):
        buckets[int(n * arr[i])].append(arr[i])

    #sorting every bucket using insertion sort
    for i in range(n):
        insertionSort(buckets[i])

    # concatenating the sorted buckets together
    result = []
    for i in range(n):
        result.extend(buckets[i])

    #replacting the original array with the sorted result's array
    for i in range(len(arr)):
        arr[i] = result[i]


array_sizes, times = analyze_algorithm.time_of_algorithm(bucketSort, 'Bucket Sort')

plotting.createPlot(array_sizes, times, 'Bucket Sort')

# Example Usage
# arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]

# print("Original Array:")
# print(arr)

# # Perform Bucket Sort
# sorted_array = bucketSort(arr)

# print("Sorted Array using Bucket Sort:")
# print(sorted_array)
