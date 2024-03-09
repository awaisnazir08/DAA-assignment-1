import matplotlib.pyplot as plt
import seaborn as sns

def createPlot(sizes, times, name):
    """
    The function `createPlot` generates a line plot to visualize the relationship between array sizes
    and execution times with a specified name for the plot.
    
    :param sizes: The `sizes` parameter is a list of values representing the input sizes (e.g., array
    sizes) for which corresponding execution times are provided
    :param times: The `times` parameter in the `createPlot` function represents the execution times
    corresponding to different array sizes. These times are typically measured in seconds and are used
    to analyze the time complexity of an algorithm or operation as the input size varies
    :param name: The `name` parameter is a string that represents the name or label of the plot. It is
    used to customize the title and legend of the plot based on the data being visualized
    """
    plt.figure(figsize=(12, 8))  # Set the figure size before creating the plot
    sns.set_style("darkgrid")
    sns.lineplot(x=sizes, y=times, marker='o', label=name, color = 'green')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.title(f'{name} Time Complexity Analysis')
    plt.legend()
    plt.show()
