from os import stat
import plotly.figure_factory as ff
import csv
import pandas as pd
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv('data.csv')
data = df['reading_time'].tolist()
mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("Mean of population is :", mean)
print("Standard deviation of population is :", std_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,100):
    set_of_mean = random_set_of_mean(30)
    mean_list.append(set_of_mean)

mean_of_sample1 = statistics.mean(mean_list)
std_deviation = statistics.stdev(mean_list)
print("Mean of sampling data is :", mean)
print("Standard deviation of sampling data is :", std_deviation)
fig = ff.create_distplot([data], ["reading time results"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="Mean"))
fig.show()

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)


z_score = (mean_of_sample1 - mean)/std_deviation
print("Z Score is :", z_score)


