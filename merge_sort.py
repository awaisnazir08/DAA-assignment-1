# The lines `import analyze_algorithm` and `import plotting` are importing Python modules named
# `analyze_algorithm` and `plotting`, which contain the code for time calculation and graphing visualization of time complexities respectively.
import analyze_algorithm
import plotting


def merge(array, left, middle, right):
    """
    The function `merge` merges two subarrays within a given array in ascending order.
    
    :param a: The parameter `a` is a list that contains the elements to be merged. The function `merge`
    takes this list `a` along with the indices `left`, `middle`, and `right` as input parameters. The
    function merges the two subarrays of `a` from indices `left
    :param left: The `left` parameter in the `merge` function represents the starting index of the
    subarray within the array `a` that needs to be merged. It indicates the left boundary of the
    subarray
    :param middle: The `middle` parameter in the `merge` function represents the index that divides the
    array `a` into two subarrays for merging. It indicates the boundary between the left and right
    subarrays that need to be merged
    :param right: The `right` parameter in the `merge` function represents the index of the rightmost
    element in the subarray being merged. It indicates the end point of the subarray within the main
    array that needs to be merged
    """

    '''
    The code snippet you provided is the implementation of the merge step in the merge sort algorithm.
    Here's a breakdown of what each part of the code is doing:
    First, we create 2 subarrays for the left and right part
    then we iterate through both the arrays and put the elements back in the original array in the sorted order
    afterwards, if there are still elements remaining in the sub arrays, we put them back in the original array
    '''
    # making two arrays 
    a1 = array[left : middle + 1]
    a2 = array[middle + 1 : right + 1]

    n1 = len(a1)
    n2 = len(a2)
    i = j = 0
    k = left
    
    #inserting elements from the new created two arrays into the original array in ascending order
    while i < n1 and j < n2:
        if a1[i] < a2[j]:
            array[k] = a1[i]
            i += 1
        else:
            array[k] = a2[j]
            j += 1
        k += 1

    #if elements still left in either array, insert them into the original array
    while i < n1:
        array[k] = a1[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = a2[j]
        j += 1
        k += 1

def mergeSort(a, left, right):
    """
    The function `merge_sort` implements the merge sort algorithm to sort a list `a` within the
    specified range `[left, right]`.
    
    :param a: The parameter `a` in the `merge_sort` function represents the list or array that you want
    to sort using the merge sort algorithm
    :param left: The `left` parameter in the `merge_sort` function represents the index of the leftmost
    element in the subarray that is currently being sorted. It helps in dividing the array into smaller
    subarrays for sorting in the merge sort algorithm
    :param right: The `right` parameter in the `merge_sort` function represents the index of the
    rightmost element in the subarray that is being sorted. It helps in determining the boundaries of
    the subarray that needs to be sorted during each recursive call of the merge sort algorithm
    """
    '''
    the code below is recursively calling the merge_sort function on the left and right arrays, and then calling the 
    merge function to merge back the arrays
    this goes on and on until the the arrays are so much divided that they cannot further be divided; that is when left becomes 
    equal or greater than right..!!
    '''
    if left < right:
        middle = (left + right) // 2
        mergeSort(a, left, middle)
        mergeSort(a, middle + 1, right)
        merge(a, left, middle, right)



# The line `array_sizes, times = analyze_algorithm.time_of_algorithm(mergeSort, 'Merge Sort')` is
# calling a function named `time_of_algorithm` from the `analyze_algorithm` module.
array_sizes, times = analyze_algorithm.time_of_algorithm(mergeSort, 'Merge Sort')


# The line `plotting.createPlot(array_sizes, times, 'Merge Sort')` is calling a function named
# `createPlot` from the `plotting` module. This function is used to create a plot or graph to
# visualize the relationship between the array sizes and the corresponding time taken to execute the
# 'Merge Sort' algorithm.
plotting.createPlot(array_sizes, times, 'Merge Sort')
