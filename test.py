import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already sorted, so no need to check them
        flag = 0
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
        if flag == 0:
            break

# Function to analyze the time complexity of an algorithm
def analyze_algorithm(algorithm, sizes):
    times = []

    for n in sizes:
        arr = [random.randint(1, 1000000) for _ in range(n)]

        start_time = time.time()
        algorithm(arr)
        end_time = time.time()

        execution_time = end_time - start_time
        times.append(execution_time)

    return times

# Function to plot the results
def plot_results(sizes, results, algorithm_name):
    plt.plot(sizes, results, label=algorithm_name)

# Sizes of the arrays to be tested
array_sizes = list(range(10, 10011, 1000))
print(array_sizes)
# Analyzing and plotting for Bubble Sort
bubble_sort_times = analyze_algorithm(bubble_sort, array_sizes)
plot_results(array_sizes, bubble_sort_times, "Bubble Sort")

# Displaying the plot
plt.xlabel('Array Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Bubble Sort Time Complexity Analysis')
plt.legend()
plt.show()
