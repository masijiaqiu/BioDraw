import prettyplotlib as ppl
import matplotlib.pyplot as plt
import csv
from numpy import array


# parameters = {
#   'title': 'heatmap demo'
# }
def heatmap(input_data, parameters, output):
    data = []
    with open(input_data) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            data.append([float(item) for item in row])
    f.close()

    data = array(data)
    fig, ax = plt.subplots(1)
    ppl.pcolormesh(fig, ax, data)
    ax.set_title(parameters['title'])
    fig.savefig(output, format='svg')
