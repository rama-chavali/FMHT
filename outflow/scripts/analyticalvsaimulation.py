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
    "legend.frameon": True,
    "axes.grid": True
})
plt.rcParams['mathtext.default'] = 'bf'  # Make all math/scientific text bold
YMAX = 11

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

delY = h / (YMAX - 1)
y_min = -h / 2
y_max =  h / 2
Y = np.linspace(y_min, y_max, YMAX)

U = np.zeros(YMAX)
for j in range(YMAX):
    if j == 0 or j == YMAX - 1:
        U[j] = 0.0
    else:
        U[j] = (dp / (2.0 * MU * l)) * ((h ** 2) / 4 - Y[j] ** 2)

data1 = pd.read_csv("../2m_geometry_200x20/outlet.txt", sep="\s+", header=None)
data2 = pd.read_csv("../2m_geometry_100x10/outlet.txt", sep="\s+", header=None)
data3 = pd.read_csv("../2m_geometry_400x40/outlet.txt", sep="\s+", header=None)

common_y = np.intersect1d(data1[0].to_numpy(),
                          np.intersect1d(data2[0].to_numpy(), data3[0].to_numpy()))

u1_common = data1.loc[data1[0].isin(common_y), 1].to_numpy()
u2_common = data2.loc[data2[0].isin(common_y), 1].to_numpy()
u3_common = data3.loc[data3[0].isin(common_y), 1].to_numpy()

plt.plot(U, Y, label='Analytical')
plt.plot(u2_common, common_y, color="green", label='Coarse')
plt.plot(u1_common, common_y, color="orange", label='Moderate')
plt.plot(u3_common, common_y, color="red", label='Fine')

ax = plt.gca()
ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(axis='x', style='sci', scilimits=(-4, 4))
ax.ticklabel_format(axis='y', style='sci', scilimits=(-1, 1))

# Bold axis labels
plt.xlabel('u', fontweight='bold')
plt.ylabel('y', fontweight='bold')

# Bold legend
plt.legend(loc='best', handlelength=1.2, labelspacing=0.3, prop={'weight': 'bold'})

# Bold tick labels and scientific notation
for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
             ax.get_xticklabels() + ax.get_yticklabels() +
             [ax.xaxis.get_offset_text(), ax.yaxis.get_offset_text()]):
    item.set_fontweight('bold')

# Optional: make tick lines slightly thicker
ax.tick_params(axis='both', width=1.2)

plt.savefig("plots/outflowvsanalytical.eps", dpi=800)
plt.savefig("plots/outflowvsanalytical.png", dpi=800)

plt.show()
