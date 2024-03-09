import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loading and reading the data from the csv file
data_frame = pd.read_csv('algorithm_times.csv')

# setting the seaborn style
sns.set_style(style="whitegrid")

# creating a line plot for each algorithm to compare the time complexities
plt.figure(figsize=(14, 8))
for algorithm in data_frame['Algorithm'].unique():
    algorithm_data = data_frame[data_frame['Algorithm'] == algorithm]
    sns.lineplot(x='Array Size', y='Time Taken', data=algorithm_data, label=algorithm, marker='o')

# setting the labels and the title
plt.xlabel('Array Size')
plt.ylabel('Time Taken (seconds)')
plt.title('Algorithm Time Complexities')
# uncomment the line below to visualize the zoomed in graph
# plt.ylim(0,0.5)


plt.legend(loc='upper right', bbox_to_anchor=(1, 1))

plt.show()
