---
title: Week 4 Planning
---

# Data Visualisation

## Teaching Aims

- Methodological: Systematising and understanding summarising and conveying information graphically.
    - Key Questions:
        - How many variables (dimensions)?
        - What type of variables? Discrete vs. Continuous, Ordered?
        - What kind of comparison?
- Implementation: Understanding the implicit model behind graphing software like matplotlib (and seaborn)
    - Figures
        - Title
        - Spacing
        - Axes (subplots)
            - Title
            - Graphical Objects
                - Lines
                - Dots
                - Shapes
                - Text
            - axes (xaxis and yaxis)
                - Ticks
                    - Tick intervals
                    - Tick labels
                - Label


## Methodological Aspect

- Figures, by and large, serve a similar function to statistics. They convey a great deal of relevant information about a dataset without requiring one to inspect the individual values.
    - For instance, a histogram or KDE plot says a lot more about the shape of a distribution than most statisitics can.
    - It's easier to understand the functional shape of a time trend by plotting it than just eyeballing the numbers.
    - Also, they look pretty.
- Data visualisation is useful at two steps in the data analysis process:
    - Exploratory Analysis: here, being able to quickly construct a graph that shows what you need is key.
    - Presentation of Results: knowing a lot about how to customise a plot to exactly match your requirements matters more here.
- There are dozens of types of figures:
    - Distribution:
        - Histogram, KDE, rugplot, swarmplot, violinplot, box-and-whiskers
    - Unorderable Frequencies:
        - Bar, Grouped bars,
- Use Cases:
    - 1 dimensional:
        - Orderable:
            - Histogram, kernel density estimate
        - Unorderable:
            - Pie chart (if proportions), bar chart (frequencies)
    - 2 dimensional:
        - Orderable * Unorderable:
            -


## The Anatomy of a Figure

- The figure
- The subplots (axes)
- The axes (labels, ticks, etc)
- The graphical elements
