# Project 0: Degrees

## Description
This project implements a program in **Python 3.12** that determines the number of “degrees of separation” between two actors, based on the *Six Degrees of Kevin Bacon* concept. Using breadth-first search (BFS), the algorithm finds the shortest connection path between two actors through the movies they have co-starred in.

## Objective
Given two actors’ names, the program calculates the minimum number of steps (shared movies) required to connect them, while displaying the details of each link in the chain of relationships.

## Example
```bash
$ python degrees.py small
Loading data...
Data loaded.
Name: Emma Watson
Name: Jennifer Lawrence
3 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class

