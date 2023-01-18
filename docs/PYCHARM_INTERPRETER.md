# Configuring your Python virtual environment PyCharm (Community and Pro)

## 1. Click on the current interpreter shown on the bottom right

   <img width="60%" src="img/pycharm_python_1.png">
   
## 2a. Choose an existing interpreter from the list

   <img width="60%" src="img/pycharm_python_2a.png">

If your desired interpreter was found, select it and you're done.

If not, move onto 2b.
   
## 2b. Add a new interpreter

Add New Interpreter > Add Local Interpreter...

   <img width="60%" src="img/pycharm_python_2b.png">

## 3. Select your interpreter type on the left

If you installed Python via Anaconda, choose that and follow the instructions [here](https://docs.anaconda.com/anaconda/user-guide/tasks/pycharm/#switching-environments-within-a-pycharm-project).

Otherwise, you can choose **System Interpreter**

   <img width="60%" src="img/pycharm_python_3.png">

## 4a. Select an existing system interpreter

   <img width="60%" src="img/pycharm_python_4a.png">
   
   If your desired version was found, click OK. If not, go on to 5b.

## 4b. Find your system interpreter

   <img width="60%" src="img/pycharm_python_4b.png">

If you’re not sure where to find it, try one of the following locations
(replace 3.9 or 39 with the desired version number):

### Windows (look for python.exe)
- C:\Python39
- C:\Program Files\Python39
- C:\Users\username\AppData\Local\Programs\Python\Python39-XX

### Mac (look for python3.9 or python3)
- /usr/local/bin/
- /Library/Frameworks/Python.framework/Versions/3.9/bin/
- /usr/local/Cellar/python/3.9.X_X/bin/
- /Users/username/anaconda/bin/
- /anaconda3/bin/

### Linux (look for python3.9 or python3)
- /usr/bin/
- /usr/local/bin