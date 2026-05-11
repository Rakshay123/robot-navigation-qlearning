import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap


def visualize_training(env, training_steps):

    colors = [
        "#F8F9FA",  # Empty
        "#FFB4A2",  # Obstacle
        "#A8DADC",  # Path
        "#CDEAC0",  # Start
        "#FFE699",  # Goal
        "#5E60CE"   # Robot
    ]

    cmap = ListedColormap(colors)

    fig, ax = plt.subplots(figsize=(8, 8))

    for step, reward, status in training_steps[:60]:

        grid = np.zeros(
            (env.grid_size, env.grid_size)
        )

        # Obstacles
        for obstacle in env.obstacles:
            grid[obstacle] = 1

        # Start
        grid[env.start] = 3

        # Goal
        grid[env.goal] = 4

        # Robot position
        grid[step] = 5

        ax.clear()

        ax.imshow(grid, cmap=cmap)

        ax.set_xticks(
            range(env.grid_size)
        )

        ax.set_yticks(
            range(env.grid_size)
        )

        ax.grid(
            color="white",
            linewidth=2
        )

        # Labels
        for row in range(env.grid_size):
            for col in range(env.grid_size):

                if (row, col) == env.start:
                    ax.text(
                        col, row, "S",
                        ha="center",
                        va="center",
                        fontsize=16,
                        fontweight="bold"
                    )

                elif (row, col) == env.goal:
                    ax.text(
                        col, row, "G",
                        ha="center",
                        va="center",
                        fontsize=16,
                        fontweight="bold"
                    )

                elif (
                    row,
                    col
                ) in env.obstacles:

                    ax.text(
                        col, row, "X",
                        ha="center",
                        va="center",
                        fontsize=16,
                        fontweight="bold"
                    )

        # Live AI learning info
        ax.set_title(
            f"AI Learning Phase\n"
            f"Robot Position: {step}\n"
            f"{status} | Reward: {reward}",
            fontsize=14,
            fontweight="bold"
        )

        # Dramatic pauses
        if status == "Obstacle Hit":
            plt.pause(2)

        elif status == "Goal Reached":
            plt.pause(2)

        else:
            plt.pause(0.8)

    plt.close()


def visualize_final_path(env, path):

    colors = [
        "#F8F9FA",
        "#FFB4A2",
        "#A8DADC",
        "#CDEAC0",
        "#FFE699",
        "#5E60CE"
    ]

    cmap = ListedColormap(colors)

    fig, ax = plt.subplots(figsize=(8, 8))

    for step in path:

        grid = np.zeros(
            (env.grid_size, env.grid_size)
        )

        # Obstacles
        for obstacle in env.obstacles:
            grid[obstacle] = 1

        # Learned path
        for p in path:
            if (
                p != env.start
                and p != env.goal
            ):
                grid[p] = 2

        # Start and Goal
        grid[env.start] = 3
        grid[env.goal] = 4

        # Robot
        grid[step] = 5

        ax.clear()

        ax.imshow(grid, cmap=cmap)

        ax.set_xticks(
            range(env.grid_size)
        )

        ax.set_yticks(
            range(env.grid_size)
        )

        ax.grid(
            color="white",
            linewidth=2
        )

        # Labels
        for row in range(env.grid_size):
            for col in range(env.grid_size):

                if (row, col) == env.start:
                    ax.text(
                        col, row, "S",
                        ha="center",
                        va="center",
                        fontsize=16,
                        fontweight="bold"
                    )

                elif (row, col) == env.goal:
                    ax.text(
                        col, row, "G",
                        ha="center",
                        va="center",
                        fontsize=16,
                        fontweight="bold"
                    )

                elif (
                    row,
                    col
                ) in env.obstacles:

                    ax.text(
                        col, row, "X",
                        ha="center",
                        va="center",
                        fontsize=16,
                        fontweight="bold"
                    )

        ax.set_title(
            "Final Intelligent Navigation\n"
            "Optimal Path Learned Successfully 🎯",
            fontsize=16,
            fontweight="bold"
        )

        # Smooth movement
        if step == env.goal:
            plt.pause(2)
        else:
            plt.pause(0.8)

    plt.show()