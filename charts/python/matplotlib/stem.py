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

def stem(data, parameters, output):
    #data
    x = []
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
    
        #input array
        for row in f_csv:
            x.append(float(row[0]))

    #parameters
    colors = ['#BCD8E3', '#E0A295', '#75625E', '#7F9AA5', '#AFCDD8', '#E9CDA6', '#70B879', '#E8E098', '#898A82',
             '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F', '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',
             '#70B879', '#AAD9A5', '#8AC2BF']
    color = random.sample(colors, 2)

    bottom = 0
    if 'bottom' in parameters.keys():
    	bottom = parameters['bottom']

    if 'title' in parameters.keys():
        # besides the title, also print the mu and sigma value
        plt.title(parameters['title']+' - Base Line: '+str(bottom))
    if 'xlabel' in parameters.keys():
        plt.xlabel(parameters['xlabel'])
    if 'ylabel' in parameters.keys():
        plt.ylabel(parameters['ylabel'])
    if 'markerface_color' in parameters.keys():
        exec("color[0]='"+str(parameters['markerface_color'])+"'")
    if 'baseline_color' in parameters.keys():
        exec("color[1]='" + str(parameters['baseline_color'])+"'")
    if 'lw' in parameters.keys():
        lw = parameters['lw']


    markerline, stemlines, baseline = plt.stem(np.arange(len(x)), x, '-.',bottom = bottom)
    plt.setp(markerline, 'markerfacecolor', color[0])
    plt.setp(baseline, 'color', color[1], 'linewidth',lw)
    plt.xticks([])
    plt.xlim(-0.5,len(x)+0.5)

    savefig(output,format = 'svg')