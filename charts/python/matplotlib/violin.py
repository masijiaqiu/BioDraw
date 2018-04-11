"""
Author: Ziwei JIANG
Date:2016/8/21
Version:1.0
Discription:
"""

import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
from matplotlib.pyplot import savefig

def violin(data, parameters, output):

    # data
    all_data=[]
    pos=[]
    with open(data) as f:
        f_csv=csv.reader(f)
        header=next(f_csv)
        count=len(header)
        pos=header[1:]
        for row in f_csv:
            all_data.append(map(float,row[1:count]))
        all_data=map(list,zip(*all_data))

     # parameters
    figsize=(8,5)
    if 'figsize' in parameters.keys():
        figsize = eval(parameters['figsize'])
    fig = plt.figure(facecolor='w', figsize=figsize)
    if 'xlabel' in parameters.keys():
        plt.xlabel(parameters['xlabel'])
    if 'title' in parameters.keys():
        plt.title(parameters['title'])
    if 'ylabel' in parameters.keys():
        plt.ylabel(parameters['ylabel'])

    param=" "
    if 'showmeans' in parameters.keys():
        param=param+',showmeans='+str(parameters['showmeans'])
    if 'showmedians' in parameters.keys():
        param=param+',showmedians='+str(parameters['showmedians'])
    if 'widths' in parameters.keys():
        param=param+',widths='+str(parameters['widths'])
    if 'points' in parameters.keys():
        param=param+',points='+str(parameters['points'])

   
    # plot violin plot
    exec("plt.violinplot(all_data"+param+")")
    # adding horizontal grid lines
    plt.grid(True)

    # add x-tick labels
    plt.xticks(np.arange(len(all_data))+1,pos)

    savefig(output,format='svg')
