import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

# sns.set_style("darkgrid")

# Figure 1: Summary Statistics vs DistPlot

x1 = list(np.random.normal(0, 1, 150))+list(np.random.normal(8, 1, 150))
x2 = np.random.normal(4, 4, 300)
x3 = np.random.multinomial(1, [1/6]*6, size=50).ravel()
data = pd.DataFrame({
    "x1": x1,
    "x2": x2,
    "x3": x3
    })
data.describe().to_html()
df = data.melt()

f, ax = plt.subplots(1, 1, figsize=(8, 4))
sns.distplot(data['x1'], label='x1')
sns.distplot(data['x2'], label='x2')
ax.legend()
f.savefig("figures/lecture_fig1.png", bbox_inches="tight")

bes_df = pd.read_feather("../Week2/data/bes_data_subset_week2.feather")

# Anatomy of a Figure

matplotlib.rcdefaults()
f = plt.figure(figsize=(8, 4))

matplotlib.rc('axes', edgecolor='r', lw=5)
f, ax = plt.subplots(1, 1, figsize=(8, 4))
f.suptitle("This is a figure with a subplot")
ax.set_title("This is a subplot", color="r")
f.savefig("figures/lecture_emptysubplot1.png", bbox_inches="tight")
matplotlib.rcdefaults()


#matplotlib.rc('axes', edgecolor='r', lw=5)
f, ax = plt.subplots(1, 2, figsize=(8, 4))
f.suptitle("This is a figure with two subplots")
ax[0].set_title("This is a subplot", color="r")
ax[1].set_title("This is another subplot", color="r")
f.savefig("figures/lecture_emptysubplot2.png", bbox_inches="tight")
matplotlib.rcdefaults()

#matplotlib.rc('axes', edgecolor='r', lw=5)
f, ax = plt.subplots(2, 2, figsize=(8, 4))
f.suptitle("This is a figure with four subplots")
for i in range(2):
    for j in range(2):
        ax[i][j].set_title(f"Subplot [{i}][{j}]", color="r")
f.savefig("figures/lecture_emptysubplot3.png", bbox_inches="tight")
matplotlib.rcdefaults()



f, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.scatter(data['x2'], data['x1'], color='r')
# data['x3'].apply(lambda x: dict(zip(range(1, 6), sns.color_palette(n_colors=5)))[x])
f.savefig("figures/lecture_scatter1.png", bbox_inches="tight")

f, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.plot(np.linspace(0, 10, 100), np.linspace(0, 5, 100), color='r')
f.savefig("figures/lecture_line1.png", bbox_inches="tight")

f, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.scatter(data['x2'], data['x1'], color='r', s=3)
ax.plot(np.linspace(-10, 20, 150), np.linspace(-3.5, 4, 150)**2)
ax.axhline(0, color='k', alpha=0.5, ls="--")
ax.axvline(0, color='k', alpha=0.5, ls="--")
f.savefig("figures/lecture_linescatter1.png", bbox_inches="tight")

f, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.scatter(data['x2'], data['x1'], color='g', s=3)
ax.plot(np.linspace(-10, 20, 150), np.linspace(-3.5, 4, 150)**2)
ax.axhline(0, color='k', alpha=0.5, ls="--")
ax.axvline(0, color='k', alpha=0.5, ls="--")
ax.xaxis.set_label_text("X-Axis Label", color='r')
ax.yaxis.set_label_text("Y-Axis Label", color='r')
f.savefig("figures/lecture_linescatter2.png", bbox_inches="tight")

f, ax = plt.subplots(1, 1, figsize=(8, 3.5))
ax.scatter(data['x2'], data['x1'], color='g', s=3)
ax.plot(np.linspace(-10, 20, 150), np.linspace(-3.5, 4, 150)**2)
ax.axhline(0, color='k', alpha=0.5, ls="--")
ax.axvline(0, color='k', alpha=0.5, ls="--")
ax.xaxis.set_label_text("X-Axis Label")
ax.yaxis.set_label_text("Y-Axis Label")
ax.xaxis.set_ticks(range(-10, 40, 10))
ax.yaxis.set_ticks(range(-4, 25, 2))
f.savefig("figures/lecture_linescatter3.png", bbox_inches="tight")

f, ax = plt.subplots(1, 1, figsize=(8, 3.5))
ax.scatter(data['x2'], data['x1'], color='g', s=3)
ax.plot(np.linspace(-10, 20, 150), np.linspace(-3.5, 4, 150)**2)
ax.axhline(0, color='k', alpha=0.5, ls="--")
ax.axvline(0, color='k', alpha=0.5, ls="--")
ax.xaxis.set_label_text("X-Axis Label")
ax.yaxis.set_label_text("Y-Axis Label")
ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(base=3))
ax.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(base=2))
f.savefig("figures/lecture_linescatter4.png", bbox_inches="tight")


f, ax = plt.subplots(1, 1, figsize=(8, 4))
sns.boxenplot(bes_df['region'], bes_df['Age'], ax=ax)
ax.xaxis.set_ticklabels(ax.xaxis.get_ticklabels(), rotation=30)
f.savefig("figures/lecture_rotated_labels1.png", bbox_inches="tight")

# Gallery

sns.set_style('darkgrid')

# Histogram (One Category)

f, ax = plt.subplots(1, 1, figsize=(8, 4))
sns.distplot(bes_df['Age'].dropna(), kde=False, ax=ax)
ax.set_title("Age Distribution of BES Respondents")
f.savefig("figures/lecture_hist1.png")

# Histogram (Two Categories)

f, ax = plt.subplots(1, 1, figsize=(8, 6))
sns.distplot(bes_df[bes_df['y09'] == 'Male']
             ['Age'].dropna(), kde=False, label='Male')
sns.distplot(bes_df[bes_df['y09'] == 'Female']
             ['Age'].dropna(), kde=False, label='Female')
ax.legend()
ax.set_title("Age Distribution of BES by Gender")
f.savefig("figures/lecture_hist2.png", bbox_inches="tight")

# Box and Whisker Plot

f, ax = plt.subplots(1, 1, figsize=(8, 4))
sns.boxplot(bes_df['Age'].dropna(), bes_df['region'])
ax.set_title("BES Age Distribution by Region")
f.savefig("figures/lecture_box1.png", bbox_inches="tight")

# Swarm Plot (One Category)

f, ax = plt.subplots(1, 1, figsize=(8, 4))
sns.swarmplot(bes_df['Age'])
ax.set_title("BES Age Swarm Plot")
f.savefig("figures/lecture_swarm1.png", bbox_inches="tight")


# Swarm Plot (Multiple Categories)

f, ax = plt.subplots(1, 1, figsize=(8, 4))
sns.swarmplot(bes_df['Age'], bes_df['y01'])
ax.set_title("BES Age Swarm Plot by Income Group")
f.savefig("figures/lecture_swarm2.png", bbox_inches="tight")


# Violin Plot (One Category)

f, ax = plt.subplots(1, 1, figsize=(8, 4))
sns.violinplot(bes_df['Age'])
ax.set_title("BES Age Violin Plot")
f.savefig("figures/lecture_violin1.png", bbox_inches="tight")

# Heatmap

f, ax=plt.subplots(1, 1, figsize=(15, 8))
sns.heatmap(pd.crosstab(bes_df['y01'], bes_df['region']), cmap="RdBu_r")
f.savefig("figures/lecture_heatmap1.png", bbox_inches="tight")
# This is an issue with this particular version of matplotlib
