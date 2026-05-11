import customtkinter as ctk


class GameBoard:

    def __init__(
        self,
        parent,
        grid_size,
        obstacles
    ):

        self.parent = parent
        self.grid_size = grid_size
        self.obstacles = obstacles

        self.robot_position = [
            0,
            0
        ]

        self.goal_position = (
            grid_size - 1,
            grid_size - 1
        )

        self.path = [
            (0, 0)
        ]

        self.create_board()

    def create_board(
        self
    ):

        self.board_frame = (
            ctk.CTkFrame(
                self.parent,
                fg_color="transparent"
            )
        )

        self.board_frame.pack(
            pady=20
        )

        self.cells = []

        cell_size = (
            500
            //
            self.grid_size
        )

        for row in range(
            self.grid_size
        ):

            row_cells = []

            for col in range(
                self.grid_size
            ):

                cell = (
                    ctk.CTkFrame(
                        self.board_frame,
                        width=cell_size,
                        height=cell_size,
                        corner_radius=18,
                        fg_color="#1E293B"
                    )
                )

                cell.grid(
                    row=row,
                    column=col,
                    padx=6,
                    pady=6
                )

                label = (
                    ctk.CTkLabel(
                        cell,
                        text="",
                        font=ctk.CTkFont(
                            size=28,
                            weight="bold"
                        )
                    )
                )

                label.place(
                    relx=0.5,
                    rely=0.5,
                    anchor="center"
                )

                row_cells.append(
                    (
                        cell,
                        label
                    )
                )

            self.cells.append(
                row_cells
            )

        self.update_board()

    def update_board(
        self
    ):

        for row in range(
            self.grid_size
        ):
            for col in range(
                self.grid_size
            ):

                cell, label = (
                    self.cells[row][col]
                )

                color = "#1E293B"
                text = ""

                # Start
                if (
                    row,
                    col
                ) == (
                    0,
                    0
                ):

                    color = "#22C55E"
                    text = "S"

                # Goal
                elif (
                    row,
                    col
                ) == (
                    self.goal_position
                ):

                    color = "#FACC15"
                    text = "G"

                # Obstacles
                elif (
                    row,
                    col
                ) in (
                    self.obstacles
                ):

                    color = "#EF4444"
                    text = "X"

                # Path
                elif (
                    row,
                    col
                ) in (
                    self.path
                ):

                    color = "#38BDF8"

                # Robot
                if [
                    row,
                    col
                ] == (
                    self.robot_position
                ):

                    color = "#6366F1"
                    text = "🤖"

                cell.configure(
                    fg_color=color
                )

                label.configure(
                    text=text
                )

    def move_robot(
        self,
        direction
    ):

        row, col = (
            self.robot_position
        )

        new_row = row
        new_col = col

        if (
            direction
            ==
            "UP"
        ):
            new_row -= 1

        elif (
            direction
            ==
            "DOWN"
        ):
            new_row += 1

        elif (
            direction
            ==
            "LEFT"
        ):
            new_col -= 1

        elif (
            direction
            ==
            "RIGHT"
        ):
            new_col += 1

        # boundary check
        if not (
            0
            <=
            new_row
            <
            self.grid_size
            and
            0
            <=
            new_col
            <
            self.grid_size
        ):

            return (
                "Invalid Move ❌",
                -5
            )

        # obstacle
        if (
            new_row,
            new_col
        ) in (
            self.obstacles
        ):

            return (
                "Obstacle Hit 🚫",
                -10
            )

        self.robot_position = [
            new_row,
            new_col
        ]

        self.path.append(
            (
                new_row,
                new_col
            )
        )

        self.update_board()

        if (
            new_row,
            new_col
        ) == (
            self.goal_position
        ):

            return (
                "Goal Reached 🎯",
                100
            )

        return (
            "Moving 🤖",
            5
        )

    def move_to_position(
        self,
        row,
        col
    ):

        self.robot_position = [
            row,
            col
        ]

        if (
            row,
            col
        ) not in (
            self.path
        ):

            self.path.append(
                (
                    row,
                    col
                )
            )

        self.update_board()

        if (
            row,
            col
        ) == (
            self.goal_position
        ):

            return (
                "Goal Reached 🎯",
                100
            )

        return (
            "AI Moving 🤖",
            5
        )