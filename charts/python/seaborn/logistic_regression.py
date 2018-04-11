"""
Faceted logistic regression
===========================

_thumb: .58, .5
"""
import seaborn as sns
import pandas as pd

# # parameters = {
#   'title': 'logistic regression demo',
#   'color': {
#       'male': '#6495ED',
#       'female': '#F08080'
#   },
#   'x': 'age',
#   'y': 'survived',
#   'col': 'sex',
#   'hue': 'sex',
#   'xlim': [0, 80],
#   'ylim': [-0.05, 1.05]
# # }

def logistic_regression(input_data, parameters, output):
    sns.set(style="darkgrid")
    # Load the example titanic dataset
    df = pd.read_csv(input_data)

    # Show the survival proability as a function of age and sex
    g = sns.lmplot(x=parameters["x"], y=parameters["y"], col=parameters["col"], hue=parameters["hue"], data=df,
                   palette=parameters["color"], y_jitter=.02, logistic=True)
    g.set(xlim=(parameters["xlim"][0],parameters["xlim"][1]), ylim=(parameters["ylim"][0],parameters["ylim"][1]))
    sns.plt.suptitle(parameters["title"])
    sns.plt.savefig(output,format='svg')
