"""
Linear regression with marginal distributions
=============================================

_thumb: .5, .6
"""
import seaborn as sns
import pandas as pd

# parameters = {
#   'title': 'Linear regression with marginal distributions',
#   'data_header': ['total_bill', 'tip'],
#   'xlim': [0, 60],
#   'ylim': [0,12]
# }
def regression_marginals(input_data, parameters, output):
    sns.set(style="darkgrid", color_codes=True)

    tips = pd.read_csv(input_data)
    g = sns.jointplot(parameters['data_header'][0], parameters['data_header'][1], data=tips, kind="reg",
                      xlim=(parameters['xlim'][0],parameters['xlim'][1]), ylim=(parameters['ylim'][0],parameters['ylim'][1]), color="black", size=7)
    sns.plt.title(parameters['title'])
    sns.plt.savefig(output,format='svg')