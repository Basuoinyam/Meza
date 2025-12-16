import matplotlib.pyplot as plt
import os


# --- Helper Functions ---

def load_maze(file_path):
    """ تحميل المتاهة من ملف نصي """
    maze = []
    start = None
    goal = None

    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return None, None, None

    with open(file_path, 'r') as f:
        for i, line in enumerate(f):
            raw_row = line.strip().split()
            if not raw_row: continue

            row = []
            for j, cell in enumerate(raw_row):
                if cell.upper() == 'S':
                    start = (i, j)
                    row.append(1)
                elif cell.upper() == 'G':
                    goal = (i, j)
                    row.append(1)
                else:
                    try:
                        row.append(int(cell))
                    except ValueError:
                        row.append(0)
            maze.append(row)

    return maze, start, goal


def get_neighbors(maze, pos):
    """ تحديد الجيران المتاحين """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    rows = len(maze)
    cols = len(maze[0])
    for dr, dc in directions:
        r, c = pos[0] + dr, pos[1] + dc
        if 0 <= r < rows and 0 <= c < cols and maze[r][c] != 0:
            neighbors.append((r, c))
    return neighbors


def reconstruct_path(came_from, start, goal):
    """ إعادة بناء المسار """
    current = goal
    path = []
    if current not in came_from:
        return []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path


def calculate_path_cost(maze, path):
    """ حساب التكلفة """
    if not path: return 0
    return sum(maze[r][c] for r, c in path[1:])


def visualize(maze, path, filename, algorithm_name):
    """ رسم المتاهة وحفظ الصورة """
    maze_copy = [row[:] for row in maze]
    if path:
        for r, c in path:
            maze_copy[r][c] = -1

    plt.figure(figsize=(6, 6))
    plt.imshow(maze_copy, cmap="coolwarm_r")

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            cell_val = maze[i][j]
            if maze_copy[i][j] == -1:
                txt = "P"
                color = "white"
            elif cell_val == 0:
                txt = "W"
                color = "black"
            else:
                txt = str(cell_val)
                color = "black"
            plt.text(j, i, txt, ha="center", va="center", color=color, fontweight='bold')

    plt.title(f"{algorithm_name}\n(Numbers=Cost, W=Wall, P=Path)")
    plt.axis('off')
    plt.savefig(filename)
    plt.close()