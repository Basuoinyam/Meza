from collections import deque
import time
# استدعاء الدوال المساعدة
from utils.helpers import get_neighbors, reconstruct_path, calculate_path_cost

def bfs(maze, start, goal):
    queue = deque([start])
    visited = set([start])
    came_from = {start: None}
    nodes_explored = 0
    start_time = time.time()

    while queue:
        current = queue.popleft()
        nodes_explored += 1

        if current == goal:
            end_time = time.time()
            path = reconstruct_path(came_from, start, goal)
            total_cost = calculate_path_cost(maze, path)
            return path, total_cost, nodes_explored, (end_time - start_time) * 1000

        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)

    return [], 0, nodes_explored, 0

def dfs(maze, start, goal):
    stack = [start]
    visited = set([start])
    came_from = {start: None}
    nodes_explored = 0
    start_time = time.time()

    while stack:
        current = stack.pop()
        nodes_explored += 1

        if current == goal:
            end_time = time.time()
            path = reconstruct_path(came_from, start, goal)
            total_cost = calculate_path_cost(maze, path)
            return path, total_cost, nodes_explored, (end_time - start_time) * 1000

        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                stack.append(neighbor)

    return [], 0, nodes_explored, 0