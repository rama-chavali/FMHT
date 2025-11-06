import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

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

# Analytical solution
U = np.zeros(YMAX)
for j in range(YMAX):
    if j == 0 or j == YMAX - 1:
        U[j] = 0.0
    else:
        U[j] = (dp / (2.0 * MU * l)) * ((h ** 2) / 4 - Y[j] ** 2)

# Load CFD data
data1 = pd.read_csv("../pressure_outlet/2m_geometry_200x20/outlet.txt", sep="\s+", header=None)
data2 = pd.read_csv("../pressure_outlet/2m_geometry_100x10/outlet.txt", sep="\s+", header=None)
data3 = pd.read_csv("../pressure_outlet/2m_geometry_400x40/outlet.txt", sep="\s+", header=None)

# Find common y-values across all datasets
common_y = np.intersect1d(data1[0].to_numpy(),
                          np.intersect1d(data2[0].to_numpy(), data3[0].to_numpy()))

# Filter u-values corresponding to these common y-values
u1_common = data1.loc[data1[0].isin(common_y), 1].to_numpy()
u2_common = data2.loc[data2[0].isin(common_y), 1].to_numpy()
u3_common = data3.loc[data3[0].isin(common_y), 1].to_numpy()

# Plot
plt.plot(U, Y, label=r'$\mathbf{analytical}$')
plt.plot(u2_common, common_y, label=r'$\mathbf{coarse}$')
plt.plot(u1_common, common_y, label=r'$\mathbf{moderate}$')
plt.plot(u3_common, common_y, label=r'$\mathbf{fine}$')

plt.legend()
plt.grid(True)

ax = plt.gca()
ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(axis='x', style='sci', scilimits=(-4,-4))
ay = plt.gca()
ay.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ay.ticklabel_format(axis='y', style='sci', scilimits=(-1,-2))

# Bold LaTeX labels
plt.xlabel(r"$\mathbf{x-velocity}$", fontsize=14)
plt.ylabel(r"$\mathbf{h}$", fontsize=14)

plt.savefig("plots/pressureoutletvsanalytical.eps", dpi=800)
plt.savefig("plots/pressureoutletvsanalytical.png", dpi=800)

plt.show()
