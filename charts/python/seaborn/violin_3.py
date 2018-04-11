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



def violin_3(data, parameters, output):
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
    plt.title(title)
    if 'x' in parameters.keys():
    	x=parameters['x']
    if 'y' in parameters.keys():
    	y=parameters['y']
    if 'hue' in parameters.keys():
    	hue=parameters['hue']
    if 'palette' in parameters.keys():
    	param=param+",palette='"+parameters['palette']+"'"
    if 'scale' in parameters.keys():
    	param=param+",scale='"+parameters['scale']+"'"
    #draw
    exec("sns.violinplot(x=x, y=y,hue=hue,data=tips,split=True"+param+")")
    #save
    savefig(output,format='svg')