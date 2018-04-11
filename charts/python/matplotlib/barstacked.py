"""
Author: Masijia QIU 
Date: 2016/08/19
Version: 1.0
Description:
"""
import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
from matplotlib.pyplot import savefig
import random

def barstacked(data, parameters, output):
    # data
    x = []
    y = []
    legend = ()
    example_num = 0
    figsize = (8,6)
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        example_num = len(headers)-1
        for row in f_csv:
            x.append(row[0])
            y.append(map(float, row[1:example_num+1]))

    # parameters
    colors = ['#BCD8E3', '#E0A295', '#75625E', '#7F9AA5', '#AFCDD8', '#E9CDA6', '#70B879', '#E8E098', '#898A82',
             '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F', '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',
             '#70B879', '#AAD9A5', '#8AC2BF']
    color = random.sample(colors, len(x))

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
        param = param + ',align="' + parameters['align']+'"'
    if 'alpha' in parameters.keys():
        param = param + ',alpha=' + str(parameters['alpha'])

    # draw
    x_pos = [ float(t)+0.2 for t in np.arange(example_num)]
    bottom = [0.]* example_num
    ax = fig.add_subplot(111)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0+0.07, box.width * 0.82, box.height*0.9])
    for i in range(len(x)):
        cbar = plt.bar(x_pos, y[i], width=0.5, bottom=bottom, color=color[i], edgecolor='')
        legend = legend + (cbar[0],)
        bottom = [a+b for a, b in zip(y[i], bottom)]

    plt.xticks(x_pos, headers[1:])
    if parameters['legend'] == 'True':
        fig.legend(legend, x, 'center right', bbox_to_anchor=(0.98, 0.5), fontsize =10)

    savefig(output, format='svg')


def barstackedn(data, parameters, output):
    # data
    x = []
    y = []
    legend = ()
    example_num = 0
    figsize = (8,6)
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        example_num = len(headers)-1
        for row in f_csv:
            x.append(row[0])
            y.append(map(float, row[1:example_num+1]))

    # parameters
    item_num = len(x)
    colors = ['#BCD8E3', '#E0A295', '#75625E', '#7F9AA5', '#AFCDD8', '#E9CDA6', '#70B879', '#E8E098', '#898A82',
             '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F', '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',
             '#70B879', '#AAD9A5', '#8AC2BF']
    color = random.sample(colors, item_num)

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
        param = param + ',align="' + parameters['align']+'"'
    if 'alpha' in parameters.keys():
        param = param + ',alpha=' + str(parameters['alpha'])

    # draw
    x_pos = [ float(t)+0.2 for t in np.arange(example_num)]
    bottom = [0.]* example_num
    ax = fig.add_subplot(111)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0+0.07, box.width * 0.82, box.height*0.9])
    for i in range(example_num):
        temp_sum = 0
        for j in range(item_num):
            temp_sum += y[j][i]
        for j in range(item_num):
            y[j][i] /= float(temp_sum)
    for i in range(item_num):
        cbar = plt.bar(x_pos, y[i], width=0.5, bottom=bottom, color=color[i], edgecolor='')
        legend = legend + (cbar[0],)
        bottom = [a+b for a, b in zip(y[i], bottom)]
    plt.ylim(ymax=1)
    plt.xticks(x_pos, headers[1:])
    if parameters['legend'] == 'True':
        fig.legend(legend, x, 'center right', bbox_to_anchor=(0.98, 0.5), fontsize =10)

    savefig(output, format='svg')