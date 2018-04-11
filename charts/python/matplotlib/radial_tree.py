#!/usr/bin/env python
"""
Routes to LANL from 186 sites on the Internet.

This uses Graphviz for layout so you need PyGraphviz or PyDotPlus.

"""
# Author: Aric Hagberg (hagberg@lanl.gov)

#    Copyright (C) 2004-2016
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.


import networkx as nx
import math
import pygraphviz
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
import csv 


# parameters = {
#     'title': 'radial tree'
# }

def radial_tree(input_data, parameters, output):
    G = nx.Graph()

    time = {}
    time[0] = 0 # assign 0 to center node
    with open(input_data) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            head = row[0]
            tail = row[1]
            rtt = row[2]
            G.add_edge(int(head), int(tail))
            time[int(head)] = float(rtt)
    f.close()
    # get largest component and assign ping times to G0time dictionary
    G0 = sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)[0]
    G0.rtt = {}
    for n in G0:
        G0.rtt[n] = time[n]

    plt.figure(figsize=(8, 8))
    # use graphviz to find radial layout
    pos = graphviz_layout(G0, prog="twopi", root=0)
    # draw nodes, coloring by rtt ping time
    nx.draw(G0, pos,
            node_color=[G0.rtt[v] for v in G0],
            with_labels=False,
            alpha=0.5,
            node_size=15)
    # adjust the plot limits
    xmax = 1.02 * max(xx for xx,yy in pos.values())
    ymax = 1.02 * max(yy for xx,yy in pos.values())
    plt.xlim(0, xmax)
    plt.ylim(0, ymax)
    plt.suptitle(parameters['title'])
    plt.savefig(output, format='svg')
