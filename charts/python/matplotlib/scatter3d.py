'''
==============
title: 3D scatterplot
==============

Description: Demonstration of a basic scatterplot in 3D.
'''
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv


# parameters = {
#     'title': 'The Example Graph of 3D scatterplot',
#     'format': {
#         'Group1': {'color': 'r', 'marker': 'o'},
#         'Group2': {'color': 'b', 'marker': '^'}
#     },
#     'x-label': 'X Label',
#     'y-label': 'Y Label',
#     'z-label': 'Z Label'
# }
def scatter3d(input_data, parameters, output):
    data = {}
    with open(input_data) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            group = row[0]
            if group in data:
                for index in range(0, len(row)-1):
                    data[group][index].append(float(row[index+1]))
            else:
                data[group] = []
                for index in range(0, len(row)-1):
                    data[group].append([float(row[index+1])])
    f.close()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')


    for group in data:
        ax.scatter(data[group][0], data[group][1], data[group][2], c=parameters['format'][group]['color'], marker=parameters['format'][group]['marker'], label=group)

    ax.set_xlabel(parameters['x-label'])
    ax.set_ylabel(parameters['y-label'])
    ax.set_zlabel(parameters['z-label'])
    ax.set_title(parameters['title'])
    plt.legend(loc='upper left', numpoints=1, ncol=3, fontsize=8, bbox_to_anchor=(0, 0))
    plt.savefig(output,format='svg')

