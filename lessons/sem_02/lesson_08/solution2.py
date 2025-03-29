import matplotlib.pyplot as plt
import numpy as np

from IPython.display import HTML
from matplotlib.animation import FuncAnimation

plt.style.use("ggplot")


def get_neighbors(point: tuple[int, int]):
    left = (point[0], point[1] - 1)
    right = (point[0], point[1] + 1)
    up = (point[0] - 1, point[1])
    down = (point[0] + 1, point[1])
    return [left, right, up, down]


def validate(point: tuple[int, int], maze: np.ndarray):
    return (point[0] >= 0 and point[1] >= 0) \
            and (point[0] < maze.shape[0] and point[1] < maze.shape[1])


def animate_wave_algorithm(
    maze: np.ndarray,
    start: tuple[int, int],
    end: tuple[int, int],
    save_path: str = ""
):
    maze_copy = np.copy(maze)
    track = np.full(maze.shape, -1)
    maze[start] = 0

    fig, ax = plt.subplots()
    ax.set_title("Волновой алгоритм")
    frames_forward = []

    frames_back = []

    def forward(point: tuple[int, int]):
        if point != start:
            frames_forward.append((point, maze[point]))
        track[point] += 1
        neighbors = get_neighbors(point)
        for position in neighbors:
            if validate(position, maze) and maze[position] == 1:
                if track[position] != -1:
                    continue
                maze[position] = maze[point] + 1
                if position == end:
                    frames_forward.append((position, maze[position]))
                    back(position)
                    break
                forward(position)

    def back(point: tuple[int, int]):
        frames_back.append(point)
        track[point] += 1
        if point == start:
            return
        neighbors = get_neighbors(point)
        for position in neighbors:
            if validate(position, maze) and (maze[point] - maze[position]) == 1:
                if track[position] == 0:
                    back(position)

    forward(start)
    frames_forward.sort(key=lambda x: x[1])

    def update(frame_idx):
        ax.clear()
        ax.set_title("Волновой алгоритм")

        ax.set_xticks(np.arange(-0.5, maze.shape[1], 1))
        ax.set_yticks(np.arange(-0.5, maze.shape[0], 1))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        for i in range(maze.shape[0]):
            ax.text(-1, i, str(i), color="black", ha="center", va="center", fontsize=10)
        for j in range(maze.shape[1]):
            ax.text(j, maze.shape[0], str(j), color="black", ha="center", va="center", fontsize=10)

        ax.grid(True, color="black", linestyle="-", linewidth=2)
        ax.imshow(maze_copy, cmap='binary')

        ax.add_patch(
            plt.Rectangle(
                (-0.5, -0.5),
                maze.shape[1],
                maze.shape[0],
                edgecolor="black",
                fill=False, lw=3
                )
            )

        for i in range(min(frame_idx + 1, len(frames_forward))):
            (x, y), step = frames_forward[i]
            ax.text(y, x, str(step), color="blue", ha="center", va="center")

        if frame_idx >= len(frames_forward):
            path_idx = frame_idx - len(frames_forward)
            if path_idx < len(frames_back):
                point = frames_back[path_idx]
                ax.add_patch(
                    plt.Rectangle(
                        (point[1] - 0.5, point[0] - 0.5),
                        1, 1,
                        color="green",
                        alpha=0.5
                    )
                )

    frames_count = len(frames_forward) + len(frames_back)
    anim = FuncAnimation(fig, update, frames=frames_count, interval=500)

    if save_path:
        anim.save(save_path, fps=200)

    return anim


maze = np.array([
    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
])

# Загрузка лабиринта из файла
maze = np.load(
    r"test_data\maze.npy"
)

# Нахождение первой единички (start)
start = tuple(np.argwhere(maze == 1)[0])  # Первая единичка

# Нахождение последней единички (end)
end = tuple(np.argwhere(maze == 1)[-1])  # Последняя единичка

save_path = "labyrinth.gif"  # Укажите путь для сохранения анимации

animation = animate_wave_algorithm(maze, start, end, save_path)
HTML(animation.to_jshtml())
