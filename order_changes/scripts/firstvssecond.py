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

Re = 41.0
ua = (Re * NU) / (2 * height)
dp = (12.0 * MU * length * ua) / (height ** 2)

Y = np.linspace(-height/2, height/2, YMAX)

U = np.zeros(YMAX)
for j in range(YMAX):
    if j == 0 or j == YMAX - 1:
        U[j] = 0.0
    else:
        U[j] = (dp / (2.0 * MU * length)) * ((height ** 2)/4 - Y[j]**2)

data1 = pd.read_csv("../first_order/poutlet.txt", sep="\s+", header=None)
data2 = pd.read_csv("../first_order/outflow.txt", sep="\s+", header=None)
data3 = pd.read_csv("../second_order/poutlet.txt", sep="\s+", header=None)
data4 = pd.read_csv("../second_order/outflow.txt", sep="\s+", header=None)


fig, ax = plt.subplots(constrained_layout=True)
#ax.plot(U, Y, label=r'Analytical')
ax.plot(data1[1].to_numpy(), data1[0].to_numpy(), label=r'First Order Pressure Outlet ')
#ax.plot(data2[1].to_numpy(), data2[0].to_numpy(), label=r'First Order Outflow')
ax.plot(data3[1].to_numpy(), data3[0].to_numpy(), label=r'Second Order Pressure Outlet')
#ax.plot(data4[1].to_numpy(), data4[0].to_numpy(), label=r'Second Order Outflow')


ax.legend()
ax.grid(True)

ax = plt.gca()
ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(axis='x', style='sci', scilimits=(-4, -4))
ay = plt.gca()
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(axis='y', style='sci', scilimits=(-1, -2))

plt.xlabel('$u$', fontsize=14)
plt.ylabel('$h$', fontsize=14)

plt.savefig("plots/firstvssecond.eps", dpi=800)
plt.savefig("plots/firstvssecond.png", dpi=800)


plt.show()
