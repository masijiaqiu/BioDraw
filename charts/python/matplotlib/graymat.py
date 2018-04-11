"""
Author: Ziwei JIANG
Date: 2016/09/08
Version: 1.0
Description:
"""
import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
from matplotlib.pyplot import savefig
import random


def graymat(data, parameters, output):
	#data
    all_data=[]
    with open(data) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            all_data.append(map(float,row[:]))
    #parameter
    fignum=100
    if 'fignum' in parameters.keys():
        fignum=int(parameters['fignum'])



	plt.matshow(all_data, fignum=fignum, cmap=plt.cm.gray)

	savefig(output,format='svg')
