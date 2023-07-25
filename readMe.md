# Lights Out Puzzle in the Terminal

## Table of Contents

- [Introduction](#introduction)
- [Objective](#objective)
- [Game Rules](#game-rules)
- [Getting Started](#getting-started)
  - [Clone the Repository](#clone-the-repository)
  - [Local Virtual Environment Setup](#local-virtual-environment-setup)
  - [Download Dependencies](#download-dependencies)

## Introduction

Lights Out Puzzle in the Terminal is a Python project that brings the classic "Lights Out" puzzle to the command-line interface. The game challenges users to solve a grid of lights by toggling them on or off. Players can either solve the puzzle on their own or request the application to find the solution. The project's main goal is to provide a fun and interactive way to learn various Python concepts, including object-oriented programming, data structures, matrix operations, linear algebra Gaussian reduction, and general Python programming.

## Objective

The primary objective of this project is to create a fully functional "Lights Out" puzzle game in the terminal. By working on this project, developers and Python enthusiasts can achieve the following learning goals:

1. Gain practical experience in Python object-oriented programming (OOP) and design patterns.
2. Implement and manage data structures to represent the game board and its state.
3. Perform matrix operations and apply linear algebra techniques, such as Gaussian reduction, to solve the puzzle.
4. Enhance overall Python programming skills, including coding style, debugging, and testing.

## Game Rules

The "Lights Out" puzzle is played on a grid of lights, which can be in an on or off state. The goal is to turn off all the lights on the grid. However, toggling a light will also change the state of its adjacent lights. The puzzle's challenge lies in finding the right combination of light toggles to achieve the goal.

## Getting Started

Follow the steps below to set up the project and start playing the Lights Out Puzzle in the terminal.

### Clone the Repository

Clone this repository to your local machine using the following command:
 ```
 git clone https://github.com/your-username/lights-out-puzzle.git
 ```

 ### Local Virtual Environment Setup

Change into the project directory and set up a virtual environment:

```
cd lights-out-puzzle
python3 -m venv .venv
```

Activate the virtual environment:

- On Windows:

```
venv\Scripts\activate
```

- On macOS and Linux:

```
source .venv/bin/activate
```

### Download Dependencies and Execute app file

Install the required dependencies using pip:

```
pip install -r requirements.txt

python3 app.py
```

