---
title: Intro to Python Course Planning
date: Week 1
---

_From the syllabus_:

### _Week 1_: Introduction to Python and the Development Environment

**Learning Aims**:

1. What is Python and what can I use it for?
2. What are the tools I can use to write Python code?
3. Writing your first Python script

There are three learning goals in the first week. The first relates to what Python is, and how it can be useful for social science researchers. Students will learn about the various use cases for Python, and come up with ways that it may help them achieve their research aims.

The second learning goal is to gain familiarity with the tools used to code in Python and present their research. These include Jupyter notebooks, IDEs and the terminal. Students will primarily use Jupyter notebooks in this course, but are welcome to use alternative development tools.

The final goal is to write their first program in Python. Commands and operators such as `print`, `+`, `&` etc. will be introduced.

### Coding Goals

- print()
- import, from, as
- int, float, str (and bool)
- basic arithmetic
- basic string operations
- lists and dicts

### Next Week

- Data I/O (requires knowledge of strings, paths)
- Constructing pandas dataframes from dicts and lists
- Selecting


### Lecture

The lecture begins with a few administrative points, and then goes into the following parts:

- _What is Python and what can I use it for_?
    - What is Python?
        - _General purpose scripting language with large data science community_
            - What is a script? For our purposes, it automates some task.
                - Usually some inputs and an output, but sometimes it can just generate things (from some external data source, e.g. the web).
                - Good to keep this input-output idea in your head. Each script should take some inputs, and give some outputs.
    - What can I use Python for?
        - List possible applications of Python for social science research. My primary goal is to motivate students, but also to try and illustrate the broad possibilities.
            - Aside: what do I use Python for?
                - General scripting
                - Quick data visualisation
                - Data Cleaning
                - Natural Language Processing
                - Web Scraping/Data Collection
        - If possible, try and find a number of papers that have used Python. This isn't always obvious, and `R` tends to be more popular in the computational political science community, whereas python is more popular amongst the engineering/hard sciences.
    - Quick Aside: Python vs `R`
        - This question comes up frequently. My two cents on the debate is that whereas `R` is a language specifically for statistical computing, python is a general-purpose programming language popular with the data science community. There is a lot of overlap in the functionality between the two languages, and learning either one will enable you to do many things anyway.
- _Basic Coding Tools_
    -
    - Anaconda: An environment manager. Python has many _libraries_ and _versions_; this software helps you keep them tidy.
    - Jupyter: Code editor (and executor). Takes the form of terminals, notebooks and lab.
        - How to start Jupyter (and why is this running in a browser??)
        - Navigating the Jupyter Lab interface
    - Some other IDEs (for nerds):
        - Atom: my preferred tool, for anyone who is interested.
        - PyCharm: most commonly used tool for development, good for people in the class with prior experience coding in other languages.
        - vim: if you're hardcore
        - Takeaway: Python is a language, which is separate from the tools you use to write and execute it.
- _First Steps in Python_:
    - `print("Hello World!")`
    - `type_dict = {42: "integer", 3.5: "float", True: "boolean", "word": "string"}`
    -
