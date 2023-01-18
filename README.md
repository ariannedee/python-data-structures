# Python Data Structures and Comprehensions Live Training

This is the code for the *O'Reilly Live Training* - **Python Data Structures and Comprehensions** presented by Arianne Dee

## For this class, you will need:
1. **Python 3.7 or higher** installed on your computer
   - Installed from the [Python website](https://www.python.org/downloads/) or through [Anaconda](https://www.anaconda.com/)
2. An **IDE** for Python
   - The examples can either be run as Jupyter Notebooks or Python scripts.
3. A copy of the **course files**
   - Cloned (ideal) or downloaded
4. Jupyter, NumPy and Pandas installed
    - `pip install jupyter numpy pandas`
5. Fill out a short **survey**: https://forms.gle/KCSXZy7tHeb1B9ce8
   - We will analyze the results during the class.

There are detailed set up instructions for each step below.

If you have further questions, please email **arianne.dee.studios** at **gmail** dot **com**.

## Detailed setup instructions 

1. [Install Python](#1-install-python-37-or-higher)
2. [Choose an IDE](#2-choose-an-ide)
3. [Download the code](#3-download-the-course-files)
4. [Install external packages](#4-install-external-python-packages)

### 1. Install Python 3.7 or higher

If you have been using Python for data science, 
you probably have it installed already through [Anaconda](https://www.anaconda.com/).

If not, or you're not sure, 
the easiest way to get Python is to download it from the 
[website](https://www.python.org/downloads/).

1. Go to https://www.python.org/downloads/
2. Click the yellow button at the top to download the latest version of Python (e.g. 3.11.1)
3. Complete installation
   1. **On Mac or Linux**
      - Follow the prompts and install using the default settings.
   2. **On Windows**
      1. If you're just installing Python now,
      follow: [Windows Python installer instructions](docs/WININSTALL.md)
      2. If you've already installed Python with the default settings,
      follow: [Add Python to PATH variable in Windows](docs/WINSETPATH.md)

### 2. Choose an IDE

The course examples use [jupytext](https://github.com/mwouts/jupytext) 
to create **.ipynb** (_notebook_) and **.py** (_script_) files 
for each of the examples.

#### Running notebook files
The notebook files can be run in:

- [Jupyter Lab](https://jupyter.org/install#jupyterlab)  <-- The instructor will use this in class
- [Jupyter Notebook](https://jupyter.org/install#jupyter-notebook)
- Spyder
- PyCharm professional
- VS Code
    - Install the official Python extension
- PyCharm community (read-only access)  <-- The instructor will use this in class

Any of these options will work for this course.

If all else fails, you can run Jupyter Lab in the browser 
and upload the course files using [JupyterLite](https://jupyter.org/try-jupyter/lab/).

#### Managing your Python environment

In addition to viewing the example notebooks, 
you may want an IDE to help manage your environment.

[Go here](docs/PYCHARM_SETUP.md) for instructions on how to use **PyCharm community** to:
- Set your Python interpreter for your project
- Install required external packages (**NumPy** and **Pandas**)
- Install **Jupyter**
- Run **Jupyter Lab** from the Terminal
- View the .ipynb files

### 3. Download the course files

GitHub repository link: https://github.com/ariannedee/python-data-structures

#### If you know git:

Clone the repository.

#### If you don't know git:

1. Click the green "< > Code" button at the top-right of the page
2. Click "Download ZIP"
3. Unzip it and move the **python-data-structures-main** folder to a convenient location

#### Open the code in your IDE

Open the top level folder, **python-data-structures** or **python-data-structures-main** in your IDE (e.g. PyCharm).

If using PyCharm or VS Code, make sure the desired Python interpreter is set (on the bottom right toolbar).

### 4. Install external Python packages

**Jupyter**, **NumPy** and **Pandas** need to be installed.

#### With `pip`

In a terminal: `pip install jupyter numpy pandas`

#### With PyCharm

Instructions:

1. Make sure your Python interpreter is set (in the bottom right toolbar).
2. On the bottom toolbar, there is an option for **Python Packages**.
3. Search for `jupyter`, click on the one with the exact name, and click **Install package**
4. Repeat for `numpy` and `pandas`


##### If you need to set your Python interpreter version in PyCharm

On a Mac:

- Go to **PyCharm** > **Preferences**

On a PC:

- Go to **File** > **Settings**

Once in Settings:

- Go to **Project: intro-to-python** > **Project Interpreter**
- Look for your Python version in the Project Interpreter dropdown and select it. Please use Python 3.6 or higher.
- If you found it, click OK and try running `example_1_first_code` again
- Otherwise, if your version wasn't there, click **gear icon** > **Add...**
- In the new window, select **System Interpreter** on the left, and then look for the Python version in the dropdown
- If it's not there, click the **...** button and navigate to your Python location
- **Note:** For this last step, you may have to search the internet for where Python gets installed by default on your operating system

If you are having trouble configuring your Python version, you can find visual instructions
here: [Python interpreter setup](docs/PYCHARM_INTERPRETER.md)
