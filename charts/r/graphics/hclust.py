"""
Author: Xu Zhang
Date: 2016/10/10
Version: 1.0
Description:
"""
import json
import os
from config.config import rscript_cmd
from config.config import r_tmp_file


def hclust(data, parameters, output):

    # parameters
    param = ''
    if 'hang' in parameters.keys():
        param = param + ',hang=' + str(parameters['hang'])
    #if param.strip().startswith(','):
    #    param = param[1:]

    try:
        os.system('touch ./charts/tmp.r')
        os.system('echo \'library("graphics")\' >> '+r_tmp_file)
        os.system('echo "input_data=read.csv(\''+ data +'\',header = T)" >>'+r_tmp_file)
        os.system('echo "hc = hclust(dist(input_data))" >> '+r_tmp_file)
        os.system('echo "svg(file=\''+output+'\')" >> '+r_tmp_file)
        os.system('echo "plot(hc'+param+')" >> '+r_tmp_file)
        os.system('echo "dev.off" >> '+r_tmp_file)
#        os.system('echo "dev.off()" >>'+r_tmp_file)
        os.system(rscript_cmd+' '+r_tmp_file)
    finally:
        os.system('cat '+r_tmp_file)
        os.system('rm '+r_tmp_file)

