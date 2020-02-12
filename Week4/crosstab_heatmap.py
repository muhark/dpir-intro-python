import pandas as pd
import re
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_feather("../Week2/data/bes_data_subset_week2.feather")
matplotlib.rcParams["text.usetex"] = True


def crosstab_heatmap(df, col1, col2, col_dict):
    # Produce crosstab
    xtab = pd.crosstab(df[col1], df[col2])
    # Right-column should show total number of answers
    if isinstance(xtab.columns, pd.CategoricalIndex):
        xtab.columns = xtab.columns.add_categories("Total")
    if isinstance(xtab.index, pd.CategoricalIndex):
        xtab.index = xtab.index.add_categories("Avg Prop")
    xtab.loc[:, "Total"] = xtab.sum(axis=1)
    xtab = xtab.loc[xtab['Total'] >= xtab.shape[1]*5]
    props = xtab.iloc[:, :-1].div(xtab['Total'], axis=0)
    props.loc['Avg Prop', :] = props.mean(axis=0)
    xtab.loc['Avg Prop', :] = ""
    props.loc[:, 'Total'] = ""

    annot = xtab.applymap(
        lambda x: "{:.4g}\n".format(int(x)) if isinstance(x, float) else ""
        ).add(
            props.applymap(
                lambda x: "({:.3g}\%)".format(
                    100*x) if isinstance(x, float) else ""
                ))

    annot.loc['Avg Prop', 'Total'] = "{:.5g}".format(xtab.iloc[:-1, -1].sum())
    annot.loc['Avg Prop', :] = annot.loc['Avg Prop',
                                         :].str.replace(re.compile(r"[\(\)]"), "")
    annot.loc[:, 'Total'] = annot['Total'].str.replace("\n", "")
    diffs = props.iloc[:, :-1] - props.iloc[-1, :-1]
    diffs['Total'] = float(0)
    diffs = diffs.applymap(lambda x: 100*x)

    fig_title = "Crosstab Heatmap of \\textbf{"+col_dict[col1]+"} by \\textbf{"+col_dict[col2]

    f, ax = plt.subplots(1, 1, figsize=annot.shape)
    sns.heatmap(
        diffs.T,
        annot=annot.T,
        fmt="s",
        ax=ax,
        cmap="RdBu_r",
        center=0,
        cbar_kws={"label": "Difference from Avg. Proportion"},
    )
    ax.set_title(fig_title)
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position("top")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="left")
    ax.set_yticklabels(ax.get_yticklabels())
    f.axes[1].set_yticklabels(
        [lab.get_text() + "\%" for lab in f.axes[1].get_yticklabels()]
    )
    ax.axvline(diffs.shape[0] - 1, color="k")
    ax.axhline(diffs.shape[1] - 1, color="k")
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.xaxis.set_label_position("bottom")
    return f



col_dict = {'a02': 'Best Party', 'y09': 'Gender'}
f = crosstab_heatmap(df, 'a02', 'y09', col_dict)
f.savefig("extra_challenge.png", bbox_inches="tight")
