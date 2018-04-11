"""
Author: Yu Liujun
Date: 2016/09/12
Version: 1.0
Description:
Small demonstration of the hlines and vlines plots.
"""
import csv
import random
import numpy as np
import numpy.random as rnd
from matplotlib.pyplot import savefig
import matplotlib.pyplot as plt
plt.rcdefaults()

def vline(data,parameters,output):

    #data
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
            x.append(float(row[1]))
            y.append(float(row[2]))
            count += 1
            n = count

    t = np.arange(n)
    X = np.array(x)
    Y = np.array(y)

    #parameters
    if 'title' in parameters.keys():
        plt.title(parameters['title']+' - Vertical Lines')

    if 'xlabel' in parameters.keys():
        plt.xlabel(parameters['xlabel'])
    if 'ylabel' in parameters.keys():
        plt.ylabel(parameters['ylabel'])

    colors = ['#BCD8E3', '#E0A295', '#75625E', '#7F9AA5', '#AFCDD8', '#E9CDA6', '#70B879', '#E8E098', '#898A82',
             '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F', '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',
             '#70B879', '#AAD9A5', '#8AC2BF']
    color = random.sample(colors, 2)

    if 'color' in parameters.keys():
        exec('color = '+str(parameters['color']))

    param = ''
    if 'alpha' in parameters.keys():
        param = param + ',alpha=' + str(parameters['alpha'])
    if 'lw' in parameters.keys():
        param = param + ',lw ='+str(parameters['lw'])

    
    p1 = plt.plot(t, Y, '^',color = color[0])
    exec('p2 = plt.vlines(t, [0], X'+param+',color = color[1])')


    """
    hax.plot(s + nse, t, 'b^')
    hax.hlines(t, [0], s, lw=2)
    hax.set_xlabel('time (s)')
    hax.set_title('Horizontal lines demo')
    """
    plt.xticks(t+0.4, ticks)
    plt.xlim(-0.5,n-0.5)

    savefig(output, format = 'svg')


def f(t):
    s1 = np.sin(2 * np.pi * t)
    e1 = np.exp(-t)
    return np.absolute((s1 * e1)) + .05

