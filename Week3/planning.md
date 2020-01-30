---
title: Week 3 Planning - Data Structures and Pandas II
author: Musashi Harukawa
---

<!-- # From the Syllabus

**Learning Aims**:

1. Writing Python functions
2. Vectorize with `apply`
3. Split-apply-combine with `groupby`
4. Working with datetime data

The third week builds on students' knowledge of `pandas`, introducing two key tools in data analysis: `apply` and `groupby`. Students will also learn how to write functions and be introduced to the idea of namespaces.

By the end of this week, students should have a sufficient grounding in handling tabular data with base Python and `pandas` to deal with most data cleaning and reshaping tasks they use in their own research.

# Lecture Structure

- Recap from last week
    - Series and DataFrames
    - Slicing and Indexing
    - Summary functions
- Writing functions
    - We want to be able to apply any summary function
    - How to write functions in Python
        - `def`
        - inputs and outputs
        - naming conventions
        - Extra: `lambda` functions
    - Aside: when to use functions (if you find yourself copy pasting code and editing, then use a function).
- pandas `apply`
    - `pd.Series.apply`
    - `pd.DataFrame.apply`
    - `apply` vs `itertuples` or `iterrows`
- Split-apply-combine
    - Frequent use case: apply function to groups within the data. For example, get a per-state average.
    - Diagrammatic explanation
    - A few examples
    - The issue with multi-indexes, the easy fix.
- Working with datetime data (is a nightmare)
    - The nightmare of datetimes
    - `strptime` and `strftime`
    - python native `datetime`, pandas `Timestamp` and numpy `datetime64`
    - `pd.Series.dt` functions, and how they can be used with `groupby` -->

# Methods Covered:

- Writing functions
- Column/DataFrame apply
- Groupby-Apply
- Append, concat and merge
- Melt and pivot

# Methods/Theory

- What is a function?
- Applying functions to vectors:
    - transformation, pointwise, and summaries
    - grouped summary
- Combining datasets
    - Append vs concat vs merge
    - A bit of set theory: union, etc.
- Long vs wide-form data


# Computational Aspect

- Functions:
    - Tools for control flow + generalizability
    - Namespaces
- Apply:
- Groupby-Apply:
    - Vectorization and performancea
- Append, concat and merge
    - Performance, accessibility over indexed data
-


Scrap:

$$
f(X_{i, 1}) = \begin{bmatrix}
                    f(x_{1, 1}) \\
                    f(x_{2, 1}) \\
                    \vdots \\
                    f(x_{N, 1})
                \end{bmatrix}
$$
