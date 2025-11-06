import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# rc params
plt.rcParams.update({
    "figure.figsize": (6, 4),
    "font.size": 12,
    "lines.linewidth": 1.5,
    "axes.labelsize": 12,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
    "legend.frameon": False,
    "axes.grid": True
})

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


data1 = pd.read_csv("../pressure_outlet/2m_geometry_200x20/outlet.txt", sep="\s+", header=None)
data2 = pd.read_csv("../pressure_outlet/2m_geometry_100x10/outlet.txt", sep="\s+", header=None)
data3 = pd.read_csv("../pressure_outlet/2m_geometry_400x40/outlet.txt", sep="\s+", header=None)

plt.plot(U, Y, label='analytical')
plt.plot(data2[1].to_numpy(), data2[0].to_numpy(), label='coarse')
plt.plot(data1[1].to_numpy(), data1[0].to_numpy(), label='moderate')
plt.plot(data3[1].to_numpy(), data3[0].to_numpy(), label='fine')


plt.legend()
plt.grid(True)

from matplotlib.ticker import ScalarFormatter
ax = plt.gca()
ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(axis='x', style='sci', scilimits=(-4,-4))

plt.xlabel('u')
plt.ylabel('y')

plt.savefig("plots/pressureoutletvsanalytical.eps", dpi=800)
plt.savefig("plots/pressureoutletvsanalytical.png", dpi=800)

plt.show()
