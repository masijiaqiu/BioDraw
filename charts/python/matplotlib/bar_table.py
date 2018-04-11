"""
Author: Yu Liujun
Date: 2016/09/12
Version: 1.0
Description:
"""
import csv
import random
import numpy as np
from numpy.random import beta
from matplotlib.pyplot import savefig
import matplotlib.pyplot as plt
plt.rcdefaults()
"""
Demo of table function to display a table within a plot.
"""
import numpy as np
import matplotlib.pyplot as plt

def bar_table(data, parameters, output):

    # data
    
    x = []
    n = 0
    column_names = []
    row_names = []
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        #headers is the list of data categories
        row_names = headers[1:len(headers)]

        #input array number
        n = len(headers)
        i = 1
        while (i < n):
            x.append([])
            i += 1
        #x[0] is the title of the group of numbers
        #others are the data of each group
        #every column is of one kind
        #y values are the counter of the total
        #each column is divided in to groups
        #each color represents a different group

        for row in f_csv:
            column_names.append(str(row[0]))
            i = 1
            while (i < n):
                x[i-1].append(float(row[i]))
                i = i+1
    
    #count of the total of columns and the total of rows
    row_number = len(x)
    column_number = len(column_names)
    #the bar width is originally set to 0.4
    bar_width = 0.4


    #parameters
    if 'title' in parameters.keys():
        plt.title(parameters['title']+' - Bar Chart with Table')
    if 'ylabel' in parameters.keys():
        plt.ylabel(parameters['ylabel'])

    colors = ['#BCD8E3', '#E0A295', '#75625E', '#7F9AA5', '#AFCDD8', '#E9CDA6', '#70B879', '#E8E098', '#898A82',
             '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F', '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',
             '#70B879', '#AAD9A5', '#8AC2BF']
    color = random.sample(colors, row_number)

    if 'color' in parameters.keys():
        exec("color=" + str(parameters['color']))
    if 'bar_width' in parameters.keys():
    	bar_width = parameters['bar_width']

    #setting the index position
    index = np.arange(column_number)
    #determining the bottom starting point of the bar chart of each color section
    bottoms = np.array([0.0] * len(column_names))

	# Plot bars and create text labels for the table
    cell_text = []
    #text to be generated in the column
    for row in range(row_number):
    	plt.bar(index, x[row], width = bar_width, bottom=bottoms, color=color[row],align = "center")
    	bottoms += x[row]
    	cell_text.append([q for q in x[row]])

	# Reverse colors and text labels to display the last value at the top.
    colors = colors[::-1]
	# Add a table at the bottom of the axes
    the_table = plt.table(cellText=cell_text,
    					  rowLabels = row_names,
                          rowColours=color,
                          colLabels=column_names,
                          loc='bottom')

	# Adjust layout to make room for the table:
    plt.subplots_adjust(left=0.2, bottom=0.2)
    plt.xticks([])


    savefig(output, format = 'svg')




