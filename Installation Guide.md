---
title: Python Installation Guide
author: Musashi Harukawa, DPIR
date: 0th Week Hilary Term 2020
geometry: margin=2cm
---

# Installing Anaconda

Anaconda is a freely-available data science software and environment manager. It can be used to manage versions and editors for Python, `R`, and other popular data science languages (such as `Julia`).

In order to simplify installing all the relevant packages and software, we will be using Anaconda for this class. The instructions on how to install Anaconda can be found at:

- **Windows**: https://docs.anaconda.com/anaconda/install/windows/
- **MacOS**: https://docs.anaconda.com/anaconda/install/mac-os/
- **Linux**: https://docs.anaconda.com/anaconda/install/linux/

Follow the instructions contained within the guide. Note the following:

- Install Python version 3.7 or later. Do NOT install Python 2.7.
- Unless you know what you are doing, I recommend that you install anaconda to the default location.
- You do not need to install as admin.
- You do not need PyCharm, but if you have a experience with Sublime or other industry-standard IDEs, you may prefer to use it (please note that you will still need to use Jupyter).
- (Windows only): You do not need to add Anaconda to your PATH environment variable.
- You do not need Anaconda Cloud.

If you run into trouble, _first try Googling the answer_ (or whatever your preferred non-invasive search engine is), and then ask me. Chances are that somebody has run into the same problem as you, and the answer exists on the Internet. If the problem persists, then feel free to get in touch.

# Verifying your Installation

Once you have installed Anaconda, check that everything works.

Open up Anaconda Navigator (like you would any other application). You should see a menu with a number of items including JupyterLab and Jupyter Notebooks. Try opening up either, and navigating to the directory (folder) where you will be keeping all of your notes for this course.

In this directory, create a Python Notebook and rename it to `my_first_notebook`. The default file ending should be `.ipynb`. Then in the first cell of this notebook, type the following command:

```{python}
print("Hello World!")
```

Click on "Run Selected Cell" in the notebook menu. You should get the following output:

```
> Hello World!
```

If all of this works without issue, then you are ready to come to class for week 1! If this does not work, and you are unable to troubleshoot the issue, please contact me prior to coming to class (so we can minimize the amount of time we spend in class installing software and troubleshooting indivdiual issues).

See you on Wednesday!
