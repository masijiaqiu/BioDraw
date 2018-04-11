"""
Author: Masijia Qiu
Date: 2016/08/24
Version: 1.0
Description:
"""
import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
from matplotlib.pyplot import savefig
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

fig=plt.figure()
ax=fig.gca(projection='3d')

def contour3d(data, parameters, output):
    # data
    x = []
    y = []
    z = []
    with open(data) as f:
    	f_csv = csv.reader(f)
    	headers = next(f_csv)
    	for row in f_csv:
    	    x.append(float(row[0]))
    	    y.append(float(row[1]))
    	    z.append(float(row[2]))
	
	xmax=max(x);xmin=min(x)
	ymax=max(y);ymin=min(y)
	zmax=max(z);zmin=min(z)
	x = np.asarray(x)
	y = np.asarray(y)
	z = np.asarray(z)
	cols = np.unique(x).shape[0]
	X = x.reshape(cols,cols)
	Y = y.reshape(cols,cols)
	Z = z.reshape(cols,cols)
	
    # parameters
    if 'xlabel' in parameters.keys():
        ax.set_xlabel(parameters['xlabel'])
    if 'title' in parameters.keys():
        ax.set_title(parameters['title'])
    if 'ylabel' in parameters.keys():
        ax.set_ylabel(parameters['ylabel'])
    if 'zlabel' in parameters.keys():
        ax.set_zlabel(parameters['zlabel'])
	
	ax.set_xlim(xmin,xmax)
	ax.set_ylim(ymin,ymax)
	ax.set_zlim(zmin,zmax)
	
    param = ''
    if 'rstride' in parameters.keys():
        param = param + ',rstride=' + str(parameters['rstride'])
    if 'cstride' in parameters.keys():
        param = param + ',cstride=' + str(parameters['cstride'])
    if 'alpha' in parameters.keys():
        param = param + ',alpha=' + str(parameters['alpha'])
    if 'color' in parameters.keys():
        param = param + ',color="' + parameters['color'] + '"'

    # draw
    exec("ax.plot_surface(X,Y,Z"+param+")")
    exec("ax.contour(X,Y,Z, zdir='x',offset=xmin,cmap=cm.coolwarm)")
    exec("ax.contour(X,Y,Z, zdir='y',offset=ymax,cmap=cm.coolwarm)")
    exec("ax.contour(X,Y,Z, zdir='z',offset=zmin,cmap=cm.coolwarm)")
	
    savefig(output, format='svg')