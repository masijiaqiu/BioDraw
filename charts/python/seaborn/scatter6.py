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



def scatter6(data, parameters, output):
    sns.set(style="whitegrid", color_codes=True)
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
    ax = sns.swarmplot(x="total_bill", y="day", hue="time", data=tips)
    #save
    savefig(output,format='svg')