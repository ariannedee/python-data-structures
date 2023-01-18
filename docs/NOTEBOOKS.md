# Jupyter notebooks

## About notebooks
**Jupyter notebooks** are **.ipynb** files, where Python code is broken up into **cells**.
Cells can be run, edited and rerun, in whatever order you like.
You can see the result of a cell immediately below it.

In addition, you can include **[Markdown](https://www.markdownguide.org/cheat-sheet/)** formatted text
throughout the document, to provide headings, descriptions, notes and links.

<img width="60%" src="img/notebooks.png">

## Why use them?

They are a convenient way to write Python code that:

- has a linear flow
- has multiple sections/steps
- requires text explanation
- returns images or plots
- you want to share with others and allow them to reproduce your work

They are often used in data science, since you often follow these steps:

- load some data
- clean it
- find information about it
- plot some results
- export it

They are a useful teaching tool because it allows you to:

- break code down into small chunks (in cells)
- cells can be edited, and rerun by the learner
- formatted text can provide a lot more information and is more readable than comments

## Jupyter Lab vs Jupyter Notebook

**Jupyter Notebook** is the original way of working with notebooks.

When you choose to launch a notebook, it opens up in a new browser tab.

It has more limited capabilities.

<img width="60%" src="img/jupyter_notebook.png">

**Jupyter Lab** is more like an IDE in the browser.

It provides a directory structure on the left, like PyCharm.
And when you open a file, it opens in tabs on the right.

<img width="60%" src="img/jupyter_lab_1.png">

One great feature is the **Table of contents** view
that gives you an overview of the headings in the document
and allows you to navigate to different sections quickly.

<img width="60%" src="img/jupyter_lab_2.png">

## Working with notebooks

### Run a single cell

Select a code cell and click the run button to run it 
(or press SHIFT + ENTER).

<img width="60%" src="img/jupyter_lab_run_cell.png">

### Run all

This restarts the Python session, clearing any variables, 
and runs the whole notebook from top to bottom.

<img width="60%" src="img/jupyter_lab_run_all.png">

### Add a cell

This adds a cell below the currently selected one.

<img width="60%" src="img/jupyter_lab_add_cell.png">

### Change the cell type

- Code: Python code
- Markdown: formatted text ([guide](https://www.markdownguide.org/cheat-sheet/))
- Raw: raw text

<img width="60%" src="img/jupyter_lab_cell_type.png">

<img width="20%" src="img/jupyter_lab_cell_type_2.png">

**Note:** You must run Markdown cells to see the formatted version

### Reorder cells

Hover over the gutter beside a cell and click + drag.

<img width="60%" src="img/jupyter_lab_move_cell.png">

**Note:** In PyCharm Professional, you must select a cell and click the up or down arrows to change its position.


