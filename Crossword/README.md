# Crossword

## Description
This project implements a **constraint satisfaction problem (CSP) solver** to generate crossword puzzles.  
It selects words from a given vocabulary to fill a crossword grid while satisfying unary and binary constraints.

## Objective
Build a program that can:
- Enforce **node consistency** for all crossword variables.
- Enforce **arc consistency** between overlapping variables using the AC3 algorithm.
- Solve the crossword puzzle using **backtracking search** with heuristics like minimum remaining values and least-constraining value.
- Generate a completed crossword puzzle if possible, satisfying all constraints.
