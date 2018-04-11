
"""
Author: Yu Liujun
Date: 2016/09/12s
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

def bar_xkcd(data, parameters, output):
    with plt.xkcd():
        # Based on "Stove Ownership" from XKCD by Randall Monroe
        # http://xkcd.com/418/

        # data
        x = []
        y = []
        with open(data) as f:
            f_csv = csv.reader(f)
            headers = next(f_csv)
            for row in f_csv:
                x.append(row[0])
                y.append(int(row[1]))

        # parameters
        if 'xlabel' in parameters.keys():
            plt.xlabel(parameters['xlabel'])
        if 'title' in parameters.keys():
            plt.title(parameters['title'])
        if 'ylabel' in parameters.keys():
            plt.ylabel(parameters['ylabel'])

        param = ''

        colors = ['#BCD8E3', '#E0A295', '#75625E', '#7F9AA5', '#AFCDD8', '#E9CDA6', '#70B879', '#E8E098', '#898A82',
             '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F', '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',
             '#70B879', '#AAD9A5', '#8AC2BF']
        color = random.sample(colors, len(x))

        if 'align' in parameters.keys():
            param = param + ',align="' + str(parameters['align'])+'"'
        if 'color' in parameters.keys():
            exec("color=" + str(parameters['color']))
        param = param + ',color = color'
        # draw
        x_pos = np.arange(len(x))
        exec("plt.bar(x_pos, y "+param+")")
        plt.xticks(x_pos, x)
        """
        fig = plt.figure()
        ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
        ax.bar([-0.125, 1.0 - 0.125], [0, 100], 0.25)
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.set_xticks([0, 1])
        ax.set_xlim([-0.5, 1.5])
        ax.set_ylim([0, 110])
        ax.set_xticklabels(['CONFIRMED BY\nEXPERIMENT', 'REFUTED BY\nEXPERIMENT'])
        plt.yticks([])

        plt.title("CLAIMS OF SUPERNATURAL POWERS")

        fig.text(
            0.5, 0.05,
            '"The Data So Far" from xkcd by Randall Monroe',
            ha='center')
        """
        savefig(output, format = 'svg')