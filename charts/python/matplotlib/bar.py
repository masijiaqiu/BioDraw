"""
Author: Xu Zhang
Date: 2016/08/16
Version: 1.0
Description:
"""
import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
from matplotlib.pyplot import savefig


def bar(data, parameters, output):

    # data
    x = []
    y = []
    figsize = (8,6)

    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            x.append(row[0])
            y.append(int(row[1]))

    # parameters
    if 'figsize' in parameters.keys():
        figsize = eval(parameters['figsize'])
    fig = plt.figure(facecolor='w', figsize=figsize)

    if 'xlabel' in parameters.keys():
        plt.xlabel(parameters['xlabel'])
    if 'title' in parameters.keys():
        plt.title(parameters['title'])
    if 'ylabel' in parameters.keys():
        plt.ylabel(parameters['ylabel'])

    param = ''
    if 'align' in parameters.keys():
        param = param + ',align="' + str(parameters['align'])+'"'
    if 'alpha' in parameters.keys():
        param = param + ',alpha=' + str(parameters['alpha'])
    if 'color' in parameters.keys():
        param = param + ',color="' + str(parameters['color'])+'"'
    else:
        param = param + ',color="#108484"'

    # draw
    x_pos = np.arange(len(x))
    exec("plt.bar(x_pos, y "+param+")")

    plt.xticks(x_pos, x)
    savefig(output, format='svg')
