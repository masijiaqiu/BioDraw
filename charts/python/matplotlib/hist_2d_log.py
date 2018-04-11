
"""
Author: Yu Liujun
Date: 2016/11/09
Version: 1.0
Description:
"""
import csv
import random
import numpy as np
from numpy.random import beta
from matplotlib.pyplot import savefig
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
plt.rcdefaults()


def hist_2d_log(data, parameters, output):

	#data
	x = []
	y = []
	with open(data) as f:
		f_csv = csv.reader(f)
		headers = next(f_csv)
		#headers: list

		for row in f_csv:
			x.append(float(row[0]))
			y.append(float(row[1]))

	if 'xlabel' in parameters.keys():
		plt.xlabel(parameters['xlabel'])
	if 'ylabel' in parameters.keys():
		plt.ylabel(parameters['ylabel'])
	if 'title' in parameters.keys():
		plt.title(parameters['title']+' - 2D Histogram')

	param = ''
	
	number_of_bins = 40
	if 'number_of_bins' in parameters.keys():
		number_of_bins = int(parameters['number_of_bins'])
	param = param + ', bins = number_of_bins'

	plt.xlim = (np.max(x),np.min(x))
	plt.ylim = (np.max(y),np.min(y))
	exec("plt.hist2d(x,y"+param+",norm = LogNorm())")
	plt.colorbar()

	savefig(output, format = 'svg')

