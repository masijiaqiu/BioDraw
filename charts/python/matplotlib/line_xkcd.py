"""
Author: Yu Liujun
Date: 2016/09/12
Version: 1.0
Description:
"""
import csv
import random
import matplotlib
import numpy as np
from numpy.random import beta
from matplotlib.pyplot import savefig
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
plt.rcdefaults()

def line_xkcd(data, parameters, output):
    with plt.xkcd():
        # Based on "Stove Ownership" from XKCD by Randall Monroe
        # http://xkcd.com/418/

        #data
        x = []
        tags = []
        n = 0
        headers = []
        with open(data) as f:
            f_csv = csv.reader(f)
            headers = next(f_csv)
            n = len(headers)

            i = 1
            while (i < n):
                x.append([])
                i += 1
            for row in f_csv:
                tags.append(row[0])
                i = 1
                while (i < n):
                    x[i-1].append(float(row[i]))
                    i = i+1

        # parameters
        if 'title' in parameters.keys():
            plt.title(parameters['title'])
        if 'xlabel' in parameters.keys():
            plt.xlabel(parameters['xlabel'])
        if 'ylabel' in parameters.keys():
            plt.ylabel(parameters['ylabel'])

        param = ''

        colors = ['#BCD8E3', '#E0A295', '#75625E', '#7F9AA5', '#AFCDD8', '#E9CDA6', '#70B879', '#E8E098', '#898A82',
             '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F', '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',
             '#70B879', '#AAD9A5', '#8AC2BF']
        color = random.sample(colors, len(x))

        if 'color' in parameters.keys():
            exec("color=" + str(parameters['color']))

        n = len(x)
        i=0
        figure = []
        while i <n:
            exec('figure.append(plt.plot(x[i]'+param+',color = color[i]))')
            i+=1

        tag_pos = np.arange(len(tags))
        plt.xticks(tag_pos, tags)

        savefig(output, format = 'svg')