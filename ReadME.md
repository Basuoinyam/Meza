# Maze Search Algorithms Project

## 📌 Project Overview
This project implements and compares several classical search algorithms on a 2D maze environment.

The goal is to analyze their performance in terms of:
- **Path Length** (Number of steps taken).
- **Total Cost** (Sum of weights of the path).
- **Nodes Explored** (Computational effort/efficiency).
- **Execution Time** (Speed in milliseconds).

The project is designed for **3rd year university students** studying Artificial Intelligence or Search Algorithms.

---

## 🧠 Implemented Algorithms
The project includes the following algorithms, organized in a modular structure:

1. **Breadth First Search (BFS):**
2. **Depth First Search (DFS):**
3. **Uniform Cost Search (UCS):**
4. **Hill Climbing:**
5. **A* Search (A-Star):**

---
📊 Output & Results
Upon successful execution, the project generates:

Console Output: Displays a table with the metrics for each algorithm directly in the terminal.

Visualizations (.png): Images showing the path found by each algorithm (e.g., astar_result.png, bfs_result.png).

P = Path taken.

W = Wall.

Numbers = Path Cost.

CSV Report (results.csv): A structured file containing the performance data, which can be opened in Excel for creating charts and further analysis

## 🗺 Maze Representation
The maze is loaded from a text file (`mazes/maze.txt`).
To match the logic in the code, the encoding is as follows:

- `S` → Start position.
- `G` → Goal position.
- `0` → **Wall / Obstacle** (Cannot be traversed).
- `1` → Standard Path (Cost = 1).
- `2-9` → High Cost Path (Simulates traffic, mud, or difficult terrain).
'''
## 📂 Project Structure
meza/
│
├── algorithms/             # Algorithm implementations
│   ├── __init__.py
│   ├── bfs_dfs.py          # BFS and DFS logic
│   ├── ucs.py              # Uniform Cost Search logic
│   ├── hill_climbing.py    # Hill Climbing logic
│   └── astar.py            # A* Search logic
│
├── mazes/                  # Maze input files
│   └── maze.txt            # The map file
│
├── utils/                  # Helper functions
│   ├── __init__.py
│   └── helpers.py          # Functions for loading, neighbors, and plotting
│
├── main.py                 # Entry point (Runs the comparison)
├── results.csv             # Generated report (Excel compatible)
└── *.png                   # Generated images of the solutions
