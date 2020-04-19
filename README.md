# PythonProjectTemplate
Python Project Template/Skeleton

The purpose of this repository is to have all the files, folders and style conventions that are usually part of a
standard python project in a single location.

Some things might not make sense for every project, but overall the most import elements are here.

I created this template for my own personal use, but feel free to use it.

## How to use
* Just copy the `Project` folder

or

* [Use this template directly](https://github.com/Kronopt/PythonProjectTemplate/generate)
  and then move everything from the `Project` folder to the root of your project

### Notes
* Chose only one CI/CD pipeline (delete the one you don't want):
    * **CicleCI** (`.circleci` folder)
    * **Github Actions** (`.github` folder)
* Chose only one testing library (delete the one you don't want and then edit
  the `make.bat`/`Makefile` test and coverage functions with the correct command):
    * **pytest** (`tests\test_pytest.py`)
    * **nose2** (`tests\test_nose2.py`)
    * **unittest** (`tests\test_unittest.py`)
* Most files have variables in them (in the form of `<variable>`, like `<project_name>`) which you should edit
