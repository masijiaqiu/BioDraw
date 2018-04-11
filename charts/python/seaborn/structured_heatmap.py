"""
Discovering structure in heatmap data
=====================================

_thumb: .4, .2
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

# parameters = {
#   'title': 'structured heatmap demo'
# }
def structured_heatmap(input_data, parameters, output):
    sns.set(font="monospace")
    df = pd.read_csv(input_data,header=[0, 1, 2], index_col=0)
    networks = []
    with open(input_data) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            for i in range(1, len(row)):
                if int(row[i]) not in networks:
                    networks.append(int(row[i]))
            break
    f.close()

    network_pal = sns.cubehelix_palette(len(networks),
                                        light=.9, dark=.1, reverse=True,
                                        start=1, rot=-2)
    network_lut = dict(zip(map(str, networks), network_pal))

    # Convert the palette to vectors that will be drawn on the side of the matrix
    networks = df.columns.get_level_values("network")
    network_colors = pd.Series(networks, index=df.columns).map(network_lut)

    # Create a custom colormap for the heatmap values
    cmap = sns.diverging_palette(h_neg=210, h_pos=350, s=90, l=30, as_cmap=True)

    # Draw the full plot
    sns.clustermap(df.corr(), row_colors=network_colors, linewidths=.5,
                   col_colors=network_colors, figsize=(13, 13), cmap=cmap)
    sns.plt.suptitle(parameters['title'])
    sns.plt.savefig(output,format='svg')
