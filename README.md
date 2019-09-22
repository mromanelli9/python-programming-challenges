# Python programming challenges
This is a collection of programming challenges, written in Python,
that I've encountered mainly during my job interviews.

# Preparation
1. Make sure that you have python 3.7.x installed. Some functionality (like type-hints
   and f-strings) from later versions of python are used, so you should  make sure that
   you have the correct version.
2. Run `conda env create -f environment.yml` to make sure that you have installed the
   necessary dependencies.

# How to use
For each task you'll find the description at the beginning of the file,
but there are also other useful information on the task function docstring.
The tasks are marked with a difficulty ranging from 0-5, where 0 should be very easy, while 5
can be quite difficult.

To run tests, simply run `pytest tests` from the project root.
The tasks that are not implemented are skipped so they'll not invalidate the other tests.

The _solutions_ folder contains my solutions for some of the tasks.
They're not intended to be the best solutions at all.
If you want to propose a solution, it'll be more than welcome.

# Tasks
Here is a list of the tasks:

|   | Name              | Difficulty | Solution |
|---|-------------------|------------|----------|
| 1 | _exact_ _hours_   | 3          |          |
| 2 | _lisp_            | 2          | [x]      |
| 3 | _matmul_          | 4          |          |
| 4 | _pipes_           | 4          |          |
| 5 | _training_        | 5          |          |
| 6 | _wifi_ _password_ | 1          | [x]      |
| 7 | _signal_ _crossing_ | 3        | [x]      |

# License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)