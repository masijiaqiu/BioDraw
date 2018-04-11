"""
Author: Masijia Qiu
Date: 2016/09/01
Version: 1.0
Description:
"""
import csv
import math
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.pyplot import savefig

def radar_factory(num_vars, frame='circle'):
    theta = np.linspace(0, 2*np.pi, num_vars, endpoint=False)
    theta += np.pi/2

    def draw_poly_patch(self):
        verts = unit_poly_verts(theta)
        return plt.Polygon(verts, closed=True, edgecolor='k')

    def draw_circle_patch(self):
        return plt.Circle((0.5, 0.5), 0.5)

    patch_dict = {'polygon': draw_poly_patch, 'circle': draw_circle_patch}
    if frame not in patch_dict:
        raise ValueError('unknown value for `frame`: %s' % frame)

    class RadarAxes(PolarAxes):

        name = 'radar'
        RESOLUTION = 1
        draw_patch = patch_dict[frame]

        def fill(self, *args, **kwargs):
            closed = kwargs.pop('closed', True)
            return super(RadarAxes, self).fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            lines = super(RadarAxes, self).plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            
            if x[0] != x[-1]:
                x = np.concatenate((x, [x[0]]))
                y = np.concatenate((y, [y[0]]))
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(np.degrees(theta), labels)

        def _gen_axes_patch(self):
            return self.draw_patch()

        def _gen_axes_spines(self):
            if frame == 'circle':
                return PolarAxes._gen_axes_spines(self)
                
            spine_type = 'circle'
            verts = unit_poly_verts(theta)
            
            verts.append(verts[0])
            path = Path(verts)

            spine = Spine(self, spine_type, path)
            spine.set_transform(self.transAxes)
            return {'polar': spine}

    register_projection(RadarAxes)
    return theta


def unit_poly_verts(theta):
    x0, y0, r = [0.5] * 3
    verts = [(r*np.cos(t) + x0, r*np.sin(t) + y0) for t in theta]
    return verts

def radar1(data, parameters, output):
    # data
    p = []
    x = []
    cols = 0
    labels = []
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        cols = len(headers)
        labels = headers[1:cols]
        labels = tuple(labels)
        for row in f_csv:
            if row[0] not in p:
                p.append(row[0])
            for i in range(1,cols):
                x.append(float(row[i]))


    # parameters
    title = ''
    if 'title' in parameters.keys():
        title = parameters['title']
    _alpha = 0.5
    if 'alpha' in parameters.keys():
        _alpha = parameters['alpha']
    _figsize = (9,9)
    if 'figsize' in parameters.keys():
        _figsize = eval(parameters['figsize'])
    colors = ['b','r','g','m']
    if 'colors' in parameters.keys():
        colors = eval(parameters['colors'])
    _frame = 'polygon'
    if 'frame' in parameters.keys():
        _frame = parameters['frame']
        
    N1 = len(p)
    N2 = cols-1
    theta = radar_factory(N2,frame=_frame)
    
    rmin = math.ceil(max(x))/5
    rgrid = [rmin,rmin*2,rmin*3,rmin*4,rmin*5]
    x = np.asarray(x)
    x = x.reshape(N1,N2)
    
    # draw
    fig = plt.figure(figsize=_figsize)
    fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.85, bottom=0.05)
    
    ax = fig.add_subplot(111,projection='radar')
    for d,color in zip(x,colors):
        ax.plot(theta,d,color=color)
        ax.fill(theta,d,facecolor=color,alpha=_alpha)
    plt.rgrids(rgrid)
    ax.set_varlabels(labels)
    
    plt.subplot(111)
    legend = plt.legend(p, loc=(0.9, .95), labelspacing=0.1)
    plt.setp(legend.get_texts(), fontsize='small')

    plt.figtext(0.5, 0.965, title,
                ha='center', color='black', weight='bold', size='large')
    
    savefig(output, format='svg')

def radar2(data, parameters, output):
    # data
    p1 = []
    p2 = []
    x = []
    cols = 0
    labels = []
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        cols = len(headers)
        labels = headers[2:cols]
        labels = tuple(labels)
        for row in f_csv:
            if row[0] not in p1:
                p1.append(row[0])
            if row[1] not in p2:
                p2.append(row[1])
            for i in range(2,cols):
                x.append(float(row[i]))


    # parameters
    title = ''
    if 'title' in parameters.keys():
        title = parameters['title']
    _alpha = 0.5
    if 'alpha' in parameters.keys():
        _alpha = parameters['alpha']
    _figsize = (9,9)
    if 'figsize' in parameters.keys():
        _figsize = eval(parameters['figsize'])
    colors = ['b','r','g','m']
    if 'colors' in parameters.keys():
        colors = eval(parameters['colors'])
    _frame = 'polygon'
    if 'frame' in parameters.keys():
        _frame = parameters['frame']
        
    N1 = len(p1)
    N2 = len(p2)
    N3 = cols-2
    theta = radar_factory(N3,frame=_frame)
    
    rmin = math.ceil(max(x))/5
    rgrid = [rmin,rmin*2,rmin*3,rmin*4,rmin*5]
    x = np.asarray(x)
    x = x.reshape(N1,N2,N3)
    
    # draw
    fig = plt.figure(figsize=_figsize)
    fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.95, bottom=0.35)
    
    for i in range(0,N1):
        ax = fig.add_subplot(1,2,i+1,projection='radar')
        ax.set_title(p1[i], weight='bold', size='medium', position=(0.5, 1.1),
                     horizontalalignment='center', verticalalignment='center')
        for d,color in zip(x[i],colors):
            ax.plot(theta,d,color=color)
            ax.fill(theta,d,facecolor=color,alpha=_alpha)
        plt.rgrids(rgrid)
        ax.set_varlabels(labels)
    
    plt.subplot(1, 2, 1)
    legend = plt.legend(p2, loc=(0.9, .95), labelspacing=0.1)
    plt.setp(legend.get_texts(), fontsize='small')

    plt.figtext(0.5, 0.965, title,
                ha='center', color='black', weight='bold', size='large')
    
    savefig(output, format='svg')

def radar4(data, parameters, output):
    # data
    p1 = []
    p2 = []
    x = []
    cols = 0
    labels = []
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        cols = len(headers)
        labels = headers[2:cols]
        labels = tuple(labels)
        for row in f_csv:
            if row[0] not in p1:
                p1.append(row[0])
            if row[1] not in p2:
                p2.append(row[1])
            for i in range(2,cols):
                x.append(float(row[i]))

    # parameters
    title = ''
    if 'title' in parameters.keys():
        title = parameters['title']
    _alpha = 0.5
    if 'alpha' in parameters.keys():
        _alpha = parameters['alpha']
    _figsize = (9,9)
    if 'figsize' in parameters.keys():
        _figsize = eval(parameters['figsize'])
    colors = ['b','r','g','m']
    if 'colors' in parameters.keys():
        colors = eval(parameters['colors'])
    _frame = 'polygon'
    if 'frame' in parameters.keys():
        _frame = parameters['frame']
        
    N1 = len(p1)
    N2 = len(p2)
    N3 = cols-2
    theta = radar_factory(N3,frame=_frame)
    
    rmin = math.ceil(max(x))/5
    rgrid = [rmin,rmin*2,rmin*3,rmin*4,rmin*5]
    x = np.asarray(x)
    x = x.reshape(N1,N2,N3)
    
    # draw
    fig = plt.figure(figsize=_figsize)
    fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.85, bottom=0.05)
    
    for i in range(0,N1):
        ax = fig.add_subplot(2,2,i+1,projection='radar')
        ax.set_title(p1[i], weight='bold', size='medium', position=(0.5, 1.1),
                     horizontalalignment='center', verticalalignment='center')
        for d,color in zip(x[i],colors):
            ax.plot(theta,d,color=color)
            ax.fill(theta,d,facecolor=color,alpha=_alpha)
        plt.rgrids(rgrid)
        ax.set_varlabels(labels)
    
    plt.subplot(2, 2, 1)
    legend = plt.legend(p2, loc=(0.9, .95), labelspacing=0.1)
    plt.setp(legend.get_texts(), fontsize='small')

    plt.figtext(0.5, 0.965, title,
                ha='center', color='black', weight='bold', size='large')
    
    savefig(output, format='svg')

def radarline1(data, parameters, output):
    # data
    p = []
    x = []
    cols = 0
    labels = []
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        cols = len(headers)
        labels = headers[1:cols]
        labels = tuple(labels)
        for row in f_csv:
            if row[0] not in p:
                p.append(row[0])
            for i in range(1,cols):
                x.append(float(row[i]))


    # parameters
    title = ''
    if 'title' in parameters.keys():
        title = parameters['title']
    _alpha = 0.5
    if 'alpha' in parameters.keys():
        _alpha = parameters['alpha']
    _figsize = (9,9)
    if 'figsize' in parameters.keys():
        _figsize = eval(parameters['figsize'])
    colors = ['b','r','g','m']
    if 'colors' in parameters.keys():
        colors = eval(parameters['colors'])
    _frame = 'polygon'
    if 'frame' in parameters.keys():
        _frame = parameters['frame']
    _linewidth = 2
    if 'linewidth' in parameters.keys():
        _linewidth = float(parameters['linewidth'])
        
    N1 = len(p)
    N2 = cols-1
    theta = radar_factory(N2,frame=_frame)
    
    rmin = math.ceil(max(x))/5
    rgrid = [rmin,rmin*2,rmin*3,rmin*4,rmin*5]
    x = np.asarray(x)
    x = x.reshape(N1,N2)
    
    # draw
    fig = plt.figure(figsize=_figsize)
    fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.85, bottom=0.05)
    
    ax = fig.add_subplot(111,projection='radar')
    for d,color in zip(x,colors):
        ax.plot(theta,d,color=color, linewidth=_linewidth)
    plt.rgrids(rgrid)
    ax.set_varlabels(labels)
    
    plt.subplot(111)
    legend = plt.legend(p, loc=(0.9, .95), labelspacing=0.1)
    plt.setp(legend.get_texts(), fontsize='small')

    plt.figtext(0.5, 0.965, title,
                ha='center', color='black', weight='bold', size='large')
    
    savefig(output, format='svg')

def radarline2(data, parameters, output):
    # data
    p1 = []
    p2 = []
    x = []
    cols = 0
    labels = []
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        cols = len(headers)
        labels = headers[2:cols]
        labels = tuple(labels)
        for row in f_csv:
            if row[0] not in p1:
                p1.append(row[0])
            if row[1] not in p2:
                p2.append(row[1])
            for i in range(2,cols):
                x.append(float(row[i]))


    # parameters
    title = ''
    if 'title' in parameters.keys():
        title = parameters['title']
    _alpha = 0.5
    if 'alpha' in parameters.keys():
        _alpha = parameters['alpha']
    _figsize = (9,9)
    if 'figsize' in parameters.keys():
        _figsize = eval(parameters['figsize'])
    colors = ['b','r','g','m']
    if 'colors' in parameters.keys():
        colors = eval(parameters['colors'])
    _frame = 'polygon'
    if 'frame' in parameters.keys():
        _frame = parameters['frame']
    _linewidth = 2
    if 'linewidth' in parameters.keys():
        _linewidth = float(parameters['linewidth'])
        
    N1 = len(p1)
    N2 = len(p2)
    N3 = cols-2
    theta = radar_factory(N3,frame=_frame)
    
    rmin = math.ceil(max(x))/5
    rgrid = [rmin,rmin*2,rmin*3,rmin*4,rmin*5]
    x = np.asarray(x)
    x = x.reshape(N1,N2,N3)
    
    # draw
    fig = plt.figure(figsize=_figsize)
    fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.95, bottom=0.35)
    
    for i in range(0,N1):
        ax = fig.add_subplot(1,2,i+1,projection='radar')
        ax.set_title(p1[i], weight='bold', size='medium', position=(0.5, 1.1),
                     horizontalalignment='center', verticalalignment='center')
        for d,color in zip(x[i],colors):
            ax.plot(theta,d,color=color, linewidth=_linewidth)
        plt.rgrids(rgrid)
        ax.set_varlabels(labels)
    
    plt.subplot(1, 2, 1)
    legend = plt.legend(p2, loc=(0.9, .95), labelspacing=0.1)
    plt.setp(legend.get_texts(), fontsize='small')

    plt.figtext(0.5, 0.965, title,
                ha='center', color='black', weight='bold', size='large')
    
    savefig(output, format='svg')

def radarline4(data, parameters, output):
    # data
    p1 = []
    p2 = []
    x = []
    cols = 0
    labels = []
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        cols = len(headers)
        labels = headers[2:cols]
        labels = tuple(labels)
        for row in f_csv:
            if row[0] not in p1:
                p1.append(row[0])
            if row[1] not in p2:
                p2.append(row[1])
            for i in range(2,cols):
                x.append(float(row[i]))

    # parameters
    title = ''
    if 'title' in parameters.keys():
        title = parameters['title']
    _alpha = 0.5
    if 'alpha' in parameters.keys():
        _alpha = parameters['alpha']
    _figsize = (9,9)
    if 'figsize' in parameters.keys():
        _figsize = eval(parameters['figsize'])
    colors = ['b','r','g','m']
    if 'colors' in parameters.keys():
        colors = eval(parameters['colors'])
    _frame = 'polygon'
    if 'frame' in parameters.keys():
        _frame = parameters['frame']
    _linewidth = 2
    if 'linewidth' in parameters.keys():
        _linewidth = float(parameters['linewidth'])
        
    N1 = len(p1)
    N2 = len(p2)
    N3 = cols-2
    theta = radar_factory(N3,frame=_frame)
    
    rmin = math.ceil(max(x))/5
    rgrid = [rmin,rmin*2,rmin*3,rmin*4,rmin*5]
    x = np.asarray(x)
    x = x.reshape(N1,N2,N3)
    
    # draw
    fig = plt.figure(figsize=_figsize)
    fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.85, bottom=0.05)
    
    for i in range(0,N1):
        ax = fig.add_subplot(2,2,i+1,projection='radar')
        ax.set_title(p1[i], weight='bold', size='medium', position=(0.5, 1.1),
                     horizontalalignment='center', verticalalignment='center')
        for d,color in zip(x[i],colors):
            ax.plot(theta,d,color=color,linewidth=_linewidth)
        plt.rgrids(rgrid)
        ax.set_varlabels(labels)
    
    plt.subplot(2, 2, 1)
    legend = plt.legend(p2, loc=(0.9, .95), labelspacing=0.1)
    plt.setp(legend.get_texts(), fontsize='small')

    plt.figtext(0.5, 0.965, title,
                ha='center', color='black', weight='bold', size='large')
    
    savefig(output, format='svg')
