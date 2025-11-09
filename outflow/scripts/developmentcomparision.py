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
plt.rcParams['mathtext.default'] = 'bf'

YMAX = 101

RHO = 1000.0
MU = 0.00102
NU = MU / RHO

length = 2.0
height = 0.2
width = 0.2

l = length
h = height
w = width

Re = 41.0
ua = (Re * NU) / (2 * h)
dp = (12.0 * MU * l * ua) / (h * h)
Q  = (w * dp * h**3) / (12.0 * MU * l)

y_min = -h / 2
y_max =  h / 2
Y = np.linspace(y_min, y_max, YMAX)

U = np.zeros(YMAX)
for j in range(YMAX):
    if j == 0 or j == YMAX - 1:
        U[j] = 0.0
    else:
        U[j] = (dp / (2.0 * MU * l)) * ((h ** 2) / 4 - Y[j] ** 2)

data1 = pd.read_csv("../pressure_outlet/coarse10mpressureoutlet/outlet.txt", sep="\s+", header=None)
data2 = pd.read_csv("../pressure_outlet/initial_geometry/outlet.txt", sep="\s+", header=None)

plt.plot(U, Y, label='Analytical')
plt.plot(data2[1].to_numpy(), data2[0].to_numpy(), label='Initial geometry')
plt.plot(data1[1].to_numpy(), data1[0].to_numpy(), label='Extended geometry')

ax = plt.gca()
ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(axis='x', style='sci', scilimits=(-4, -4))

plt.xlabel('u', fontweight='bold')
plt.ylabel('y', fontweight='bold')
plt.legend(loc='best', handlelength=2, labelspacing=0.3, prop={'weight': 'bold'})

for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
             ax.get_xticklabels() + ax.get_yticklabels() +
             [ax.xaxis.get_offset_text(), ax.yaxis.get_offset_text()]):
    item.set_fontweight('bold')

ax.tick_params(axis='both', width=1.2)

plt.savefig("plots/initialvsincreased.eps", dpi=800)
plt.savefig("plots/initialvsincreased.png", dpi=800)

plt.show()
