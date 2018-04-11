"""
Plotting a three-way ANOVA
==========================

_thumb: .42, .5
"""
import seaborn as sns
import pandas as pd
import csv 

parameters = {
    'title': 'Plotting a three-way ANOVA'
}

def pointplot_anova(input_data, parameters, output):
    sns.set(style="whitegrid")
    # Load the example exercise dataset
    header = []
    with open(input_data) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            for item in row:
                header.append(item)
            break
    f.close()

    df = pd.read_csv(input_data)
    # Draw a pointplot to show pulse as a function of three categorical factors
    g = sns.factorplot(x=header[5], y=header[4], hue=header[6], col=header[3], data=df,
                       capsize=.2, palette="YlGnBu_d", size=6, aspect=.75)
    g.despine(left=True)
    sns.plt.suptitle(parameters['title'])
    sns.plt.savefig(output,format='svg')
