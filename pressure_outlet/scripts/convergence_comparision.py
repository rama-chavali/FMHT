import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

plt.rcParams.update({
    "figure.figsize": (6, 4),
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

#data1 = pd.read_csv("../coarse10mpressureoutlet/uconvergence.txt", sep="\s+", header=None)
#data2 = pd.read_csv("../initial_geometry/uconvergence.txt", sep="\s+", header=None)
data3 = pd.read_csv("../2m_geometry_100x10/uconvergence.txt", sep="\s+", header=None)

#plt.plot(data2[0].to_numpy(), data2[1].to_numpy(),color="red", label='Initial geometry')
plt.plot(data3[0].to_numpy(), data3[1].to_numpy(),color="orange", label='Final geometry')
#plt.plot(data1[0].to_numpy(), data1[1].to_numpy(),label='Extended geometry')

ax = plt.gca()
ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(axis='x', style='sci')
ax.ticklabel_format(axis='y', style='sci', scilimits=(-4,-4))

plt.xlabel('x')
plt.ylabel('u')
plt.legend(loc='best', handlelength=1.2, labelspacing=0.3)

plt.savefig("plots/final_uconvergence.eps", dpi=800)
plt.savefig("plots/final_uconvergence.png", dpi=800)

plt.show()
