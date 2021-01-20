---
title: Introduction to Python for Social Science
subtitle: Lecture 1 - Introduction to Python
author: Musashi Harukawa, DPIR
date: 1st Week Hilary 2021
---

# Course Overview

## Schedule

8-week long course, delivered weekly on Teams.

- 1600-1645: Lecture
- 1645-1730: Coding Tutorial
- 1730-1745: 15 minute intermission
- 1745-1830: Workshop

<aside class="notes">
> - Outline purpose of each. Lectures theoretical, coding tutorial practical.
> - Workshops chance to work on assignment, are optional, but I will be available to help/answer questions.
</aside>

## Topics:

1. Introduction to Python and the Development Environment
2. Data Structures and `pandas` I
3. Data Structures and `pandas` II
4. Data Visualisation
5. Machine Learning with `scikit-learn` I
6. Machine Learning with `scikit-learn` II
7. Web Scraping with `BeautifulSoup` and `regex`
8. Web Scraping with `Selenium`

<aside class="notes">
> - I've chosen five topics for the eight weeks.
> - The first week will be focused on getting you to understand a bit better what Python is, and will teach some basics.
> - The second and third week focus on working with data; cleaning, reshaping, writing and reading, and most importantly _understanding_.
> - The fourth week will introduce two libraries for making data-based visuals; these will be publication grade, and can be used for academic papers or in a professional setting.
> - The fifth and sixth week look at machine learning. The library we will use is not _the_ cutting edge, but has an amazing array of well-documented algorithms and is ideal for teaching ML basics.
> - The seventh week gives a flying introduction to automating the collection of data from web pages. Web scraping is something I get asked about a lot, and takes longer than a week to teach, but hopefully I can give you a strong starting point to develop your own scrapers.
> - The final week was originally on NLP, but given that there will be a separate module for this taught by Ash in TT, I decided to expand the web scraping module.
</aside>

## Lecture

- Lectures will contain a mixture of theory, methodological motivation, and contextual information.
- Largely social science methodology, with a bit of computer science.
- The slides will be made available at the following:
  - https://github.com/muhark/dpir-intro-python
  - Canvas
- Lectures will also be uploaded to Panopto (details to follow)

<aside class="notes">
Explain lecture flow. In the lecture, we look at the intersection of social science methodology and computer science theory.
</aside>

## Coding Tutorial

- In this section I explain the nitty-gritty of actually implementing these problems in code.
- Open up the notebooks on your laptop and code along with me while we work through examples!

## Workshop

- In the workshop, you will work through a number of set programming problems and discussion questions.
- I will be available during this period to answer questions and clarify points

## Office Hours

- Time tbd, depending on time zones and demand. Currently thinking Tuesday morning.


## Feedback

- This course is very new!
- Feedback can either be:
    - sent to me at `musashi.harukawa@politics.ox.ac.uk`
    - written into a questionnaire circulated in Week 3

<aside class="notes">
> - This is a brand new course, and far from perfect.
> - I would appreciate and welcome any feedback on any aspect.
> - Please also feel free to come talk to me in person!
</aside>

# Week 1: Introduction to Python and the Development Environment

## Overview:

This week will cover the following points:

1. What is Python?...
2. ... and what can I use it for?
3. What are the tools I have to write, test and run Python code?
4. Coding tutorial I: Base Data Types and Structures


# What is Python?...

## Python is an _open-source, general-purpose scripting language_.

## Open-Source

- Built by a community
- Maintained by a community
- Free to use for all

## General-Purpose

- If you're doing it on a computer and there's some repetitive element, then you can automate it in Python.
- Python isn't limited to Data Science, but it's very popular with data scientists!

<aside class="notes">
Large community means that a larger number of people create, contribute to, and maintain the data analysis tools that we all use.
</aside>

## Scripting
<aside class="notes">
> - It's good to keep the input-output framework in your head.
> - Also not strictly limited to scripting; Python is widely used for applications development.
> - For our purposes, however, its common usage for scripting is a big plus, as that's what we usually do.
</aside>

- No strict definition for what a "script" is.
- Series of commands to automate some task.
- Like a pipeline: takes some inputs, does some things to these inputs, and gives back some outputs.

## Language
<aside class="notes">
</aside>

- Python is a language, and not an application.
- Practical difference for you:
    - most applications provide you options to select from.
    - languages require to generate commands from accepted rules.
- Upshot is that you can do nearly anything with Python!

# and what can I use Python for?

## I want to...

- Clean up my messy data!
- Run analyses with (hundreds of) millions of data points
    - it won't fit into an excel spreadsheet!
- I want to automate downloading several decades of newspaper articles!
- I want to create beautiful (interactive) visuals to accompany my analyses!
- I want to uncover hidden structures linking parliamentary committees!
- Again: _any repetitive task done on a computer can be automated with Python_.

## Comparison: Python vs `R`

| Task                               | `python` | `R`   |
| ---------------------------------- | -------- | ----- |
| General Purpose Programming        | Great    | Poor  |
| Regression Analysis                | OK       | Great |
| Machine Learning                   | Great    | Great |
| Web Scraping                       | Great    | OK    |
| Natural Language Processing[^1594] | Great    | Great |
| Data Visualisation                 | Great    | Great |


[^1594]: Python and `R` both provide extensive and powerful natural language processing libraries, e.g. `nltk`, `gensim` in Python; `tm`, `quanteda` in `R`, and `spaCy` in both. Unfortunately, there are many techniques that are only implemented in one language but not the other.

Conclusion: ... it depends, but ideally you want to learn both!

# Tools of the Trade

## Development

- Writing Code
- Executing Code

## Jupyter

- Interactive code editor.
- Multiple options: console, notebook and lab

## Google Colab

- Google's cloud-based Jupyter notebooks
- Sufficient for this class

## Managing Libraries
<aside class="notes">
> - Discuss briefly why Python requires a manager, and why you might want to use it locally.
</aside>

For managing Python packages, I recommend Anaconda.

- Environment and software manager.
- Recommended solution for Python installation and management.
- Can be used from the command line (`cli`) or browser-like interface (anaconda-navigator).

## Other Options

- I use Atom or VIM to write code
- PyCharm is popular with developers
- If you've spent a lot of time with RStudio, you may prefer Spyder.

# This Week

## Data Types and Structures

- Today I introduce two fundamental, but abstract aspects of coding:
  - Data Types
  - Data Structures

<aside class="notes">
Note that we will continue to discuss these topics for 3 weeks.
</aside>

## Why Automate?

- Advantage of automation cost, scale, and scope.
- To harness computational methods, need to represent our observations in a way that algorithms and programs can utilise.
- Process of quantifying and structuring our observations usually entails loss of some information.

<aside class="notes">
> - As social scientists, our goal when automating 
- This automation is not limited to collecting data. Running a regression or sorting your responses by data is the automation of doing this by hand.
- Some qualitative scholars I speak to contend that the validity of the quantitative endeavour ends there.
    - Are there unquantifiable things?
- I'm more optimistic about what is possible, and think that the key to having valid quantitative inferences is to be extremely clear on the connection between the data in your analysis and the actual events you are measuring.
</aside>

## Bridging the Gap between Qualitative and Quantitative Methods

- Choosing a representation of your information that retains relevant properties is key.
- To read more about this particular debate, a good starting point is [Stevens (1946)](https://pdfs.semanticscholar.org/2680/6102a45a6104489872dd3241b6e8030bbc40.pdf).

<aside class="notes">
- I would love to discuss this further, but this isn't really that kind of methods class.
</aside>

## Data Types

Some (statistical) data types:

- Logical
- Numerical
- Categorical
- Text
- Date and time


<aside class="notes">
- What do I mean when I talk about different "types" of data?
- Small exercise: what are instances of each of these?
</aside>

## Representing Data on a Computer

- _Good news:_ Python, like most modern programming languages, has ways to represent each of the data types listed above.
- _Bad news:_ At a fundamental level, this is being stored as 0's and 1's.
- _Take away:_ Take the time to understand the relationship between:
    -  your empirical observations,
    -  the abstracted representation of them in your mathematical model,
    -  the approximation of this in your computational model.

<aside class="notes">
- I'm making a bit of an assumption here about the theory-generating workflow, in that a stylised mathematical model is usually prior to a computational/empirical approach.
</aside>

## Data Structures

- Data types are concerned with the representation of individual data points, or observations.
- Data structures are concerned with the relations between observations.
    - Are the data points members of the same set?
    - Are the data points members of the same sequence?
    - Are the data points different features of single empirical unit?

## Exercise

![Menu](https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/2016-04_Menu_.jpg/800px-2016-04_Menu_.jpg)

<aside class="notes">
- Question to discuss with partner: how would you represent this information in a computer? Possible answers include:
    - Data Frame (a combination of relational and vector data)
    - Multiple sequences
    - Hierarchically: course -> item -> - desc. - price
</aside>

## And now...

1. Open Browser
2. Go to [colab.research.google.com/](colab.research.google.com/)
3. Open pre-existing notebook, or create new one.
4. Start coding!

# Coding Recap

## Variable Assignment

Variables can be assigned with `=`.

## Four Basic Data Types

There are four basic data types in Python. These are:

- String
- Integer
- Float
- Boolean

## String

- _A sequence of characters_.
- Behaves like a sequence; can be indexed with `[index]`

## Integer

- Whole numbers.
- Can be positive or negative.

## Float

- Decimal numbers.
- Behave unexpectedly. Remember: `0.1*3==0.3` returns `False`.

## Boolean

- True/False
- Behaves similarly to integers 0 and 1.

## Two basic data structures

We learned about two basic data structures:

- Lists
- Dictionaries

## Lists

- Lists are an ordered sequence of values.
- Created by writing a sequence of comma-separated values between square brackets:
  - i.e. `[1, 2, 5, "some string"]`
- Lists are mutable; values can be changed in place without creating a new variable.
- Lists can be indexed the same way as strings:
  - `[n]` to get the n+1th element.
  - `[m:n]` to get all elements from m+1 to n.

## Dictionaries

- Unordered mapping of _keys_ to _values_.
  - Cannot be indexed numerically, and if iterated over, will not return values in the same order.
- Created by writing a list of `key:value` pairs separated by commas between curly braces.
  - i.e. `{"cat": "meow", "dog": "bork"}`
- `some_dict[some_key]` returns the corresponding value for `some_key` in `some_dict`
- To see all of the keys, use the `.keys()` method of the dict, i.e. `some_dict.keys()`
- To see all of the values, use the `.values()` method of the dict, i.e. `some_dict.values()`


# Next Week: Data Structures and `pandas` I

##

We learn about:

- Tabular data structures
- `pandas`, a key library for working with data
- Reading different data formats
- Slicing and indexing data

# Readings

## Readings

[_Automate the Boring Stuff with Python_](https://automatetheboringstuff.com/2e)

- Chapter 1
- Chapter 4 (up to "The in and not in operators") 
- Chapter 5 (up to "Checking Whether a Key or Value Exists in a Dictionary")

[_Python for Data Analysis: Data Wrangling with Pandas, NumPy and IPython, 2nd edition_](http://solo.bodleian.ox.ac.uk/permalink/f/89vilt/oxfaleph021507068)

_Useful_:

- 2.2: IPython Basics
- 3.1: Data Structures and Sequences

_Interesting_:

- 1.2 Why Python for Data Analysis?
