"""
Author: Ziwei JIANG
Date: 2016/09/10
Version: 1.0
Description:
"""
import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
from matplotlib.pyplot import savefig
import random


def xcorr(data, parameters, output):
	#data
	x=[]
	y=[]
	with open(data) as f:
		f_csv=csv.reader(f)
		headers=next(f_csv)
		for row in f_csv:
			x.append(float(row[0]))
			y.append(float(row[1]))
	#parameters
	figsize=(8,6)
	param=""
	if 'figsize' in parameters.keys():
		figsize = eval(parameters['figsize'])
	fig=plt.figure(figsize=figsize)
	if 'xlabel' in parameters.keys():
		plt.xlabel(parameters['xlabel'])
	if 'title' in parameters.keys():
		plt.title(parameters['title'])
	if 'ylabel' in parameters.keys():
		plt.ylabel(parameters['ylabel'])
	if 'usevlines' in parameters.keys():
		param=param+",usevlines="+parameters['usevlines']
	if 'normed' in parameters.keys():
		param=param+",normed="+parameters['normed']
	if 'maxlags' in parameters.keys():
		param=param+",maxlags="+str(parameters['maxlags'])
	if 'lw' in parameters.keys():
		param=param+",lw="+str(parameters['lw'])
	if 'color' in parameters.keys():
		param=param+",color='"+parameters['color']+"'"
	exec("plt.xcorr(x, y"+param+")")

    # adding horizontal grid lines
	plt.grid(True,linestyle='--',linewidth=0.5)


	savefig(output,format='svg')