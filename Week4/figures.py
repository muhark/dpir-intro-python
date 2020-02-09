import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

# sns.set_style("darkgrid")

# Figure 1: Summary Statistics vs DistPlot

x1 = list(np.random.normal(0, 1, 150))+list(np.random.normal(8, 1, 150))
x2 = np.random.normal(4, 4, 300)
x3 = np.random.multinomial(1, [1/6]*6, size=300).ravel()+1
data = pd.DataFrame({
    "x1": x1,
    "x2": x2,
    "x3": x3
    })
data.describe().to_html()
df = data.melt()

f, ax = plt.subplots(1, 1, figsize=(15, 8))
sns.distplot(data['x1'], label='x1')
sns.distplot(data['x2'], label='x2')
ax.legend()
f.savefig("figures/lecture_fig1.png", bbox_inches="tight")


# Gallery

# Histogram (One Category)

f, ax = plt.subplots(1, 1, figsize=(15, 8))
sns.distplot(df['value'], kde=False)
f.savegfig("figures/lecture_hist1.png")

# Histogram (Two Categories)

f, ax = plt.subplots(1, 1, figsize=(15, 8))
sns.distplot(data['x1'], label='x1', kde=False)
sns.distplot(data['x2'], label='x2', kde=False)
ax.legend()
f.savefig($1, bbox_inches="tight")

# Box and Whisker Plot

f, ax = plt.subplots(1, 1, figsize=(15, 8))
sns.boxplot(df['variable'], df['value'])
f.savefig("figures/lecture_box1.png", bbox_inches="tight")

# Swarm Plot (One Category)

f, ax = plt.subplots(1, 1, figsize=(15, 8))
sns.boxplot(df['variable'], df['value'])
f.savefig("figures/lecture_box1.png", bbox_inches="tight")


# Swarm Plot (Multiple Categories)

f, ax = plt.subplots(1, 1, figsize=(15, 8))
sns.swarmplot(df['value'], df['variable'])
f.savefig("figures/lecture_box1.png", bbox_inches="tight")


# Violin Plot (One Category)

# Violin Plot (Two Categories)

# Scatter Plot

# Line Plot

# Bar Plot

# Rug Plot


# Anatomy of a Figure

matplotlib.rcdefaults()
f = plt.figure(figsize=(15, 8))

matplotlib.rc('axes', edgecolor='r', lw=5)
f, ax = plt.subplots(1, 1, figsize=(15, 8))
f.suptitle("This is a figure with a subplot")
ax.set_title("This is a subplot", color="r")
f.savefig("figures/lecture_emptysubplot1.png", bbox_inches="tight")
matplotlib.rcdefaults()


#matplotlib.rc('axes', edgecolor='r', lw=5)
f, ax = plt.subplots(1, 2, figsize=(15, 8))
f.suptitle("This is a figure with two subplots")
ax[0].set_title("This is a subplot", color="r")
ax[1].set_title("This is another subplot", color="r")
f.savefig("figures/lecture_emptysubplot2.png", bbox_inches="tight")
matplotlib.rcdefaults()

#matplotlib.rc('axes', edgecolor='r', lw=5)
f, ax = plt.subplots(2, 2, figsize=(15, 8))
f.suptitle("This is a figure with four subplots")
for i in range(2):
    for j in range(2):
        ax[i][j].set_title(f"Subplot [{i}][{j}]", color="r")
f.savefig("figures/lecture_emptysubplot3.png", bbox_inches="tight")
matplotlib.rcdefaults()



f, ax = plt.subplots(1, 1, figsize=(15, 8))
ax.scatter(data['x2'], data['x1'], color=data['x3'].apply(
    lambda x: dict(zip(range(1, 6), sns.color_palette(n_colors=5)))[x]))
f.savefig("figures/lecture_scatter1.png", bbox_inches="tight")

f, ax = plt.subplots(1, 1, figsize=(15, 8))
ax.plot(np.linspace(0, 10, 100), np.linspace(0, 5, 100), color='r')

f, ax = plt.subplots(1, 1, figsize=(15, 8))
ax.scatter(data['x2'], data['x1'], color='r')
ax.plot(np.linspace(-10, 20, 150), np.linspace(-3.5, 4, 150)**2)
ax.axhline(0, color='k', alpha=0.5, ls="--")
ax.axvline(0, color='k', alpha=0.5, ls="--")
