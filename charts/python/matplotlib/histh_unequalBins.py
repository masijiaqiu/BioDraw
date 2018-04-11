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

def histh_unequalBins(data, parameters, output):

    # data
    x = []
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
    
        #input array
        for row in f_csv:
            x.append(float(row[0]))
    
    # total of inputs
    count = len(x)

    # parameters
    if 'title' in parameters.keys():
        # besides the title, also print the mu and sigma value
        plt.title(parameters['title']+' - Unequal Bins Horizontal')
    if 'xlabel' in parameters.keys():
        plt.xlabel(parameters['xlabel'])
    if 'ylabel' in parameters.keys():
        plt.ylabel(parameters['ylabel'])

    # defining normed, facecolor, alpha
    
    param = ''
    bins = []

    colors = ['#BCD8E3', '#E0A295', '#75625E', '#7F9AA5', '#AFCDD8', '#E9CDA6', '#70B879', '#E8E098', '#898A82',
             '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F', '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',
             '#70B879', '#AAD9A5', '#8AC2BF']
    color = random.sample(colors, len(headers))

    if 'normed' in parameters.keys():
        param = param + ', normed='+ str(parameters['normed'])+''

    if 'color' in parameters.keys():
        param = param + ',color="' + str(parameters['color'])+'"'
    else:
        param = param + ',color="'+color[0]+'"'

    if 'alpha' in parameters.keys():
        param = param + ',alpha=' + str(parameters['alpha'])

    if 'rwidth' in parameters.keys():
        param = param + ',rwidth=' + str(parameters['rwidth'])
        
    if 'bins' in parameters.keys():
        exec("bins ="+parameters['bins'])

    # draw
    # Create a histogram by providing the bin edges (unequally spaced).
    exec("fig = plt.hist(x, bins"+param+", histtype='bar',orientation = 'horizontal')")

    savefig(output, format='svg')

    #end