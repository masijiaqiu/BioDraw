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

def box_color(data, parameters, output):

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
    medianprops=dict(linestyle='--',linewidth='2',color='black')
    boxprops=dict(linestyle='--',linewidth='2',color='black')

    colors = ['#BCD8E3', '#E0A295', '#75625E', '#7F9AA5', '#AFCDD8', '#E9CDA6', '#70B879', '#E8E098', '#898A82',
             '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F', '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',
             '#70B879', '#AAD9A5', '#8AC2BF']
    #color = random.sample(colors, examples)

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
    if 'showmedian' in parameters.keys():
        param=param+',showmedian='+str(parameters['showmedian'])
    if 'showcaps' in parameters.keys():
        param=param+',showcaps='+str(parameters['showcaps'])
    if 'vert' in parameters.keys():
        param=param+',vert='+str(parameters['vert'])
    if 'patch_artist' in parameters.keys():
        param=param+',patch_artist='+str(parameters['patch_artist'])
    if 'meanline' in parameters.keys():
        param=param+',meanline='+str(parameters['meanline'])
    if 'showbox' in parameters.keys():
        param=param+',showbox='+str(parameters['showbox'])
    if 'box_linestyle' in parameters.keys():
        boxprops['linestyle']=parameters['box_linestyle']
    if 'box_linewidth' in parameters.keys():
        boxprops['linewidth']=parameters['box_linewidth']
    if 'box_color' in parameters.keys():
        boxprops['color']=parameters['box_color']
    if 'median_linestyle' in parameters.keys():
        medianprops['linestyle']=parameters['median_linestyle']
    if 'median_linewidth' in parameters.keys():
        medianprops['linewidth']=parameters['median_linewidth']
    if 'median_color' in parameters.keys():
        medianprops['color']=parameters['median_color']
    param=param+',boxprops='+str(boxprops)
    param=param+',medianprops='+str(medianprops)

    # plot violin plot
    exec("bplot=plt.boxplot(all_data"+param+")")
    # adding horizontal grid lines
    plt.grid(True)

    #fill
    for patch,color in zip(bplot['boxes'],colors):
        patch.set_facecolor(color)
        
    # add x-tick labels
    plt.xticks(np.arange(len(all_data))+1,pos)

    savefig(output,format='svg')
