# Helper script to produce matplotlib plots from morpho dicts
# By: Sam Hocking

import sys
import json
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from dictImportTools import Tools

cwd = os.getcwd()

seriesArr = []
xfield = sys.argv[1]
version = sys.argv[2]

if xfield == "num points":
    notxfield = "num vertices"
else:
    notxfield = "num points"

for i in range(3,len(sys.argv)):
    seriesArr.append(pd.Series(Tools.importFloatDict(sys.argv[i])))
df = pd.DataFrame(seriesArr)
print(df)

df.to_csv(f'{cwd}/results/results_{xfield}_({datetime.now().strftime("%Y.%m.%d-%H.%M.%S")}).csv')
df.to_json(f'{cwd}/results/results_{xfield}_({datetime.now().strftime("%Y.%m.%d-%H.%M.%S")}).json')

fig, ax = plt.subplots()

for col in df.columns:
    plt.plot(df[xfield], df[col], label=f'{col}')

plt.legend()
ax.set_title(f'Process "time" vs. {xfield} [{notxfield}={int(df[notxfield][0])}] ({version})')
ax.set_xlabel(xfield)
ax.set_ylabel('"Time"')
filename = f'{cwd}/results/results_plot_{xfield}_{version}_({datetime.now().strftime("%Y.%m.%d-%H.%M.%S")}).png'
plt.savefig(filename)
plt.show()

