"""
Author: Ziwei JIANG
Date:2016/9/1
Version:1.0
Discription:
"""

import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
from matplotlib.pyplot import savefig

def box_flier(data, parameters, output):

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
    param=" "
    boxprops=dict(linestyle='--',linewidth='2',color='black')
    flierprops = dict(marker='o', markerfacecolor='green', markersize=12,linestyle='None',markeredgecolor='c')

    if 'figsize' in parameters.keys():
        figsize = eval(parameters['figsize'])
    fig = plt.figure(facecolor='w', figsize=figsize)
    if 'xlabel' in parameters.keys():
        plt.xlabel(parameters['xlabel'])
    if 'title' in parameters.keys():
        plt.title(parameters['title'])
    if 'ylabel' in parameters.keys():
        plt.ylabel(parameters['ylabel'])
    if 'whis' in parameters.keys():
        param=param+',whis='+str(parameters['whis'])
    if 'widths' in parameters.keys():
        param=param+',widths='+str(parameters['widths'])
    if 'showmeans' in parameters.keys():
        param=param+',showmeans='+str(parameters['showmeans'])
    if 'showcaps' in parameters.keys():
        param=param+',showcaps='+str(parameters['showcaps'])
    if 'vert' in parameters.keys():
        param=param+',vert='+str(parameters['vert'])
    if 'flier_marker' in parameters.keys():
        flierprops['marker']=parameters['flier_marker']
    if 'flier_markerfacecolor' in parameters.keys():
        flierprops['markerfacecolor']=parameters['flier_markerfacecolor']
    if 'flier_markeredgecolor' in parameters.keys():
        flierprops['markeredgecolor']=parameters['flier_markeredgecolor']
    if 'flier_markersize' in parameters.keys():
        flierprops['markersize']=parameters['flier_markersize']
    if 'flier_linestyle' in parameters.keys():
        flierprops['linestyle']=parameters['flier_linestyle']
    if 'box_linestyle' in parameters.keys():
        boxprops['linestyle']=parameters['box_linestyle']
    if 'box_linewidth' in parameters.keys():
        boxprops['linewidth']=parameters['box_linewidth']
    if 'box_color' in parameters.keys():
        boxprops['color']=parameters['box_color']
    param=param+',flierprops='+str(flierprops)
    param=param+',boxprops='+str(boxprops)

    # plot violin plot
    exec("bplot=plt.boxplot(all_data,showfliers='True'"+param+")")
    # adding horizontal grid lines
    plt.grid(True,linestyle='--',linewidth=0.5)

    # add x-tick labels
    plt.xticks(np.arange(len(all_data))+1,pos)

    savefig(output,format='svg')
