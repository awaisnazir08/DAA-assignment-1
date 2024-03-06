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
    
    
    # The line `arrays = list(range(10, 10011, 1000))` is creating a list of array sizes that will be used
    # to test the algorithm's execution time.
    arrays = list(range(10, 10011, 1000))
    
    # The line `times = []` is initializing an empty list named `times`. This list will be used to store
    # the execution times of the algorithm for different array sizes. Each time the algorithm is run on an
    # array of a specific size, the execution time will be calculated and appended to this list.
    times = []
    
    for i in arrays:
        # The code snippet you provided is a conditional statement that determines how the input array `arr`
        # is generated based on the value of the `name` parameter passed to the `time_of_algorithm` function.
        if name == 'Bucket Sort':
            arr = [random.uniform(0, 1) for _ in range(i)]
        else:
            arr = [random.randint(0, 1000000) for _ in range(i)]

        print(f'First 10 elements of Unsorted array of size {i}: {arr[:10]}')

        # The line `start_timer = time.time()` is capturing the current time before the execution of the
        # algorithm starts. This is done to measure the starting point of the algorithm's execution. Later,
        # after the algorithm has finished running, the end time will be captured, and the difference between
        # the end time and the start time will give us the total execution time of the algorithm.
        start_timer = time.time()

        if name in ['Quick Sort', 'Merge Sort']:
            algorithm(arr, 0, len(arr)-1)
        else:
            algorithm(arr)
        # capturing the end time
        end_timer = time.time()
        
        #calculating the execution time (in seconds)
        execution_time = end_timer - start_timer
        
        #appending the time in the times array to be used for graphing 
        times.append(execution_time)
        print(f'First 10 elements of Sorted array of size {i} using {name}: {arr[:10]}')
    return arrays, times