"""
Author: Ziwei JIANG
Date: 2016/09/08
Version: 1.0
Description:
"""
import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
from matplotlib.pyplot import savefig
import random


def line538(data, parameters, output):
	#data
    x=[]
    y=[]
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        count=len(headers)/2
        for a in range(count):
            x.append([])
            y.append([])
        for row in f_csv:
            for a in range(count):
                x[a].append(row[2*a])
                y[a].append(row[2*a+1])
    #parameter
    figsize=(8,6)
    param=''
    examples = count
    width = 2.6
    setcolor=[]
    colors = ['#BCD8E3', '#E0A295', '#75625E', '#7F9AA5', '#AFCDD8', '#E9CDA6', '#70B879', '#E8E098', '#898A82',
             '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F', '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',
             '#70B879', '#AAD9A5', '#8AC2BF']
    color = random.sample(colors, examples)

    if 'figsize' in parameters.keys():
        figsize = eval(parameters['figsize'])
    fig=plt.figure(figsize=figsize)
    if 'xlabel' in parameters.keys():
        plt.xlabel(parameters['xlabel'])
    if 'title' in parameters.keys():
        plt.title(parameters['title'])
    if 'ylabel' in parameters.keys():
        plt.ylabel(parameters['ylabel'])
    if 'color' in parameters.keys():
        color=eval(parameters['color'])
    if 'width' in parameters.keys():
    	param=param+",linewidth="+str(parameters['width'])



	# draw
    with plt.style.context('fivethirtyeight'):
        for a in range(count):
            exec("plot"+str(a)+"=plt.plot(x["+str(a)+"]"+",y["+str(a)+"],label=headers[2*a+1],color=color["+str(a)+"]"+param+")")

	# adding horizontal grid lines
    plt.grid(True,linestyle='--',linewidth=0.5)

    #add legend
    plt.legend()


    savefig(output,format='svg')

