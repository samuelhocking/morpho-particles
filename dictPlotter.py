# Helper script to produce matplotlib plots from morpho dicts
# By: Sam Hocking

import sys
import json
import os
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from dictImportTools import Tools

cwd = os.getcwd()

seriesArr = []
xfield = sys.argv[1]

if xfield == "numPts":
    notxfield = "numVerts"
else:
    notxfield = "numPts"

for i in range(2,len(sys.argv)):
    seriesArr.append(pd.Series(Tools.importFloatDict(sys.argv[i])))
df = pd.DataFrame(seriesArr)

df.to_csv(f'{cwd}/results/results_{xfield}_({datetime.now().strftime("%Y.%m.%d-%H.%M.%S")})_data.csv')
# df.to_json(f'{cwd}/results/results_{xfield}_({datetime.now().strftime("%Y.%m.%d-%H.%M.%S")}).json')

fig, ax = plt.subplots(figsize=(8,6))

col_list = list(df)
col_list.remove(xfield)
col_list.remove(notxfield)
df['total'] = df[col_list].sum(axis=1)
col_list.append('total')
print(df)

for col in col_list:
    plt.plot(df[xfield], df[col], label=f'{col}')
handles, labels = ax.get_legend_handles_labels()
lgd = ax.legend(handles, labels, loc='right', bbox_to_anchor=(1.3,0.5))
ax.set_title(f'Process "time" vs. {xfield} [{notxfield}={int(df[notxfield][0])}]')
ax.set_xlabel(xfield)
ax.set_ylabel('"Time"')
filename = f'{cwd}/results/results_{xfield}_({datetime.now().strftime("%Y.%m.%d-%H.%M.%S")})_plot.png'
fig.savefig(filename, bbox_extra_artists=(lgd,), bbox_inches='tight')