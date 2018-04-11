"""
Author: Ziwei JIANG
Date:2016/8/30
Version:1.0
Discription:
"""

import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig

def violinh(data, parameters, output):
    
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
    figsize=(6,10)
    param=" "

    if 'figsize' in parameters.keys():
        figsize = eval(parameters['figsize'])
    fig = plt.figure(facecolor='w', figsize=figsize)
    if 'xlabel' in parameters.keys():
        plt.xlabel(parameters['xlabel'])
    if 'title' in parameters.keys():
        plt.title(parameters['title'])
    if 'ylabel' in parameters.keys():
        plt.ylabel(parameters['ylabel'])
    if 'widths' in parameters.keys():
        param=param+',widths='+str(parameters['widths'])
    if 'points' in parameters.keys():
        param=param+',points='+str(parameters['points'])
    if 'showmeans' in parameters.keys():
        param=param+',showmeans='+str(parameters['showmeans'])
    if 'showextrema' in parameters.keys():
        param=param+',showextrema='+str(parameters['showextrema'])
    if 'showmedians' in parameters.keys():
        param=param+',showmedians='+str(parameters['showmedians'])
   
    #add grid lines
    plt.grid(True)

    # plot violin plot
    exec("plt.violinplot(all_data,vert=False"+ param+")")

    # add y-tick labels
    plt.yticks(np.arange(len(all_data))+1,pos)


    savefig(output,format='svg')
