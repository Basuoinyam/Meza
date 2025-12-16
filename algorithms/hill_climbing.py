import time
from utils.helpers import get_neighbors, calculate_path_cost


def manhattan(a, b):
    """
    حساب المسافة المانهاتنية بين نقطتين a و b.
    كل نقطة عبارة عن زوج (x, y).
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def hill_climbing(maze, start, goal):
    current = start
    path = [current]
    nodes_explored = 0
    start_time = time.time()

    while current != goal:
        nodes_explored += 1

        # استخدام دالة الجيران الموحدة (التي تتجاهل الجدران تلقائياً)
        neighbors = get_neighbors(maze, current)

        if not neighbors:
            # طريق مسدود
            return [], 0, nodes_explored, (time.time() - start_time) * 1000

        # اختيار الجار الأقرب للهدف بناءً على مسافة مانهاتن
        # (Hill Climbing: Greedy local search)
        next_node = min(neighbors, key=lambda x: manhattan(x, goal))

        # في التسلق البسيط، إذا كانت الخطوة القادمة لا تقربنا للهدف (أو تساويه)، نتوقف
        # (هنا نسمح بالمساواة للمتابعة في الهضاب المسطحة أحياناً، لكن الشرط الأصلي هو التحسن الصارم)
        # سأستخدم شرطك: إذا كانت المسافة القادمة أكبر أو تساوي الحالية، نتوقف (Local Optima)
        if manhattan(next_node, goal) >= manhattan(current, goal):
            return [], 0, nodes_explored, (time.time() - start_time) * 1000

        current = next_node
        path.append(current)

        # حماية من الدوائر اللانهائية (Infinite Loops) في Hill Climbing
        if len(path) > len(maze) * len(maze[0]):
            return [], 0, nodes_explored, (time.time() - start_time) * 1000

    end_time = time.time()
    total_cost = calculate_path_cost(maze, path)
    return path, total_cost, nodes_explored, (end_time - start_time) * 1000