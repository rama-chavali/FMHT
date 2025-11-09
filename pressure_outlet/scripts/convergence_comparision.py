import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

plt.rcParams.update({
    "figure.figsize": (8, 6),
    "font.size": 12,
    "font.family": "serif",
    "font.serif": ["Times New Roman"],
    "lines.linewidth": 1.5,
    "axes.labelsize": 12,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
    "legend.fontsize": 9,
    "legend.frameon": False,
    "axes.grid": True
})
plt.rcParams['mathtext.default'] = 'bf'

#data1 = pd.read_csv("../coarse10mpressureoutlet/uconvergence.txt", sep="\s+", header=None)
#data2 = pd.read_csv("../initial_geometry/uconvergence.txt", sep="\s+", header=None)
data3 = pd.read_csv("../2m_geometry_100x10/uconvergence.txt", sep="\s+", header=None)
#plt.plot(data1[0].to_numpy(), data1[1].to_numpy(), color="#1f77b4", label='Extended geometry')
#plt.plot(data2[0].to_numpy(), data2[1].to_numpy(), color="red", label='Initial geometry')
plt.plot(data3[0].to_numpy(), data3[1].to_numpy(), color="orange", label='Final geometry')

ax = plt.gca()
ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(axis='x', style='sci', scilimits=(-4, 4))
ax.ticklabel_format(axis='y', style='sci', scilimits=(-1, 1))

plt.xlabel('u', fontweight='bold')
plt.ylabel('y', fontweight='bold')
plt.legend(loc='best', handlelength=1.2, labelspacing=0.3, prop={'weight': 'bold'})

for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
             ax.get_xticklabels() + ax.get_yticklabels() +
             [ax.xaxis.get_offset_text(), ax.yaxis.get_offset_text()]):
    item.set_fontweight('bold')

ax.tick_params(axis='both', width=1.2)

plt.savefig("plots/final_uconvergence.eps", dpi=800)
plt.savefig("plots/final_uconvergence.png", dpi=800)
plt.show()
