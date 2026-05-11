class GridEnvironment:

    def __init__(self, grid_size=5):

        self.grid_size = grid_size

        self.start = (0, 0)

        self.goal = (
            grid_size - 1,
            grid_size - 1
        )

        self.actions = [
            "UP",
            "DOWN",
            "LEFT",
            "RIGHT"
        ]

        self.obstacles = (
            self.generate_obstacles()
        )

    def generate_obstacles(self):

        if self.grid_size == 4:

            return [
                (1, 1),
                (2, 1)
            ]

        elif self.grid_size == 5:

            return [
                (1, 1),
                (1, 3),
                (2, 2),
                (3, 1),
                (3, 3)
            ]

        else:

            return [
                (1, 1),
                (1, 4),
                (2, 2),
                (3, 1),
                (3, 4),
                (4, 2)
            ]

    def get_next_state(
        self,
        state,
        action
    ):

        row, col = state

        if action == "UP":
            row -= 1

        elif action == "DOWN":
            row += 1

        elif action == "LEFT":
            col -= 1

        elif action == "RIGHT":
            col += 1

        # boundary check
        row = max(
            0,
            min(
                row,
                self.grid_size - 1
            )
        )

        col = max(
            0,
            min(
                col,
                self.grid_size - 1
            )
        )

        next_state = (
            row,
            col
        )

        # obstacle hit
        if next_state in self.obstacles:

            return (
                state,
                -10,
                False
            )

        # goal reached
        if next_state == self.goal:

            return (
                next_state,
                100,
                True
            )

        return (
            next_state,
            -1,
            False
        )