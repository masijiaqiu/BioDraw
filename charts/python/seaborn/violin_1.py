"""
Author: Ziwei JIANG
Date:2016/9/12
Version:1.0
Discription:
"""

import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
import seaborn as sns
import pandas as pd



def violin_1(data, parameters, output):
    #data
    tips=pd.read_csv(data)
    #parameter
    x=''
    y=''
    hue=''
    title=''
    if 'title' in parameters.keys():
        title=parameters['title']
    plt.title(title)
    if 'x' in parameters.keys():
    	x=parameters['x']
    if 'y' in parameters.keys():
    	y=parameters['y']
    if 'hue' in parameters.keys():
    	hue=parameters['hue']
    #draw
    ax = sns.violinplot(x=x, y=y,hue=hue,data=tips)
    #save
    savefig(output,format='svg')