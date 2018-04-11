"""
Author: Yu Liujun
Date: 2016/09/05
Version: 1.0
Description:
"""
import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
from matplotlib.pyplot import savefig
import random

def histh_stepline(data, parameters, output):

    # data
    x = []
    n = 0

    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        #headers: list

        #input array number
        n = len(headers)
        i = 0
        while (i < n):
            x.append([])
            i += 1

        for row in f_csv:
            i = 0
            while (i < n):
                x[i].append(float(row[i]))
                i = i+1
    
    # parameters
    if 'xlabel' in parameters.keys():
        plt.xlabel(parameters['xlabel'])
    if 'title' in parameters.keys():
        # besides the title, also print the mu and sigma value
        plt.title(parameters['title']+' - Stepfilled')
    if 'ylabel' in parameters.keys():
        plt.ylabel(parameters['ylabel'])

        # defining num_bin, normed, facecolor, alpha
    if 'num_bin' in parameters.keys():
        num_bin = int(parameters['num_bin'])
    
    #other parameters
    param = ''
    
    colors = ['#BCD8E3', '#E0A295', '#75625E', '#7F9AA5', '#AFCDD8', '#E9CDA6', '#70B879', '#E8E098', '#898A82',
             '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F', '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',
             '#70B879', '#AAD9A5', '#8AC2BF']
    color = random.sample(colors, len(x))


    if 'normed' in parameters.keys():
        param = param + ', normed='+ str(parameters['normed'])
    
    if 'color' in parameters.keys():
        param = param + ',color=' + str(parameters['color'])
    else:
        param = param + ',color=color'
    
    if 'alpha' in parameters.keys():
        param = param + ',alpha=' + str(parameters['alpha'])

    if 'linestyle' in parameters.keys():
        param = param + ', linestyle="' + str(parameters['linestyle'])+'"'

    if 'linewidth' in parameters.keys():
        param = param + ', linewidth =' + str(parameters['linewidth'])

    # draw
    # Create a stepfilled histogram
    exec('fig = plt.hist(x, num_bin'+ param +',histtype="step", label = headers, orientation="horizontal")')
    exec('plt.legend(prop={"size": 10})')
    """
    exec('fig = plt.hist(x, num_bin'+ param +',histtype="stepfilled", stacked=True,label = headers),plot_kwargs=dict(edgecolor="w")')
    exec('plt.legend(prop={"size": 10})')
    """
    savefig(output, format = 'svg')

#end