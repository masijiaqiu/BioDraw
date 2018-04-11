"""
Author: Yu Liujun
Date: 2016/09/1
Version: 1.0
Description:
"""
import csv
import random
import numpy as np
from matplotlib.pyplot import savefig
import matplotlib.pyplot as plt
plt.rcdefaults()

def populationv(data, parameters, output):

    x = []
    y = []
    ticks = []
    n = 0
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        #headers: list

        #input array number
        count = 0
        for row in f_csv:
            ticks.append(str(row[0]))
            x.append(int(row[1]))
            y.append(int(row[2]))
            count += 1
            n = count
    
    X = np.arange(n)
    Y1 = np.array(x)
    Y2 = np.array(y)

    colors = ['#BCD8E3', '#E0A295', '#75625E', '#7F9AA5', '#AFCDD8', '#E9CDA6', '#70B879', '#E8E098', '#898A82',
             '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F', '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',
             '#70B879', '#AAD9A5', '#8AC2BF']
    color = random.sample(colors, 2)

    if 'title' in parameters.keys():
        plt.title(parameters['title']+' - Vertical')

    if 'xlabel' in parameters.keys():
        plt.xlabel(parameters['xlabel'])
    if 'ylabel' in parameters.keys():
        plt.ylabel(parameters['ylabel'])

    if 'color' in parameters.keys():
        exec("color=" + str(parameters['color']))

    p1 = plt.bar(X, +Y1, facecolor=color[0], edgecolor='white', align= 'center',label = headers[1])
    p2 = plt.bar(X, -Y2, facecolor=color[1], edgecolor='white', align = 'center',label = headers[2]) 
    plt.legend(handles= [p1,p2])

    for a,b in zip(X,Y1):
        plt.text(a, b+0.05, b, ha='center', va= 'bottom')
    for a,b in zip(X,Y2):
        plt.text(a, -b-0.05, b, ha='center', va= 'top')

    plt.yticks([])
    plt.xticks(X+0.4, ticks)
    plt.xlim(-0.5,n-0.5)
    savefig(output, format = 'svg')
    #end



