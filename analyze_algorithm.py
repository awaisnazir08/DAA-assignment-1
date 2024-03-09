import random
import time
import pandas as pd
import os

def time_of_algorithm(algorithm, name=''):

    file_path = 'algorithm_times.csv'
    
    # Checking if the file path already exists
    if os.path.exists(file_path):
        # if exists, load the data from it
        data_frame = pd.read_csv(file_path)
    else:
        # otherwise create a new dataframe structure
        data_frame = pd.DataFrame(columns=['Algorithm', 'Array Size', 'Time Taken'])

    #array sizes from 10-10000
    arrays = list(range(10, 10011, 1000))
    
    #empty list for storing the times for sorting each array
    times = []

    # This block of code is a loop that iterates over different array sizes specified in the `arrays`
    # list. For each array size `i`, it generates a random array `arr` either containing
    # floating-point numbers between 0 and 1 (if the algorithm is 'Bucket Sort') or integers between 0
    # and 1,000,000 (for other sorting algorithms).
    for i in arrays:
        if name == 'Bucket Sort':
            arr = [random.uniform(0, 1) for _ in range(i)]
        else:
            arr = [random.randint(0, 1000000) for _ in range(i)]

        print(f'First and Last 10 elements of Unsorted array of size {i}: {arr[:10]} ... {arr[-10:]}')

        #noting the start time
        start_timer = time.time()

        if name in ['Quick Sort', 'Merge Sort']:
            algorithm(arr, 0, len(arr) - 1)
        else:
            algorithm(arr)

        #noting the end time
        end_timer = time.time()
        
        #calculating the time and then appending it into the times array
        execution_time = end_timer - start_timer
        times.append(execution_time)

        #printing the first 10 elements of the sorted array
        print(f'First and Last 10 elements of Sorted array of size {i} using {name}: {arr[:10]} ... {arr[-10:]}')
        print(f'Time taken to sort: {execution_time} seconds')
        print('\n\n')

        # appending the data in the DataFrame
        data_frame = data_frame._append({'Algorithm': name, 'Array Size': i, 'Time Taken': execution_time}, ignore_index=True)

    # saving the dataframe as a csv file
    data_frame.to_csv(file_path, index=False)

    return arrays, times
