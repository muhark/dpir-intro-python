---
title: Introduction to Python for Social Science
subtitle: Lecture 4 - Data Visualization
author: Musashi Harukawa, DPIR
date: 3rd Week Hilary 2020
---

# Overview

## Last Week

- Advanced Data Operations
    - Applying Functions to Vectors and Matrices
    - Grouped Summaries
    - Concatenating and Merging Data

## This Week

This week we finally get to a fun topic: **data visualisation**.

There's more to data visualisation than I could possibly cover in 90 minutes, so I focus on _static_, _two-dimensional_ visuals; these are the kind that you are most likely to use.

# Theory

# Motivation

## Visual Summaries as an Aid

- Returning to the theme of this course, the aim of much of data science is to understand the whole picture of your data.
- If you can do this without reading your entire dataset, all the better!
- When making data visuals, I think it's helpful to remember that they are, in many ways, a form of summary.
- Visualising data is not just about communicating results; it is also a powerful tool for you to understand important features of your own data.

## Motivating Example


<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>x1</th>\n      <th>x2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>count</th>\n      <td>300.000000</td>\n      <td>300.000000</td>\n    </tr>\n    <tr>\n      <th>mean</th>\n      <td>4.048335</td>\n      <td>4.066768</td>\n    </tr>\n    <tr>\n      <th>std</th>\n      <td>4.145384</td>\n      <td>3.908675</td>\n    </tr>\n    <tr>\n      <th>min</th>\n      <td>-2.304990</td>\n      <td>-6.892820</td>\n    </tr>\n    <tr>\n      <th>25%</th>\n      <td>0.102002</td>\n      <td>1.528010</td>\n    </tr>\n    <tr>\n      <th>50%</th>\n      <td>3.389367</td>\n      <td>4.125494</td>\n    </tr>\n    <tr>\n      <th>75%</th>\n      <td>8.039512</td>\n      <td>6.871554</td>\n    </tr>\n    <tr>\n      <th>max</th>\n      <td>11.230459</td>\n      <td>16.889281</td>\n    </tr>\n  </tbody>\n</table>

## Motivating Example

![The same data](figures/lecture_fig1.png)

# From Data Types and Structures to Visualisation

## Data Types/Structures

The type and structure of your data tells you what _type_ of figure you need:

- Number of Dimensions
- Ordered or Unordered?
- Discrete or Continuous?

## One-Dimensional Data

Visuals for one-dimensional data tend to be concerned with _distributions_; i.e. frequencies of values along some dimension.

Useful plots include:

- Histogram
- Box (and whiskers) plot
- Swarm plot
- Violin plot

## Two-Dimensional Data

Visuals for two-dimensional data often fulfil one of the following two purposes:

- Comparing distributions
- Plotting functions

In addition to all of the aforementioned plots, some examples of the latter include:

- Scatter plot
- Line plot
- Bar plot
- Rug plot

## Three-Dimensional Data

- While it is possible to draw plots that have a third, _z_ axis, I hate how they look.
- If you are trying to show data in three or more dimensions, I suggest that you use a _heatmap_.
- More generally, you can use _colour_ or _shape_ as a means to distinguish on a third dimension (or higher).

# Gallery

## Histogram (One Category)

## Histogram (Two Categories)

## Box and Whisker Plot

## Swarm Plot (One Category)

## Swarm Plot (Multiple Categories)

## Violin Plot (One Category)

## Violin Plot (Two Categories)

## Scatter Plot

## Line Plot

## Bar Plot

## Rug Plot


## Data Types/Structures cont.

The next question you should ask is _what am I trying to communicate?_

Am I:

- Making a comparison between groups?
- Trying to show conditional relationships between variables?
- Exploring my own data?


# Implementation

## Two Libraries

- `matplotlib` is the primary library for building data-based visuals in Python.
    - Requires a lot of explicit commands to get it to look good, but allows for nearly complete customisation of all aspects.
- `seaborn` is a more recent library, built on top of `matplotlib`.
    - Provides fast and convenient methods for most figures you will ever need.
- Both libraries can be used in conjunction.

## The Anatomy of a Data Visual

On the back end, all `matplotlib`-based visuals adhere to a similar _tree-like_ structure. By learning this structure, you can locate and customise any element of a figure.

## The Matplotlib Hierarchy

Here is a truncated version of the matplotlib hierarchy:

- Figure
    - Figure-level Methods (e.g. Title)
    - Axes (Subplots)
        - Subplot-level Methods (e.g. sub-title)
        - Graphical functions
            - Graphical primitives (shapes)
        - Axis pairs (x-axis and y-axis)
            - Axis labels
            - Axis ticks
                - Location
                - Labels
        - Legend


## Figure

The figure is essentially the "canvas" upon which all visuals are made. Some parameters/methods set at this level include:

- Total size (in pixels)
- Super-title
- Saving to file

## Axes (Subplots)

Subplots are the frames within which individual visuals are contained.
- If there is only one plot in the figure, then there will only be one subplot.
- If you want to put multiple plots, or "panel" your plots, then you will make use of multiple subplots.

## Axes (Subplots) cont.

Most drawing methods are called at the subplot level:

- Plotting (drawing the graphical objects)
- Individual plot labels
- Legends

## Graphical Functions

`matplotlib` and `seaborn` provide an enormous number of plotting functions. These functions:

- Take one or more equal-length vectors as inputs (the data)
- Draw objects accordingly to the relevant subplot
    - If the function is a `matplotlib` function, you should call it as a method of the relevant subplot.
    - If the function is a `seaborn` function, and there is more than one subplot, then you should pass the relevant subplot as a parameter to the function.
- Take a large number of customisable parameters, such as:
    - Color
    - Transparency
    - Line/dot style

## X and Y Axis

Subplots have `xaxis` and `yaxis` methods. Call these to customise the following aspects:

- Ticks (the little notches along the axes)
    - Spacing/interval
    - Labels
        - Text
        - Orientation
    - Top/Bottom, Left/Right
- Axis labels


# Anatomy, Again, with Examples

## Figure

This does not create any visible objects, but it lays down the canvas that other things will go onto.

Note:

- Most of the plotting functionality is within the `pyplot` module of `matplotlib`.
- The output of `plt.figure` has been assigned to a variable, `f`. This will be our means of accessing the figure and its methods.
- The parameter `figsize=(15, 8)` has been passed to `plt.figure`. This tells `matplotlib` to create a canvas that is 1500x800 pixels.

```{python}
import matplotlib.pyplot as plt
f = plt.figure(figsize=(15, 8))
```

## Axes (One Subplot)

```{python}
f, ax = plt.subplots(1, 1, figsize=(15, 8))
f.suptitle("This is a figure with a subplot")
ax.set_title("This is a subplot", color="r")
```

![Figure with 1 Subplot](figures/lecture_emptysubplot1.png)


## Axes (Two Subplots)

```{python}
f, ax = plt.subplots(1, 2, figsize=(15, 8))
f.suptitle("This is a figure with two subplots")
ax[0].set_title("This is a subplot", color="r")
ax[1].set_title("This is another subplot", color="r")
```

![Figure with 2 Subplots](figures/lecture_emptysubplot2.png)


## Axes (Subplot Grid System)

```{python}
f, ax = plt.subplots(2, 2, figsize=(15, 8))
f.suptitle("This is a figure with four subplots")
for i in range(2):
    for j in range(2):
        ax[i][j].set_title(f"Subplot [{i}][{j}]", color="r")
```

![Figure with Four Subplots](figures/lecture_emptysubplot3.png)

## Graphical Functions (Scatter)

```{python}
f, ax = plt.subplots(1, 1, figsize=(15, 8))
ax.scatter(data['x2'], data['x1'], color='r')
```

![Scatter Plot](figures/lecture_scatter1.png)

## Graphical Functions (Line)

```{python}
f, ax = plt.subplots(1, 1, figsize=(15, 8))
ax.plot(np.linspace(0, 10, 100), np.linspace(0, 5, 100), color='r')
```

![Line Plot](figures/lecture_line1.png)

## Graphical Functions (Scatter + Line)
