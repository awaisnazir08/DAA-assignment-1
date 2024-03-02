import matplotlib.pyplot as plt
import seaborn as sns

def createPlot(sizes, times, name):
    plt.figure(figsize=(12, 8))  # Set the figure size before creating the plot
    sns.set_style("darkgrid") 
    sns.lineplot(x=sizes, y=times, marker='o', label=name)
    plt.xlabel('Array Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.title(f'{name} Time Complexity Analysis')
    plt.legend()
    plt.show()
