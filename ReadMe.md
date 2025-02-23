## Purpose

Basic project/repo setup for Python programming using Anaconda.

## Prerequisites

1. Anaconda downloaded/installed
2. VS Code (not essential, but assumed for purposes of this info)
3. Python extension installed in VS Code
3. Mac OS (also not essential, but assumed for these purposes)

## Process

1. Open VS Code
2. File > Open Folder
3. Create new folder for project/repo in desired location
4. Create new virtual environment, in Terminal:
    * to find out Python versions available: conda search python
    * select your preference ('myenv' can be any name you want)
    * conda create --name myenv python=3.12
5. When asked to Proceed: y (assuming everything looks proper)
6. Activate in Terminal: conda activate myenv (or whatever name you used)
    * you will notice Terminal prompt starts with (myenv) instead of (base) now
7. Command Palette > Select Python Interpreter: select activated environment

## Usage

If you now go to File > New File > Python File and create a new file, you should see 'Python', version number and environment name in the bottom bar.

Try to run a simple Python ('.py') file to test:

* such as python-test.py file in this repo