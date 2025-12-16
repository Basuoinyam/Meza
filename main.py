import os
import csv   
from utils.helpers import load_maze, visualize

# استدعاء الخوارزميات
from algorithms.bfs_dfs import bfs, dfs
from algorithms.ucs import ucs
from algorithms.hill_climbing import hill_climbing
from algorithms.astar import astar

if __name__ == "__main__":
    maze_filename = os.path.join("mazes", "maze.txt")
    csv_filename = "results.csv"  # اسم ملف النتائج

    # إنشاء المتاهة إذا لم تكن موجودة
    if not os.path.exists(maze_filename):
        os.makedirs("mazes", exist_ok=True)
        with open(maze_filename, "w") as f:
            f.write("S 1 9 1 1\n")
            f.write("1 0 1 0 5\n")
            f.write("1 0 1 1 1\n")
            f.write("1 0 9 0 1\n")
            f.write("1 1 1 0 G\n")

    maze, start, goal = load_maze(maze_filename)

    if maze and start and goal:
        print(f"Maze Loaded Size: {len(maze)}x{len(maze[0])}")
        print(f"Start: {start}, Goal: {goal}")

        algorithms = [
            ("BFS", bfs),
            ("DFS", dfs),
            ("UCS", ucs),
            ("HillClimb", hill_climbing),
            ("A*", astar)
        ]

        print("-" * 65)
        print(f"{'Algorithm':<10} | {'Length':<10} | {'Cost':<10} | {'Nodes Exp':<10} | {'Time (ms)':<10}")
        print("-" * 65)

        # 2. فتح ملف CSV للكتابة
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            # كتابة الصف الأول (العناوين)
            writer.writerow(["Algorithm", "Length", "Cost", "Nodes Explored", "Time (ms)"])

            for name, func in algorithms:
                path, cost, nodes, time_ms = func(maze, start, goal)

                # تجهيز البيانات للطباعة والحفظ
                if path:
                    len_val = len(path)
                    cost_val = cost
                    print(f"{name:<10} | {len_val:<10} | {cost_val:<10} | {nodes:<10} | {time_ms:.4f}")
                    visualize(maze, path, f"{name.lower().replace('*', 'star')}_result.png", name)

                    # حفظ صف البيانات في CSV
                    writer.writerow([name, len_val, cost_val, nodes, f"{time_ms:.4f}"])
                else:
                    print(f"{name:<10} | {'No Path':<10} | {'-':<10} | {nodes:<10} | {time_ms:.4f}")

                    # حفظ صف البيانات في CSV (حالة الفشل)
                    writer.writerow([name, "No Path", "-", nodes, f"{time_ms:.4f}"])

        print(f"\nDone! Results saved to '{csv_filename}' and images generated.")
    else:
        print("Failed to load maze.")