# Filetree

## Story

You work at a company that develops UNIX maintenance software.
There is a program called _filetree_ which was developed years ago (and of course
the original developer has already left the company). Unfortunately, it is
buggy: it doesn't work as intended. Your job is to reveal and fix the bugs.

## What are you going to learn?

- code comprehension
- debugging
- recursive functions


## Tasks

1. Fix the program to properly print out the filtered contents of the actual directory.
    - Running the program from the folder of the file results in displaying the same content on the console as in the `expected_outcome.txt`.
    - The content of the `expected_outcome.txt` is not hard-coded in the program.

## General requirements

None

## Hints

- **Use the debugger!** It is really difficult to find these kind of bugs by just
  reading the code. Step through the code multiple times, watch for variable
  changes, examine the program in detail.
- Be careful, this program uses recursion at some point. It is sometimes difficult
  to understand at first, so keep trying (and watch the movie _Inception_ ;) ).

## Background materials

- <i class="far fa-exclamation"></i> [What's going on under the hood]
- <i class="far fa-exclamation"></i> <i class="far fa-video"></i> [Debugging in Visual Studio Code](https://www.youtube.com/watch?v=w8QHoVam1-I)
- <i class="far fa-exclamation"></i> [Debugging in Visual Studio Code](https://code.visualstudio.com/docs/editor/debugging)
- <i class="far fa-book-open"></i> [About debugging](https://python-textbok.readthedocs.io/en/stable/Errors_and_Exceptions.html#debugging-programs)
- <i class="far fa-video"></i> [The concept of recursion](https://www.youtube.com/watch?v=vPEJSJMg4jY)
- <i class="far fa-candy-cane"></i> [Thinking recursively in Python](https://realpython.com/python-thinking-recursively/)
