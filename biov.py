"""
Author: Xu Zhang
Date: 2016/08/16
Version: 1.0
Description: 
"""

import sys
import csv
import json


def biov(input_json):
    
    with open(input_json, 'r') as f:
        config_json = json.load(f)

    chart_info = None
    with open('./config/charts.csv') as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        for row in f_csv:
            if row[0] == config_json['chart_id']:
                chart_info = row
                break


    if chart_info is not None:
        package = chart_info[1]
        function = chart_info[2]
        exec('import '+package)
        exec(package+'.'+function+'(config_json["data"], config_json["parameters"], config_json["output"])')


if __name__ == '__main__':
    if len(sys.argv) < 1:
        print("Error, Invalid Parameters!!!")
        exit()
    else:
        biov(sys.argv[1])
