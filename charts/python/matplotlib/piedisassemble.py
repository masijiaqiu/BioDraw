"""
Author: Masijia Qiu
Date: 2016/08/16
Version: 1.0
Description:
"""
import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
from matplotlib.pyplot import savefig
from matplotlib.gridspec import GridSpec
import math


def pie_disassemble(data, parameters, output):
    # data
    label = []
    raw_data = []
    figsize = (8,6)
    legend = []
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            label.append(row[0])
            raw_data.append(float(row[1]))
    perc_data = [i/sum(raw_data) for i in raw_data]
    N = len(perc_data)

    # parameters
    COLORS = ['#215C58', '#0BA895', '#7C976A', '#D4643F', '#F29653', '#CDB56F', '#70B879', '#7F9AA5', '#AFCDD8',
             '#E8E098', '#E9CDA6',  '#E0A295', '#75625E','#898A82', '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F',
             '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',  '#70B879', '#AAD9A5', '#8AC2BF']

    if 'figsize' in parameters.keys():
        figsize = eval(parameters['figsize'])
    fig = plt.figure(facecolor='w', figsize=figsize)

    if parameters['legend'] == 'True':
        N += 1
    if 'title' in parameters.keys():
        fig.text(0.2, 0.8, parameters['title'], size=20)

    # draw
    index = 1
    for s,l in zip(perc_data, label):
        plt.subplot(1, N, index, aspect=1)
        pie_wedge_collection = plt.pie([1-s,s],  colors=['w', COLORS[index]], startangle=90, radius=1)
        plt.title(l)
        legend += [pie_wedge_collection[0][1]]
        index += 1

    if 'percentage_legend' in parameters.keys():
        label = ['{0} - {1:1.2f} %'.format(i,j*100) for i,j in zip(label, perc_data)]

    if parameters['legend'] == 'True':
        fig.legend( legend, label, fontsize='small', loc=(0.6, 0.1 ))

    savefig(output, format='svg')


def pie_disassemble_doughnut(data, parameters, output):
    # data
    label = []
    raw_data = []
    figsize = (8,6)
    legend = []
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            label.append(row[0])
            raw_data.append(float(row[1]))
    perc_data = [i/sum(raw_data) for i in raw_data]
    N = len(perc_data)

    # parameters
    COLORS = ['#215C58', '#0BA895', '#7C976A', '#D4643F', '#F29653', '#CDB56F', '#70B879', '#7F9AA5', '#AFCDD8',
             '#E8E098', '#E9CDA6',  '#E0A295', '#75625E','#898A82', '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F',
             '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',  '#70B879', '#AAD9A5', '#8AC2BF']
    color = COLORS[:len(perc_data)]+['w']

    if 'figsize' in parameters.keys():
        figsize = eval(parameters['figsize'])
    fig = plt.figure(facecolor='w', figsize=figsize)
    the_grid = GridSpec(1, N)

    if 'title' in parameters.keys():
        fig.text(0.4, 0.8, parameters['title'])

    if 'percentage_legend' in parameters.keys():
        label = ['{0} - {1:1.2f} %'.format(i,j*100) for i,j in zip(label, perc_data)]

    # draw
    index = 0
    for s, l in zip(perc_data, label):
        plt.subplot(the_grid[0, index], aspect=1)
        circle_line = plt.pie([1],radius= 0.8, colors='w')
        circle_line[0][0].set_edgecolor(color[index])
        pie_wedge_collection = plt.pie([1-s,s],  colors=['w', color[index]], startangle=90, radius=1)
        for pie_wedge in pie_wedge_collection[0]:
            pie_wedge.set_edgecolor('white')
        pie_wedge_collection[0][0].set_alpha(0.1)
        pie_wedge_collection_inside = plt.pie([1],  colors='w', radius=0.6)
        for pie_wedge in pie_wedge_collection_inside[0]:
            pie_wedge.set_edgecolor('white')
        legend += [pie_wedge_collection[0][1]]
        plt.title(l)
        index += 1

    if parameters['legend'] == 'True':
        fig.legend( legend, label, fontsize='small', loc=(0.7, 0.1))

    savefig(output, format='svg')

def pie_disassemble_area(data, parameters, output):
    # data
    label = []
    raw_data = []
    figsize = (8,6)
    legend = []
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            label.append(row[0])
            raw_data.append(float(row[1]))
    perc_data = [i/sum(raw_data) for i in raw_data]
    N = len(perc_data)

    # parameters
    COLORS = ['#215C58', '#0BA895', '#7C976A', '#D4643F', '#F29653', '#CDB56F', '#70B879', '#7F9AA5', '#AFCDD8',
             '#E8E098', '#E9CDA6',  '#E0A295', '#75625E','#898A82', '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F',
             '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',  '#70B879', '#AAD9A5', '#8AC2BF']

    if 'figsize' in parameters.keys():
        figsize = eval(parameters['figsize'])
    fig = plt.figure(facecolor='w', figsize=figsize)

    if parameters['legend'] == 'True':
        N += 1
    if 'title' in parameters.keys():
        fig.text(0.2, 0.8, parameters['title'], size=20)

    # draw
    index = 1
    radiu = [math.sqrt(i/max(perc_data)) for i in perc_data]
    for r,l in zip(radiu, label):
        plt.subplot(1, N, index, aspect=1)
        pie_wedge_collection = plt.pie([1],  colors=[COLORS[index]], startangle=90, radius=r)
        plt.title(l)
        legend += [pie_wedge_collection[0][0]]
        index += 1

    if 'percentage_legend' in parameters.keys():
        label = ['{0} - {1:1.2f} %'.format(i,j*100) for i,j in zip(label, perc_data)]

    if parameters['legend'] == 'True':
        fig.legend( legend, label, fontsize='small', loc=(0.6, 0.1 ))

    savefig(output, format='svg')


def pie_area(data, parameters, output):
    # data
    label = []
    raw_data = []
    legend = []
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            label.append(row[0])
            raw_data.append(float(row[1]))
    perc_data = [i/sum(raw_data) for i in raw_data]
    N = len(perc_data)

    # parameters
    COLORS = ['#215C58', '#0BA895', '#7C976A', '#D4643F', '#F29653', '#CDB56F', '#70B879', '#7F9AA5', '#AFCDD8',
             '#E8E098', '#E9CDA6',  '#E0A295', '#75625E','#898A82', '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F',
             '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',  '#70B879', '#AAD9A5', '#8AC2BF']
    
    figsize = (8,6)
    if 'figsize' in parameters.keys():
        figsize = eval(parameters['figsize'])
    fig = plt.figure(facecolor='w', figsize=figsize)

    if 'title' in parameters.keys():
        plt.title(parameters['title'])
    
    index = 0
    zipped = zip(perc_data, label)
    zipped.sort(key = lambda t: t[0], reverse=True)
    for d, l in zipped:
        pie_wedge_collection = plt.pie([1],  colors=[COLORS[index]], radius=math.sqrt(d))
        for pie_wedge in pie_wedge_collection[0]:
            pie_wedge.set_edgecolor('white')
        legend += [pie_wedge_collection[0][0]]
        index += 1

    if 'percentage_legend' in parameters.keys():
        legend_label = ['{0} - {1:1.2f} %'.format(j,i*100) for i, j in zipped]

    if parameters['legend'] == 'True':
        fig.legend( legend, legend_label, fontsize='small', loc=(0.78, 0.05 ))

    plt.axis('equal')
    savefig(output, format='svg')


def pie_bar(data, parameters, output):
    # data
    label = []
    raw_data = []
    figsize = (8,6)
    legend = []
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            label.append(row[0])
            raw_data.append(float(row[1]))
    perc_data = [i/sum(raw_data) for i in raw_data]
    N = len(perc_data)

    # parameters
    COLORS = ['#215C58', '#0BA895', '#7C976A', '#D4643F', '#F29653', '#CDB56F', '#70B879', '#7F9AA5', '#AFCDD8',
             '#E8E098', '#E9CDA6',  '#E0A295', '#75625E','#898A82', '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F',
             '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',  '#70B879', '#AAD9A5', '#8AC2BF']
    color = COLORS[:len(perc_data)]+['w']

    if 'figsize' in parameters.keys():
        figsize = eval(parameters['figsize'])
    fig = plt.figure(facecolor='w', figsize=figsize)
    ax = fig.add_subplot(111, aspect=1)
    box = ax.get_position()

    if 'title' in parameters.keys():
        plt.title(parameters['title'])

    # draw
    index = 0
    for s, l in zip(perc_data, label):
        pie_wedge_collection = plt.pie([1-s, s],  colors=['w', color[index]], startangle=90, radius=1.-index/float(N))
        for pie_wedge in pie_wedge_collection[0]:
            pie_wedge.set_edgecolor('white')
        pie_wedge_collection_inside = plt.pie([1],  colors='w', radius=1.-(index + 0.5)/float(N))
        for pie_wedge in pie_wedge_collection_inside[0]:
            pie_wedge.set_edgecolor('white')
        legend += [pie_wedge_collection[0][1]]
        index += 1

    if 'percentage_legend' in parameters.keys():
        label = ['{0} - {1:1.2f} %'.format(i,j*100) for i,j in zip(label, perc_data)]

    if parameters['legend'] == 'True':
        ax.set_position([box.x0-0.12, box.y0+0.07, box.width * 0.8, box.height*0.88])
        fig.legend( legend, label, 'center right', bbox_to_anchor=(0.9, 0.25), fontsize=12)
    else:
        ax.set_position([box.x0, box.y0+0.07, box.width * 0.8, box.height*0.88])

    plt.axis('equal')
    savefig(output, format='svg')