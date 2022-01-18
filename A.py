import statistics
import random
import plotly_express as px
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go

popuplation=pd.read_csv("ATB.csv")
real_population=popuplation["temp"].tolist()

mean_rp = statistics.mean(real_population)
std_rp = statistics.stdev(real_population)
print("frp mean",mean_rp)
print("frp std",std_rp)

fig = ff.create_distplot([real_population],["temp"],show_hist=True)
fig.show()

def random_set_of_means(counter):
    dataSet=[]
    for i in range(0,counter):
        fake_population_random=random.randint(0,len(real_population))
        fake_population_value= real_population[fake_population_random]
        dataSet.append(fake_population_value)
    mean = statistics.mean(dataSet)
    return mean

def showfig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()


def setup():
    mean_list=[]
    for i in range(0,1000):
        means=random_set_of_means(100)
        mean_list.append(means)
    showfig(mean_list)
    print("SAMPLING MEAN ",statistics.mean(mean_list))
    print("s std ",statistics.stdev(mean_list))


setup()
