import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import numpy as np

matplotlib.rcParams["text.usetex"] = False

# Figure 1: Bernoulli Entropy

q = np.linspace(0.000000001, 0.9999999999, 1000)
H_x = - q*np.log2(q) - (1-q)*np.log2(1-q)

sns.set_style('whitegrid')

f, ax = plt.subplots(1, 1, figsize=(9, 5))
ax.plot(q, H_x, color='cornflowerblue')
ax.axvline(0, lw=2, color='k', alpha=0.8)
ax.axhline(0, lw=2, color='k', alpha=0.8)
ax.axvline(0.5, ls="--", color='darkgrey', alpha=0.8)
ax.text(0.49, -0.1, "0.5")
ax.set_xlim(-0.05, 1.05)
ax.set_ylim(-0.05, 1.0025)
matplotlib.rcParams["text.usetex"] = True
ax.set_xlabel("$q$")
ax.set_ylabel("$H_X$")
matplotlib.rcParams["text.usetex"] = False
f.savefig("fig_bernoulli.png", bbox_inches="tight")
