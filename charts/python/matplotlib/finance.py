"""
Author: Ziwei JIANG
Date: 2016/09/08
Version: 1.0
Description:
"""
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator,\
    DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc
import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
from matplotlib.pyplot import savefig
import random
from ast import literal_eval



def finance(data, parameters, output):
    #data
	# (Year, month, day) tuples suffice as args for quotes_historical_yahoo
    date1 = (2016, 8, 1)
    date2 = (2016, 9, 9)
    sticker=''

    with open(data) as f:
        f_csv=csv.reader(f)
        headers=next(f_csv)
        for row in f_csv:
            sticker=row[0]
            date1=literal_eval(row[1])
            date2=literal_eval(row[2])
    #parameters
    param=""
    figsize=(8,6)
    param1=""

    if 'figsize' in parameters.keys():
        figsize = eval(parameters['figsize'])
    fig, ax = plt.subplots(figsize=(11,5))
    if 'title' in parameters.keys():
        ax.set_title(parameters['title'])
    if 'witdth' in parameters.keys():
        param=param+",width="+str(parameters['width'])
    if 'colorup' in parameters.keys():
        param=param+",colorup='"+parameters['colorup']+"'"
    if 'colordown' in parameters.keys():
        param=param+",colordown='"+parameters['colordown']+"'"
    if 'rotation' in parameters.keys():
        param1=param1+",rotation="+str(parameters['rotation'])
    if 'horizontalalignment' in parameters.keys():
        param1=param1+",horizontalalignment='"+parameters['horizontalalignment']+"'"


    mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
    alldays = DayLocator()              	# minor ticks on the days
    weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
    dayFormatter = DateFormatter('%d')      # e.g., 12

    quotes = quotes_historical_yahoo_ohlc(sticker, date1, date2)
    if len(quotes) == 0:
        raise SystemExit

    fig.subplots_adjust(bottom=0.2)
    ax.xaxis.set_major_locator(mondays)
    ax.xaxis.set_minor_locator(alldays)
    ax.xaxis.set_major_formatter(weekFormatter)
    #ax.xaxis.set_minor_formatter(dayFormatter)

    #plot_day_summary(ax, quotes, ticksize=3)
    exec("candlestick_ohlc(ax, quotes, width=0.6"+param+")")

    ax.xaxis_date()
    ax.autoscale_view()
    exec("plt.setp(plt.gca().get_xticklabels()"+param1+")")

    # adding horizontal grid lines
    plt.grid(True,linestyle='--',linewidth=0.5)


    savefig(output,format='svg')




