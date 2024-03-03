import random
import time
def time_of_algorithm(algorithm, name=''):
    """
    The function `time_of_algorithm` measures the execution time of a given algorithm on arrays of
    increasing sizes and returns the array sizes and corresponding execution times.
    
    :param algorithm: The `algorithm` parameter in the `time_of_algorithm` function is expected to be a
    function that sorts a given array. The function will measure the execution time of this algorithm
    for different array sizes
    :param name: The `name` parameter in the `time_of_algorithm` function is a string that specifies the
    name of the algorithm being tested. It is used to determine which sorting algorithm to apply to the
    array
    :return: The function `time_of_algorithm` returns two lists: `arrays` and `times`. The `arrays` list
    contains a range of array sizes, while the `times` list contains the execution times of the
    algorithm for each corresponding array size.
    """
    arrays = list(range(10, 10011, 1000))
    times = []
    for i in arrays:
        arr = [random.randint(0, 1000000) for _ in range(i)]
        print(f'First 10 elements of Unsorted array of size {i}: {arr[:10]}')
        start_timer = time.time()
        if name in ['Quick Sort', 'Merge Sort']:
            algorithm(arr, 0, len(arr)-1)
        else:
            algorithm(arr)
        end_timer = time.time()
        execution_time = end_timer - start_timer
        times.append(execution_time)
        print(f'First 10 elements of Sorted array of size {i} using {name}: {arr[:10]}')
    return arrays, times