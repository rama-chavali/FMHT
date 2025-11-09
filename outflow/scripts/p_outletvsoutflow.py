import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

plt.rcParams.update({
    "figure.figsize": (8, 6),
    "font.size": 12,
    "lines.linewidth": 1.5,
    "axes.labelsize": 12,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
    "legend.frameon": True,
    "axes.grid": True
})
plt.rcParams['mathtext.default'] = 'bf'  # Make all math/scientific text bold

YMAX = 41
RHO = 1000.0
MU = 0.00102
NU = MU / RHO

length = 2.0
height = 0.2
width = 0.2

Re = 41.0
ua = (Re * NU) / (2 * height)
dp = (12.0 * MU * length * ua) / (height ** 2)

Y = np.linspace(-height/2, height/2, YMAX)  # y coordinates

U = np.zeros(YMAX)
for j in range(YMAX):
    if j == 0 or j == YMAX - 1:
        U[j] = 0.0
    else:
        U[j] = (dp / (2.0 * MU * length)) * ((height ** 2)/4 - Y[j]**2)  # Analytical velocity profile

# Read data from files
data1 = pd.read_csv("../2m_geometry_100x10/outlet.txt", sep="\s+", header=None)
data2 = pd.read_csv("../2m_geometry_200x20/outlet.txt", sep="\s+", header=None)
data3 = pd.read_csv("../2m_geometry_400x40/outlet.txt", sep="\s+", header=None)
data4 = pd.read_csv("../../pressure_outlet/2m_geometry_100x10/outlet.txt", sep="\s+", header=None)
data5 = pd.read_csv("../../pressure_outlet/2m_geometry_200x20/outlet.txt", sep="\s+", header=None)
data6 = pd.read_csv("../../pressure_outlet/2m_geometry_400x40/outlet.txt", sep="\s+", header=None)

fig, ax = plt.subplots()  # Create figure and axis

# Plot analytical and CFD data
ax.plot(U, Y, label='Analytical')
ax.plot(data1[1].to_numpy(), data1[0].to_numpy(), label='Coarse Outflow')
ax.plot(data2[1].to_numpy(), data2[0].to_numpy(), label='Moderate Outflow')
ax.plot(data3[1].to_numpy(), data3[0].to_numpy(), label='Fine Outflow')
ax.plot(data4[1].to_numpy(), data4[0].to_numpy(), label='Coarse Pressure outlet')
ax.plot(data5[1].to_numpy(), data5[0].to_numpy(), label='Moderate Pressure outlet')
ax.plot(data6[1].to_numpy(), data6[0].to_numpy(), label='Fine Pressure outlet')

# Legend and grid
ax.legend(loc='best', handlelength=2, labelspacing=0.3, prop={'weight':'bold'})
ax.grid(True)

# Axis formatting
ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(axis='x', style='sci', scilimits=(-4, -4))
ax.ticklabel_format(axis='y', style='sci', scilimits=(-1, -1))

# Axis labels
plt.xlabel('u', fontsize=14, fontweight='bold')
plt.ylabel('y', fontsize=14, fontweight='bold')

# Bold tick labels and offset text
for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
             ax.get_xticklabels() + ax.get_yticklabels() +
             [ax.xaxis.get_offset_text(), ax.yaxis.get_offset_text()]):
    item.set_fontweight('bold')

ax.tick_params(axis='both', width=1.2)  # Make ticks thicker

# Save figures
plt.savefig("plots/p_outletvsutletvsoutflow.eps", dpi=800)
plt.savefig("plots/p_outletvsutletvsoutflow.png", dpi=800)

plt.show()
