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

- Tabular data consists of an ordered arrangement of rows and columns.
- A common example is a spreadsheet.
- In this class will often be referred to as a matrix $\mathbf{X_{ij}}$ of $i$ observations of $j$ variables.
  - Note all columns must be of equal length ($i$), and all rows must be of equal length ($j$).

<aside class="notes">
In this class we are primarily focused on tabular data. If your data is not tabular, you may want to figure out some way to coerce it to a tabular format because most statistical/ML models assume tabular data.
</aside>

## Coercing Data Structures

- In reality, processes we observe are rarely tabular.
  - Some observations may have special characteristics that others do not. ($j$ is not equal for all $i$)
  - There may no be inherent ordering in our observations, or the characteristics ($i$ or $j$ are not orderable).
  - Observations may be related, overlapping, or nested in a way that is relevant to our model but not suitable for a two-dimensional table.
- _Take away_:
  - When we receive or generate tabular data, we should keep in mind the _data-generating process_ and decide whether we are systematically losing information that is relevant to our model.
  - Trade-offs and subjective decisions are always necessary; make these clear and do your best to justify them.

# `pandas`

`pandas` is a very popular library for working with tabular data structures in Python. Before we start using it, let's go over some of the ways it can be useful to you as a social science researcher.

## Advantages of `pandas`

- provides fast, flexible data structures
- extensive array of convenient functions
- compatible with most data science libraries and data types

## When you should **not** use `pandas`

- Your data is not coercible to a tabular structure.
- When your dataset is too large to load in your computer's memory (or loading it uses most of your RAM).

<aside class="notes">
- `pandas` is so standard, that it makes more sense to talk about the scenarios in which you would not want to use pandas
- Note on RAM: It's not straightforward to predict the size of a dataset loaded into `pandas`. There are also options for dealing with datasets this large, although those are beyond what I can discuss in the lecture.
</aside>


## Data I/O

`pandas` comes with functions for reading and writing to all kinds of data formats. A quick list can be viewed using tab completion:

```{python}
In [1]: import pandas as pd

In [2]: pd.read_<TAB>
 read_clipboard() read_hdf()       read_sas()
 read_csv()       read_html()      read_sql()
 read_excel()     read_json()      read_sql_query()
 read_feather()   read_msgpack()   read_sql_table()
 read_fwf()       read_parquet()   read_stata()
 read_gbq()       read_pickle()    read_table
```

<aside class="notes">
- Explain what I/O means.
- This is a good moment to mention tab completion. Revisit it later during the coding tutorial.
</aside>


# Data Formats

There are a number of data storage formats that you should be aware of:

- `csv`
- `xls(x)`
- `json`
- `dta`
- `pickle`

## `csv` format

`csv` (_comma-separated-values_ or as I prefer, _character-separated values_), is a standard _plain text_ tabular data storage format.

| Pros                            | Cons                                    |
| ------------------------------- | --------------------------------------- |
| lightweight/compressable        | unpredictable separator behaviour       |
| human readable                  | fixed number of rows (strictly tabular) |
| mostly portable between systems | no built-in data types                  |
| row-accessible data format      | lack of durability                      |
|                                 | not easily column-accessible            |


## `xls(x)`

- Microsoft excel's data format.
- Not human-readable (binary).
- Tabular, but also contains some relational aspects when used with multiple "sheets".
- Note that merged cells, conditional formatting, etc. will be lost when importing with `pandas`.

## `json`

- Stands for _javascript object notation_.
- Relational: stores values as key-value pairs.
- Human-readable.
- Can store arrays as values.
- Frequently used by web APIs.
- Similar: `yaml`, `cson`, etc.

<!-- ```{json}
{
    "menu": {
        "id": "file",
        "value": "File",
        "popup": {
            "menuitem": [
                {"value"   : "New",
                 "onclick" : "CreateNewDoc()"},
                {"value"   : "Open",
                 "onclick" : "OpenDoc()"}
            ]
        }
    }
}
``` -->

## `dta`

- Stata's standard data storage format.
- Not human-readable (binary).
- `pandas` contains a reader for these by default.
- Not standard in industry, but common in political science.

## `pickle`

- Python's compressed data format.
- Stores objects exactly as they are in a python script.
- **WARNING**: Can be used to execute malicious code. Only open pickles that you can trust.

## DBMS and `SQL`

- In industry, database management systems (DBMS) are used to store and query large quantities of data in a reliable way.
- `SQL`-compliant databases are a common type. `SQL` is a database managing and querying language.
- If your research requires you to constantly be collecting data and ensuring its reliability, you should opt for a DBMS instead of one of the filetypes mentioned above.

# Coding Tutorial

Today, we learn about the following in `pandas`:

- Data I/O
- Understanding the `DataFrame` and `Series`
- Indexing and Slicing
- First look at the data
- Summary functions

## Data I/O

- As seen earlier, pandas has methods for reading in data from various formats.
- A strength of learning a library like `pandas` is that we can analyse tabular data regardless of the source format.

## Understanding `DataFrame` and `Series`

- `pandas` contains two native data containers:
  - `pandas.DataFrame`: A two-dimensional\* labelled matrix
  - `pandas.Series`: A one-dimensional labelled array

## Indexing and Slicing

- The fundamental 
