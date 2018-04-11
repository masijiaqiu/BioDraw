"""
Author: Masijia QIU 
Date: 2016/08/18
Version: 1.0
Description:
"""
import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
from matplotlib.pyplot import savefig
import random


def bargroup(data, parameters, output):

    # data
    x = []
    y = []
    legend = ()
    features = 0
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        features = len(headers)-1
        for row in f_csv:
            x.append(row[0])
            y.append(map(float, row[1:features+1]))

    # parameters
    examples = len(x)
    width = 0.6
    figsize = (6,6)
    colors = ['#BCD8E3', '#E0A295', '#75625E', '#7F9AA5', '#AFCDD8', '#E9CDA6', '#70B879', '#E8E098', '#898A82',
             '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F', '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',
             '#70B879', '#AAD9A5', '#8AC2BF']
    color = random.sample(colors, examples)

    if 'figsize' in parameters.keys():
        figsize = eval(parameters['figsize'])
    fig = plt.figure(facecolor='w', figsize=figsize)
    if 'xlabel' in parameters.keys():
        plt.xlabel(parameters['xlabel'])
    if 'title' in parameters.keys():
        plt.title(parameters['title'])
    if 'ylabel' in parameters.keys():
        plt.ylabel(parameters['ylabel'])
    if 'width' in parameters.keys():
        width = float(parameters['width'])


    param = ''
    if 'width' in parameters.keys():
        param = param + ',width="' + str(parameters['width'])+'"'
    if 'alpha' in parameters.keys():
        param = param + ',alpha="' + str(parameters['alpha'])+'"'

    # draw
    ax = fig.add_subplot(111)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0+0.07, box.width * 0.82, box.height*0.9])
    xlocation_init = [ float(t)*width*(examples+2)+0.1 for t in np.arange(features)]

    for i in range(examples):
        xlocation = [(t + width*i*1.1) for t in xlocation_init]
        cbar = plt.bar(xlocation, y[i], width, color=color[i], edgecolor='')
        legend = legend + (cbar[0],)

    if 'legend' in parameters.keys() and parameters['legend']== 'True':
        fig.legend(legend, x, 'center right', bbox_to_anchor=(0.98, 0.5), fontsize =10)

    plt.xticks(xlocation_init, x)

    savefig(output, format='svg')