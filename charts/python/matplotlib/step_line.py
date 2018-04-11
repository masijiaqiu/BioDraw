"""
Author: Yu Liujun
Date: 2016/09/06
Version: 1.0
Description:
"""
import numpy as np
from numpy import ma
import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
from matplotlib.pyplot import savefig
import random

def step_line(data, parameters, output):
	# data
    y = []
    n = 0

    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        #headers: list

        #input array number
        n = len(headers)
        i = 0
        while (i < n):
            y.append([])
            i += 1

        for row in f_csv:
            i = 0
            while (i < n):
                y[i].append(float(row[i]))
                i = i+1

    #set the starting point and ending point
    s = []
    e = []
    figsize = (12,8)
    exec('s =' + str(parameters['startingpoint']))
    exec('e =' + str(parameters['endpoint']))

    colors = ['#BCD8E3', '#E0A295', '#75625E', '#7F9AA5', '#AFCDD8', '#E9CDA6', '#70B879', '#E8E098', '#898A82',
             '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F', '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',
             '#70B879', '#AAD9A5', '#8AC2BF']
    color = random.sample(colors, len(y))

    if 'figsize' in parameters.keys():
        figsize = eval(parameters['figsize'])
    fig = plt.figure(facecolor='w', figsize=figsize)

    if 'color' in parameters.keys():
    	exec('color=' + str(parameters['color']))
    # parameters
    if 'title' in parameters.keys():
        plt.title(parameters['title']+' - Step')
    if 'xlabel' in parameters.keys():
        plt.xlabel(parameters['xlabel'])
    if 'ylabel' in parameters.keys():
        plt.ylabel(parameters['ylabel'])
    _where = 'pre'
    if 'where' in parameters.keys():
        _where = parameters['where']


	x = []
	i=0
	"""
	print len(y)
	"""
	while i < len(y):
		linespace = float((e[i]-s[i])/float(len(y[i])))
		a = np.arange(s[i], e[i], linespace)
		x.append(a.copy())
		plt.step(x[i], y[i],where = _where, label = headers[i], color = color[i])
		"""
		print len(x[i])
		print "and"
		print len(y[i])
		"""
		i+=1
	"""
	plt.step(x, y[0], label='pre (default)')
	"""
	"""
	y -= 0.5
	plt.step(x, y, where='mid', label='mid')

	y -= 0.5
	plt.step(x, y, where='post', label='post')

	y = ma.masked_where((y0 > -0.15) & (y0 < 0.15), y - 0.5)
	plt.step(x, y, label='masked (pre)')
	"""
    if 'legend' in parameters.keys():
        if parameters['legend'] == "True":
	        plt.legend()

	plt.xlim((np.min(s)-0.5),np.max(e)+0.5)
	plt.ylim(np.min(y)-0.5, np.max(y)+0.5)

	savefig(output, format = "svg")

#End




