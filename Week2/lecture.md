---
title: Introduction to Python for Social Science
subtitle: Lecture 2 - Data Structures and Pandas I
author: Musashi Harukawa, DPIR
date: 2nd Week Hilary 2020
---

# Last Week

- What is Python, and what can I use it for?
- What tools do I have to write, test and run Python code?
    - Opening up JupyterLab/Notebooks/IPython
    - Executing code in Jupyter, etc.
- Writing your first Python script and notebook.
    - Data Types
    - Data Structures

## This Week

This week we will learn about a key library for working with **data**:

- Thinking about (tabular) data
- I/O
- Slicing, indexing
- Summarising


# The Hard Truth About Data Science...

- Analysis usually takes \<30% of your time.
- \>50% of your time will be spent reading, cleaning, checking, storing, and cursing your data.
- Data cleaning is meticulous work, but that doesn't mean you can't be efficient.

# Thinking About Data

We can think of a data point as having two properties:

1. Value
2. Relation (to other values)

<aside class="notes">
- Inherent in value is an abstract type that the value is an instance of.
- In data science, we are often more concerned with the latter than the former for the bulk of the analysis. I say this because we don't tend to care about the exact values, beyond type, until the end, when we look at the output of our model. When building our pipeline, what matters most is the type and structure of data.
</aside>

# Data Structures

Three Ways of Structuring Data:

- Graph
- Tree (Hierarchical)
- **Tabular**

<aside class="notes">
Option: Do an example of how we can structure data about the members of the class.
</aside>

## Graph

- Graphs are constructed of nodes (vertices) and edges.

![Graph](https://upload.wikimedia.org/wikipedia/commons/9/9c/Graphe_initial_avant_contraction.png)

<aside class="notes">
- Nodes and edges can have values associated with them.
- A special case of graphs, called directed graphs, have edges with directions associated with them.
</aside>

## Trees

- A tree is a type of graph with [a number of properties](https://en.wikipedia.org/wiki/Tree_(graph_theory)#Tree)
- Commonly used to represent hierarchical data structures, such as nested sets or dependency/flow diagrams.

![Tree](https://upload.wikimedia.org/wikipedia/commons/c/cd/Arbol3.PNG)

<aside class="notes">
- Websites are all trees in their backend.
- A lot of the data you encounter will be tree-like in nature.
    - A key point about this is that each element in this tree may not have the same properties. This can cause problems when attempting to convert to tabular data.
</aside>

## Tabular Data

-

<aside class="notes">
In this class we are primarily focused on tabular data. If your data is not tabular, you may want to figure out some way to coerce it to a tabular format because most statistical/ML models assume tabular data.
</aside>

# Data I/O

Pandas comes with functions for reading and writing to all kinds of data formats. A quick list can be viewed using tab completion:

```{python}
In [1]: import pandas as pd

In [2]: pd.read_<TAB>
 read_clipboard() read_hdf()       read_sas()
 read_csv         read_html()      read_sql()
 read_excel()     read_json()      read_sql_query()
 read_feather()   read_msgpack()   read_sql_table()
 read_fwf()       read_parquet()   read_stata()
 read_gbq()       read_pickle()    read_table
```

# `csv` format

`csv` (_comma-separated-values_ or as I prefer, _character-separated values_), is a standard _plain text_ tabular data storage format.

Some reasons to use `csv`:

- lightweight
- human-readable
- optional header (first row)
- \*fairly\* portable between systems

Some limitations of `csv`:

- unpredictable behaviour of separator is common character (e.g. `,`)
- fixed number of rows (strictly tabular)
- not very durable

# `pd.read_csv()`
