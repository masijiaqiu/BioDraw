"""
Author: Ziwei JIANG
Date:2016/9/5
Version:1.0
Discription:
"""

import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
from matplotlib.pyplot import savefig

def barcode(data, parameters, output):
    #data
    all_data=[]
    with open(data) as f:
        f_csv=csv.reader(f)
        for row in f_csv:
        	for a in range(len(row)):
        		all_data.append(int(row[a]))

    x=np.array(all_data)

    axprops = dict(xticks=[], yticks=[])
    barprops = dict(aspect='auto', cmap=plt.cm.binary, interpolation='nearest')

    #parameter
    if 'title' in parameters.keys():
        title=parameters['title']


    #draw
    fig = plt.figure()

	# a horizontal barcode
    x.shape = 1, len(x)
    ax = fig.add_axes([0.3, 0.4, 0.6, 0.1], **axprops)
    ax.set_title(title)
    plt.imshow(x, **barprops)

    savefig(output,format='svg')
