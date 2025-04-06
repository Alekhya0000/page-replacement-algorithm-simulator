# Efficient Page Replacement Algorithm Simulator

A simple yet engaging simulator for exploring page replacement algorithms in operating systems, built with Python and a Tkinter GUI. This project implements three classic algorithms: **FIFO (First-In-First-Out)**, **LRU (Least Recently Used)**, and **Optimal**, allowing users to visualize memory management and compare algorithm performance.

## Overview
In operating systems, page replacement algorithms decide which memory pages to swap out when a new page needs to be loaded and memory is full. This simulator lets you input a number of frames (memory slots) and a page reference string, then see how each algorithm handles page faults step-by-step.

## Features
- **Interactive GUI**: A dark-themed interface with neon text and colorful buttons for a fun, modern look.
- **Three Algorithms**:
  - **FIFO**: Replaces the oldest page in memory.
  - **LRU**: Replaces the least recently used page.
  - **Optimal**: Replaces the page that won’t be needed for the longest time (ideal but impractical in real systems).
- **Step-by-Step Output**: Shows memory state, hits, and faults for each page request.
- **Performance Stats**: Displays total page faults and fault rate percentage.
- **Fun Feedback**: Adds playful messages based on simulation results (e.g., "Nice one! Low faults! 🚀").
- **Modular Design**: Separate files for each algorithm make it easy to extend or modify.

## Prerequisites
- **Python 3.x**: Ensure Python is installed (available at [python.org](https://www.python.org/)).
- No external libraries required—just the Python standard library (Tkinter is included).


