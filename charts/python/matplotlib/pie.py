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


def pie_normal(data, parameters, output):

    # data
    label = []
    raw_data = []
    figsize = (8,6)
    legend = ()
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            label.append(row[0])
            raw_data.append(float(row[1]))
    perc_data = [100.*i/sum(raw_data) for i in raw_data]

    # parameters
    COLORS = ['#215C58', '#0BA895', '#7C976A', '#D4643F', '#F29653', '#CDB56F', '#70B879', '#7F9AA5', '#AFCDD8',
             '#E8E098', '#E9CDA6',  '#E0A295', '#75625E','#898A82', '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F',
             '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',  '#70B879', '#AAD9A5', '#8AC2BF']
    color = COLORS[:len(perc_data)]+['w']

    if 'figsize' in parameters.keys():
        figsize = eval(parameters['figsize'])
    fig = plt.figure(facecolor='w', figsize=figsize)
    ax = fig.add_subplot(111)
    box = ax.get_position()

    if 'title' in parameters.keys():
        plt.title(parameters['title'])

    if 'percentage_legend' in parameters.keys():
        label = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(label, perc_data)]

    # draw
    pie_wedge_collection =plt.pie(perc_data, colors=color,
         autopct=None,
        labeldistance= 1.)
    for pie_wedge in pie_wedge_collection[0]:
        pie_wedge.set_edgecolor('white')

    if parameters['legend'] == 'True':
        ax.set_position([box.x0-0.12, box.y0+0.07, box.width * 0.8, box.height*0.88])
        fig.legend( pie_wedge_collection[0], label, 'center right', bbox_to_anchor=(0.9, 0.25), fontsize=12)
    else:
        ax.set_position([box.x0, box.y0+0.07, box.width * 0.8, box.height*0.88])

    plt.axis('equal')
    savefig(output, format='svg')


def pie_doughnut(data, parameters, output):

    # data
    label = []
    raw_data = []
    figsize = (8,6)
    legend = ()
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            label.append(row[0])
            raw_data.append(float(row[1]))
    perc_data = [100.*i/sum(raw_data) for i in raw_data]

    # parameters
    COLORS = ['#215C58', '#0BA895', '#7C976A', '#D4643F', '#F29653', '#CDB56F', '#70B879', '#7F9AA5', '#AFCDD8',
             '#E8E098', '#E9CDA6',  '#E0A295', '#75625E','#898A82', '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F',
             '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',  '#70B879', '#AAD9A5', '#8AC2BF']
    color = COLORS[:len(perc_data)]+['w']

    if 'figsize' in parameters.keys():
        figsize = eval(parameters['figsize'])
    fig = plt.figure(facecolor='w', figsize=figsize)
    ax = fig.add_subplot(111)
    box = ax.get_position()

    if 'title' in parameters.keys():
        plt.title(parameters['title'])

    if 'percentage_legend' in parameters.keys():
        label = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(label, perc_data)]
    
    # draw
    pie_wedge_collection =plt.pie(perc_data, colors=color,
        autopct= None,
        labeldistance= 1.)
    for pie_wedge in pie_wedge_collection[0]:
        pie_wedge.set_edgecolor('white')
    pie_wedge_collection_inside =ax.pie([100], colors='white', shadow=False, radius= 0.5)
    for pie_wedge in pie_wedge_collection_inside[0]:
        pie_wedge.set_edgecolor('white')

    if parameters['legend'] == 'True':
        ax.set_position([box.x0-0.12, box.y0+0.07, box.width * 0.8, box.height*0.88])
        fig.legend( pie_wedge_collection[0], label, 'center right', bbox_to_anchor=(0.9, 0.25), fontsize=12)
    else:
        ax.set_position([box.x0, box.y0+0.07, box.width * 0.8, box.height*0.88])

    plt.axis('equal')
    savefig(output, format='svg')


def pie_semicircle(data, parameters, output):

    # data
    label = []
    raw_data = []
    figsize = (8,6)
    legend = ()
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            label.append(row[0])
            raw_data.append(float(row[1]))
    perc_data = [100.*i/sum(raw_data) for i in raw_data]

    # parameters
    COLORS = ['#215C58', '#0BA895', '#7C976A', '#D4643F', '#F29653', '#CDB56F', '#70B879', '#7F9AA5', '#AFCDD8',
             '#E8E098', '#E9CDA6',  '#E0A295', '#75625E','#898A82', '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F',
             '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',  '#70B879', '#AAD9A5', '#8AC2BF']
    color = COLORS[:len(perc_data)]+['w']

    if 'figsize' in parameters.keys():
        figsize = eval(parameters['figsize'])
    fig = plt.figure(facecolor='w', figsize=figsize)
    ax = fig.add_subplot(111)
    box = ax.get_position()

    if 'title' in parameters.keys():
        plt.title(parameters['title'])

    if 'percentage_legend' in parameters.keys():
        label = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(label, perc_data)]
    
    # draw
    perc_data += [sum(perc_data)]
    label += ['']
    color += ['w']
    pie_wedge_collection =plt.pie(perc_data, colors=color,
         autopct=None,
        labeldistance= 1.5)
    for pie_wedge in pie_wedge_collection[0]:
        pie_wedge.set_edgecolor('white')

    if parameters['legend'] == 'True':
        ax.set_position([box.x0-0.12, box.y0+0.07, box.width * 0.8, box.height*0.88])
        fig.legend( pie_wedge_collection[0][:-1], label[:-1], 'center right', bbox_to_anchor=(0.9, 0.25), fontsize=12)
    else:
        ax.set_position([box.x0, box.y0+0.07, box.width * 0.8, box.height*0.88])

    plt.axis('equal')
    savefig(output, format='svg')

def pie_semicircle_doughnut(data, parameters, output):

    # data
    label = []
    raw_data = []
    figsize = (8,6)
    legend = ()
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            label.append(row[0])
            raw_data.append(float(row[1]))
    perc_data = [100.*i/sum(raw_data) for i in raw_data]

    # parameters
    COLORS = ['#215C58', '#0BA895', '#7C976A', '#D4643F', '#F29653', '#CDB56F', '#70B879', '#7F9AA5', '#AFCDD8',
             '#E8E098', '#E9CDA6',  '#E0A295', '#75625E','#898A82', '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F',
             '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',  '#70B879', '#AAD9A5', '#8AC2BF']
    color = COLORS[:len(perc_data)]+['w']

    if 'figsize' in parameters.keys():
        figsize = eval(parameters['figsize'])
    fig = plt.figure(facecolor='w', figsize=figsize)
    ax = fig.add_subplot(111)
    box = ax.get_position()

    if 'title' in parameters.keys():
        plt.title(parameters['title'])

    if 'percentage_legend' in parameters.keys():
        label = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(label, perc_data)]
    
    # draw
    perc_data += [sum(perc_data)]
    label += ['']
    color += ['w']
    pie_wedge_collection =plt.pie(perc_data, colors=color,
         autopct=None,
        labeldistance= 1.5)
    for pie_wedge in pie_wedge_collection[0]:
        pie_wedge.set_edgecolor('white')
    pie_wedge_collection_inside =ax.pie([100], colors='white',shadow=False, radius= 0.5)
    for pie_wedge in pie_wedge_collection_inside[0]:
                pie_wedge.set_edgecolor('white')
    
    if parameters['legend'] == 'True':
        ax.set_position([box.x0-0.12, box.y0+0.07, box.width * 0.8, box.height*0.88])
        fig.legend( pie_wedge_collection[0][:-1], label[:-1], 'center right', bbox_to_anchor=(0.9, 0.25), fontsize=12)
    else:
        ax.set_position([box.x0, box.y0+0.07, box.width * 0.8, box.height*0.88])

    plt.axis('equal')
    savefig(output, format='svg')
