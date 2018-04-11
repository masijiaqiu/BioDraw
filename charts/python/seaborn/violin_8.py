"""
Author: Ziwei JIANG
Date:2016/9/12
Version:1.0
Discription:
"""

import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
from matplotlib.pyplot import savefig
import seaborn as sns
import pandas as pd



def violin_8(data, parameters, output):
	#data
    tips=pd.read_csv(data)
    #parameter
    x=''
    y=''
    hue=''
    param=""
    title=''
    if 'title' in parameters.keys():
        title=parameters['title']

    if 'x' in parameters.keys():
    	x=parameters['x']
    if 'y' in parameters.keys():
    	y=parameters['y']
    if 'hue' in parameters.keys():
    	hue=parameters['hue']
    #draw
    sns.set_style("whitegrid")
    g = sns.FacetGrid(tips, col="time", size=4, aspect=.7)
    g.map(sns.violinplot, x, y, hue, split=True).despine(left=True).add_legend(title=hue)

    savefig(output,format='svg')