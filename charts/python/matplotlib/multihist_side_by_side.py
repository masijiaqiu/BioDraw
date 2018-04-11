"""
Author: Yu Liujun
Date: 2016/09/06
Version: 1.0
Description:
"""
import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
from matplotlib.pyplot import savefig
import random

# An example of three data sets to compare


def multihist_side_by_side(data, parameters, output):
    
    # data
    x = []
    n = 0
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        #headers: list

        #input array number
        n = len(headers)
        i = 0
        while (i < n):
            x.append([])
            i += 1

        for row in f_csv:
            i = 0
            while (i < n):
                x[i].append(float(row[i]))
                i = i+1

    # Computed quantities to aid plotting
    hist_range = (np.min(x), np.max(x))
    
    # parameters
    number_of_bins = 20
    if 'xlabel' in parameters.keys():
        plt.xlabel(parameters['xlabel'])
    if 'ylabel' in parameters.keys():
        plt.ylabel(parameters['ylabel'])
    if 'title' in parameters.keys():
        plt.title(parameters['title']+' - Multiple Histograms Side By Side')
    
        # defining number_of_bins, normed, facecolor, alpha
    if 'number_of_bins' in parameters.keys():
        number_of_bins = int(parameters['number_of_bins'])

    param = ''
    labels = []

    colors = ['#BCD8E3', '#E0A295', '#75625E', '#7F9AA5', '#AFCDD8', '#E9CDA6', '#70B879', '#E8E098', '#898A82',
             '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F', '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',
             '#70B879', '#AAD9A5', '#8AC2BF']
    color = random.sample(colors, len(x))

    if 'normed' in parameters.keys():
        param = param + ', normed='+ str(parameters['normed'])

    if 'alpha' in parameters.keys():
        param = param + ',alpha=' + str(parameters['alpha'])

    if 'color' in parameters.keys():
        exec("color=[" + str(parameters['color'])+"]")

    # Computed quantities to aid plotting
    hr = (np.min(x), np.max(x)+1)
    binned_data_sets = [np.histogram(d, range=hr, bins=number_of_bins)[0] for d in x]
    binned_maximums = np.max(binned_data_sets,axis = 1)

    m = np.max(binned_maximums)

    x_locations = np.arange(.6*m, (n+0.6)*m, m)

    xlim = (0,(n+0.2)*m)
    ylim = ((hr[0]-(hr[1]-hr[0])/number_of_bins),(hr[1]+(hr[1]-hr[0])/number_of_bins))

    # The bin_edges are the same for all of the histograms
    bin_edges = np.linspace(hr[0], hr[1], number_of_bins + 1)
    bin_edges2 = np.roll(bin_edges,1)
    bin_edges2[0] = bin_edges[0]-((hr[1]-hr[0])/number_of_bins)
    """
    print np.roll(bin_edges, int(np.floor(np.min(x))))
    """

    centers = .5 * (bin_edges + bin_edges2)[:-1]
    """
    centers = .5 * (bin_edges + np.roll(bin_edges, int(np.floor(np.min(x)))))[:-1]
    """
    heights = np.diff(bin_edges)

    # Cycle through and plot each histogram

    ax = plt.subplot(1,1,1)
    d = zip(x_locations, binned_data_sets)
    d_length = len(d)
    i = 0
    while i < n :
        lefts = d[i][0] - .5 * d[i][1]
        ax.barh(centers, d[i][1], height=heights, left=lefts, color = color[i])
        i +=1
    

    ax.set_xticks(x_locations)
    ax.set_xticklabels(labels = headers)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

    savefig(output, format = 'svg')
    
#end