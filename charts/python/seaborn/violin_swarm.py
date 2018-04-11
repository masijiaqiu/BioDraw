"""
Author: Ziwei JIANG
Date:2016/9/16
Version:1.0
Discription:
"""

import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
from matplotlib.pyplot import savefig
import seaborn as sns
import pandas as pd



def violin_swarm(data, parameters, output):
    sns.set(style="whitegrid", color_codes=True)
    #data
    tips=pd.read_csv(data)
    #parameter
    x=''
    y=''
    hue=''
    title=''
    param=""
    inner=None
    if 'title' in parameters.keys():
        title=parameters['title']
    plt.title(title)
    if 'x' in parameters.keys():
    	x=parameters['x']
    if 'y' in parameters.keys():
    	y=parameters['y']
    if 'inner' in parameters.keys():
        inner=parameters['inner']
    if 'color' in parameters.keys():
        param=param+",color='"+parameters['color']+"'"
    if 'alpha' in parameters.keys():
        param=param+",alpha="+parameters['alpha']
    #draw
    sns.violinplot(x=x, y=y, data=tips, inner=inner)
    exec("sns.swarmplot(x=x, y=y, data=tips"+param+")");
    #save
    savefig(output,format='svg')