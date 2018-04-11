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
from matplotlib import mlab

def hist_cumulated_reversed(data, parameters, output):

	# data
    x = []
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
    
        #input array
        for row in f_csv:
            x.append(float(row[0]))

    #   a total count of the number of bars - predefined in jason
    #   defaultly set to 20, can be read and modified later
    num_bin = 20
    
    # total of inputs
    count = len(x)

    # a mean of distribution
    mu = sum(i for i in x)/count

    # standard deviation of distribution
    sdsq = sum([(i - mu) ** 2 for i in x])
    sigma = (sdsq / count) ** .5

    # parameters
    if 'xlabel' in parameters.keys():
        plt.xlabel(parameters['xlabel'])
    if 'title' in parameters.keys():
        # besides the title, also print the mu and sigma value
        plt.title(parameters['title']+'Cumulative Line'+' $\mu='+str(round(mu,2))+'$, $\sigma='+str(round(sigma,2))+'$')
    if 'ylabel' in parameters.keys():
        plt.ylabel(parameters['ylabel'])

        # defining num_bin, normed, facecolor, alpha
    if 'num_bin' in parameters.keys():
        num_bin = int(parameters['num_bin'])
    
    param = ''

    colors = ['#BCD8E3', '#E0A295', '#75625E', '#7F9AA5', '#AFCDD8', '#E9CDA6', '#70B879', '#E8E098', '#898A82',
             '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F', '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',
             '#70B879', '#AAD9A5', '#8AC2BF']
    color = random.sample(colors, 1)

    if 'normed' in parameters.keys():
        param = param + ', normed='+ str(parameters['normed'])

    if 'color' in parameters.keys():
        param = param + ',color="' + str(parameters['color'])+'"'
    else:
        param = param + ',color="'+color[0]+'"'

    if 'alpha' in parameters.keys():
        param = param + ',alpha=' + str(parameters['alpha'])

	# Overlay a reversed cumulative histogram.
	exec("plt.hist(x, num_bin, histtype='step'"+param+", cumulative=-1)")

	plt.grid(True)
	plt.ylim(0, 1.05)

	savefig(output, format = 'svg')

#End