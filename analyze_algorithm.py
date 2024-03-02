import random
import time
def time_of_algorithm(algorithm):
    arrays = list(range(10, 10011, 1000))
    times = []
    for i in arrays:
        arr = [random.randint(0, 1000000) for _ in range(i)]
        print(f'First 20 elements of Unsorted array of size {i}: {arr[:20]}')
        start_timer = time.time()
        algorithm(arr)
        end_timer = time.time()
        execution_time = end_timer - start_timer
        times.append(execution_time)
        print(f'First 20 elements of Sorted array of size {i}: {arr[:20]}')
    return arrays, times