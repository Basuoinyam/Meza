import heapq
import time
from utils.helpers import get_neighbors, reconstruct_path


def manhattan(a, b):
    """ حساب مسافة مانهاتن (Heuristic) """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(maze, start, goal):
    # Priority Queue: (f_score, cost_so_far, node)
    start_priority = 0 + manhattan(start, goal)
    frontier = [(start_priority, 0, start)]

    came_from = {start: None}
    cost_so_far = {start: 0}

    nodes_explored = 0
    start_time = time.time()

    while frontier:
        _, current_cost, current = heapq.heappop(frontier)
        nodes_explored += 1

        if current == goal:
            end_time = time.time()
            path = reconstruct_path(came_from, start, goal)
            return path, current_cost, nodes_explored, (end_time - start_time) * 1000

        for neighbor in get_neighbors(maze, current):
            move_cost = maze[neighbor[0]][neighbor[1]]
            new_cost = cost_so_far[current] + move_cost

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + manhattan(neighbor, goal)
                heapq.heappush(frontier, (priority, new_cost, neighbor))
                came_from[neighbor] = current

    return [], 0, nodes_explored, 0