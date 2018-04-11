"""
Author: Masijia QIU
Date: 2016/08/24
Version: 1.0
Description:
"""
import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
from matplotlib.pyplot import savefig
from matplotlib.patches import Ellipse
import matplotlib_venn

def myvenn2(data, parameters, output):
	#data
	subset_Ab = 0
	subset_aB = 0
	subset_AB = 0
	colorA = '#E8B601'
	colorB = '#7AC3B1'
	colorAB = '#6B7E23'
	with open(data) as f:
		f_csv = csv.reader(f)
		headers = next(f_csv)
		for row in f_csv:
			set_a = float(row[1])
			set_b = float(row[2])

			if set_a == 0 and set_b != 0:
				subset_aB += 1
			elif set_a != 0 and set_b == 0:
				subset_Ab += 1
			elif set_a != 0 and set_b != 0:
				subset_AB += 1

	fparam = ''
	if 'figsize' in parameters.keys():
		fparam = fparam + ',figsize=' + parameters['figsize']
	exec("fig = plt.figure(facecolor='w'" + fparam + ")")

	if 'title' in parameters.keys():
		plt.title(parameters['title'])

	if 'colorA' in parameters.keys():
		colorA = parameters['colorA']
	if 'colorB' in parameters.keys():
		colorB = parameters['colorB']
	if 'colorAB' in parameters.keys():
		colorAB = parameters['colorAB']

	v = matplotlib_venn.venn2(subsets=(subset_Ab, subset_aB, subset_AB), set_labels=headers[1:])

	v.get_patch_by_id('10').set_color(colorA)
	v.get_patch_by_id('01').set_color(colorB)
	v.get_patch_by_id('11').set_color(colorAB)

	v.get_patch_by_id('10').set_alpha(0.6)
	v.get_patch_by_id('01').set_alpha(0.6)
	v.get_patch_by_id('11').set_alpha(0.7)

	savefig(output, format='svg')


def myvenn3(data, parameters, output):
	#data
	subset_Abc = 0
	subset_aBc = 0
	subset_ABc = 0
	subset_abC = 0
	subset_AbC = 0
	subset_aBC = 0
	subset_ABC = 0
	colorA = '#E8B601'
	colorB = '#7AC3B1'
	colorC = '#E53135'
	colorAB = '#6B7E23'
	colorAC = '#E58E35'
	colorBC = '#A889AD'
	colorABC = '#9E8859'
	label = []
	with open(data) as f:
		f_csv = csv.reader(f)
		label = next(f_csv)[1:]
		for row in f_csv:
			set_a = float(row[1])
			set_b = float(row[2])
			set_c = float(row[3])

			if set_a != 0 and set_b == 0 and set_c == 0:
				subset_Abc += 1
			elif set_a == 0 and set_b != 0 and set_c == 0:
				subset_aBc += 1
			elif set_a != 0 and set_b != 0 and set_c == 0:
				subset_ABc += 1
			elif set_a == 0 and set_b == 0 and set_c != 0:
				subset_abC += 1
			elif set_a != 0 and set_b == 0 and set_c != 0:
				subset_AbC += 1
			elif set_a == 0 and set_b != 0 and set_c != 0:
				subset_aBC += 1
			elif set_a != 0 and set_b != 0 and set_c != 0:
				subset_ABC += 1

	fparam = ''
	if 'figsize' in parameters.keys():
		fparam = fparam + ',figsize=' + parameters['figsize']
	exec("fig = plt.figure(facecolor='w'" + fparam + ")")

	if 'title' in parameters.keys():
		plt.title(parameters['title'])

	if 'colorA' in parameters.keys():
		colorA = parameters['colorA']
	if 'colorB' in parameters.keys():
		colorB = parameters['colorB']
	if 'colorC' in parameters.keys():
		colorC = parameters['colorC']
	if 'colorAB' in parameters.keys():
		colorAB = parameters['colorAB']
	if 'colorAC' in parameters.keys():
		colorAC = parameters['colorAC']
	if 'colorBC' in parameters.keys():
		colorBC = parameters['colorBC']
	if 'colorABC' in parameters.keys():
		colorABC = parameters['colorABC']

	v = matplotlib_venn.venn3(subsets=(subset_Abc, subset_aBc, subset_ABc, subset_abC, subset_ABc, subset_aBC, subset_ABC), set_labels=label)

	v.get_patch_by_id('100').set_color(colorA)
	v.get_patch_by_id('010').set_color(colorB)
	v.get_patch_by_id('110').set_color(colorC)
	v.get_patch_by_id('001').set_color(colorAB)
	v.get_patch_by_id('101').set_color(colorAC)
	v.get_patch_by_id('011').set_color(colorBC)
	v.get_patch_by_id('111').set_color(colorABC)

	v.get_patch_by_id('100').set_alpha(0.6)
	v.get_patch_by_id('010').set_alpha(0.6)
	v.get_patch_by_id('110').set_alpha(0.6)
	v.get_patch_by_id('001').set_alpha(0.6)
	v.get_patch_by_id('101').set_alpha(0.6)
	v.get_patch_by_id('011').set_alpha(0.7)
	v.get_patch_by_id('111').set_alpha(0.6)

	savefig(output, format='svg')


def myvenn4(data, parameters, output):
	#data
	subset_A = 0
	subset_B = 0
	subset_C = 0
	subset_D = 0
	subset_AB = 0
	subset_AC = 0
	subset_AD = 0
	subset_BC = 0
	subset_BD = 0
	subset_CD = 0
	subset_BCD = 0
	subset_ACD = 0
	subset_ABD = 0
	subset_ABC = 0
	subset_ABCD = 0
	with open(data) as f:
		f_csv = csv.reader(f)
		label = next(f_csv)[1:]
		for row in f_csv:
			set_a = float(row[1])
			set_b = float(row[2])
			set_c = float(row[3])
			set_d = float(row[4])
			if set_a != 0 and set_b == 0 and set_c == 0 and set_d == 0:
				subset_A += 1
			elif set_a == 0 and set_b != 0 and set_c == 0 and set_d == 0:
				subset_B += 1
			elif set_a == 0 and set_b == 0 and set_c != 0 and set_d == 0:
				subset_C += 1
			elif set_a == 0 and set_b == 0 and set_c == 0 and set_d != 0:
				subset_D += 1
			elif set_a != 0 and set_b != 0 and set_c == 0 and set_d == 0:
				subset_AB += 1
			elif set_a != 0 and set_b == 0 and set_c != 0 and set_d == 0:
				subset_AC += 1
			elif set_a != 0 and set_b == 0 and set_c == 0 and set_d != 0:
				subset_AD += 1
			elif set_a == 0 and set_b != 0 and set_c != 0 and set_d == 0:
				subset_BC += 1
			elif set_a == 0 and set_b != 0 and set_c == 0 and set_d != 0:
				subset_BD += 1
			elif set_a == 0 and set_b == 0 and set_c != 0 and set_d != 0:
				subset_CD += 1
			elif set_a == 0 and set_b != 0 and set_c != 0 and set_d != 0:
				subset_BCD += 1
			elif set_a != 0 and set_b == 0 and set_c != 0 and set_d != 0:
				subset_ACD += 1
			elif set_a != 0 and set_b != 0 and set_c == 0 and set_d != 0:
				subset_ABD += 1
			elif set_a != 0 and set_b != 0 and set_c != 0 and set_d == 0:
				subset_ABC += 1
			elif set_a != 0 and set_b != 0 and set_c != 0 and set_d != 0:
				subset_ABCD += 1

	fparam = ''
	if 'figsize' in parameters.keys():
		fparam = fparam + ',figsize=' + parameters['figsize']
	exec("fig = plt.figure(facecolor='w'" + fparam + ")")

	if 'title' in parameters.keys():
		plt.title(parameters['title'])

	ax = fig.add_subplot(111)
	setA = Ellipse((1.4, 3.4), 4, 8, angle=50, facecolor='#E6D220', alpha=0.5, edgecolor='#E6D220')
	setB = Ellipse((3.2, 4.4), 4, 7, angle=40, color='#F05455', alpha=0.5)
	setC = Ellipse((3.8, 4.6), 4., 8, angle=140, color='#266191', alpha=0.4)
	setD = Ellipse((5.0, 3.1), 4.2, 8, angle=130, color='#27AB53', alpha=0.4)

	ax.add_patch(setA)
	ax.add_patch(setB)
	ax.add_patch(setC)
	ax.add_patch(setD)

	fig.text(0.2, 0.35, label[0], fontdict={'size': 20}, ha = 'right', )   # SAMPLE A
	fig.text(0.29, 0.78, label[1], fontdict={'size': 20}, ha = 'right', )  # SAMPLE B
	fig.text(0.7, 0.79, label[2], fontdict={'size': 20}, ha = 'left', )   # SAMPLE C
	fig.text(0.8, 0.5, label[3], fontdict={'size': 20}, ha = 'left', )   # SAMPLE D
	ax.text(-1.2, 4, str(subset_A), fontdict={'size': 15}, ha = 'left' )          # A
	ax.text(1.1, 6.5,str(subset_B), fontdict={'size': 15}, ha = 'left' )     # B
	ax.text(4, 7, str(subset_C), fontdict={'size': 15}, ha = 'left' )     # C
	ax.text(6.2, 4, str(subset_D), fontdict={'size': 15}, ha = 'left' )       # D
	ax.text(0.68, 5.3, str(subset_AB), fontdict={'size': 15}, ha = 'left' )       # AB
	ax.text(2.5, 5.6, str(subset_BC), fontdict={'size': 15}, ha = 'left' )        # BC
	ax.text(5.2, 5.4, str(subset_CD), fontdict={'size': 15}, ha = 'left' )        # CD
	ax.text(2.4, 0.8, str(subset_AD), fontdict={'size': 15}, ha = 'left' )        # AD
	ax.text(0.9, 2.5, str(subset_AC), fontdict={'size': 15}, ha = 'left' )        # AC
	ax.text(4.9, 2.4, str(subset_BD), fontdict={'size': 15}, ha = 'left' )        # BD
	ax.text(1.3, 4, str(subset_ABC), fontdict={'size': 15}, ha = 'left' )         # ABC
	ax.text(4.1, 4, str(subset_BCD), fontdict={'size': 15}, ha = 'left' )         # BCD
	ax.text(4.1, 1.6, str(subset_ABD), fontdict={'size': 15}, ha = 'center' )         # ABD
	ax.text(1.7, 1.5, str(subset_ACD), fontdict={'size': 15}, ha = 'left' )           # ACD
	ax.text(3.2, 2.8, str(subset_ABCD), fontdict={'size': 15}, ha = 'center' )           # ABCD

	plt.axis('off')
	ax.set_xlim(-2, 10)
	ax.set_ylim(0, 8)

	savefig(output, format='svg')
