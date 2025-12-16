import heapq
import time
# استدعاء الدوال المساعدة
from utils.helpers import get_neighbors, reconstruct_path


def ucs(maze, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    nodes_explored = 0
    start_time = time.time()

    while frontier:
        current_cost, current_node = heapq.heappop(frontier)
        nodes_explored += 1

        if current_node == goal:
            end_time = time.time()
            path = reconstruct_path(came_from, start, goal)
            return path, current_cost, nodes_explored, (end_time - start_time) * 1000

        for neighbor in get_neighbors(maze, current_node):
            move_cost = maze[neighbor[0]][neighbor[1]]
            new_cost = cost_so_far[current_node] + move_cost

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current_node

    return [], 0, nodes_explored, 0