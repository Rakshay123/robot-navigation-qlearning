import customtkinter as ctk
from tkinter import messagebox

from environment import GridEnvironment
from qlearning import QLearningAgent
from game_board import GameBoard


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class RobotNavigationApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title(
            "Robot Navigation System"
        )

        self.geometry(
            "1450x850"
        )

        self.configure(
            fg_color="#0F172A"
        )

        self.grid_size = 5
        self.total_reward = 0
        self.steps = 0
        self.game_finished = False
        self.auto_running = False

        self.create_home_page()

    # ---------------- HOME PAGE ----------------
    def create_home_page(self):

        self.clear_window()

        container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        container.pack(
            expand=True
        )

        title = ctk.CTkLabel(
            container,
            text=(
                "🤖 Intelligent Robot\n"
                "Navigation System"
            ),
            font=ctk.CTkFont(
                size=42,
                weight="bold"
            )
        )

        title.pack(
            pady=30
        )

        subtitle = ctk.CTkLabel(
            container,
            text=(
                "Q-Learning Based Smart "
                "Robot Navigation"
            ),
            font=ctk.CTkFont(
                size=20
            ),
            text_color="gray"
        )

        subtitle.pack()

        start_btn = ctk.CTkButton(
            container,
            text="Start Project",
            width=250,
            height=55,
            corner_radius=18,
            font=ctk.CTkFont(
                size=20,
                weight="bold"
            ),
            command=self.create_grid_page
        )

        start_btn.pack(
            pady=40
        )

    # ---------------- GRID PAGE ----------------
    def create_grid_page(self):

        self.clear_window()

        frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame.pack(
            expand=True
        )

        title = ctk.CTkLabel(
            frame,
            text="Select Grid Size",
            font=ctk.CTkFont(
                size=34,
                weight="bold"
            )
        )

        title.pack(
            pady=30
        )

        self.grid_dropdown = (
            ctk.CTkOptionMenu(
                frame,
                values=[
                    "4 x 4",
                    "5 x 5",
                    "6 x 6"
                ],
                width=250,
                height=50,
                command=self.select_grid
            )
        )

        self.grid_dropdown.set(
            "5 x 5"
        )

        self.grid_dropdown.pack(
            pady=20
        )

        start_navigation = (
            ctk.CTkButton(
                frame,
                text="Continue",
                width=250,
                height=55,
                corner_radius=18,
                command=self.create_navigation_page
            )
        )

        start_navigation.pack(
            pady=30
        )

    def select_grid(
        self,
        choice
    ):

        self.grid_size = int(
            choice[0]
        )

    # ---------------- DASHBOARD ----------------
    def create_navigation_page(
        self
    ):

        self.clear_window()

        self.total_reward = 0
        self.steps = 0
        self.game_finished = False
        self.auto_running = False

        self.environment = (
            GridEnvironment(
                self.grid_size
            )
        )

        main_frame = (
            ctk.CTkFrame(
                self,
                fg_color="transparent"
            )
        )

        main_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # LEFT PANEL
        left_panel = (
            ctk.CTkFrame(
                main_frame,
                width=320,
                corner_radius=25
            )
        )

        left_panel.pack(
            side="left",
            fill="y",
            padx=15
        )

        title = ctk.CTkLabel(
            left_panel,
            text="🎮 Control Panel",
            font=ctk.CTkFont(
                size=26,
                weight="bold"
            )
        )

        title.pack(
            pady=20
        )

        self.reward_card = (
            ctk.CTkLabel(
                left_panel,
                text="Reward: 0",
                width=240,
                height=70,
                corner_radius=20,
                fg_color="#1E293B",
                font=ctk.CTkFont(
                    size=22,
                    weight="bold"
                )
            )
        )

        self.reward_card.pack(
            pady=10
        )

        self.step_card = (
            ctk.CTkLabel(
                left_panel,
                text="Steps: 0",
                width=240,
                height=70,
                corner_radius=20,
                fg_color="#1E293B",
                font=ctk.CTkFont(
                    size=22,
                    weight="bold"
                )
            )
        )

        self.step_card.pack(
            pady=10
        )

        self.status_card = (
            ctk.CTkLabel(
                left_panel,
                text="Status: Ready",
                width=240,
                height=80,
                corner_radius=20,
                fg_color="#1E293B",
                font=ctk.CTkFont(
                    size=20
                )
            )
        )

        self.status_card.pack(
            pady=10
        )

        manual_label = (
            ctk.CTkLabel(
                left_panel,
                text=(
                    "⌨️ Manual Controls\n"
                    "↑ ↓ ← → Keys"
                ),
                font=ctk.CTkFont(
                    size=18
                )
            )
        )

        manual_label.pack(
            pady=10
        )

        auto_btn = (
            ctk.CTkButton(
                left_panel,
                text="🤖 Auto Navigate",
                width=240,
                height=50,
                fg_color="#16A34A",
                command=self.start_auto_navigation
            )
        )

        auto_btn.pack(
            pady=10
        ) 
        restart_btn = (
            ctk.CTkButton(
                left_panel,
                text="🔄 Restart",
                width=240,
                height=50,
                fg_color="#2563EB",
                command=self.create_navigation_page
            )
        )

        restart_btn.pack(
            pady=10
        )

        # Traversal Path Card
        path_title = (
            ctk.CTkLabel(
                left_panel,
                text="📍 Traversal Path",
                font=ctk.CTkFont(
                    size=20,
                    weight="bold"
                )
            )
        )

        path_title.pack(
            pady=(20, 5)
        )

        self.path_box = (
            ctk.CTkTextbox(
                left_panel,
                width=260,
                height=220
            )
        )

        self.path_box.pack(
            pady=10
        )

        self.path_box.insert(
            "0.0",
            "(0,0)"
        )

        # CENTER BOARD
        center_frame = (
            ctk.CTkFrame(
                main_frame,
                fg_color="transparent"
            )
        )

        center_frame.pack(
            side="left",
            expand=True
        )

        self.game = (
            GameBoard(
                center_frame,
                self.grid_size,
                self.environment.obstacles
            )
        )

        # RIGHT PANEL
        right_panel = (
            ctk.CTkFrame(
                main_frame,
                width=300,
                corner_radius=25
            )
        )

        right_panel.pack(
            side="right",
            fill="y",
            padx=15
        )

        analytics_title = (
            ctk.CTkLabel(
                right_panel,
                text="📊 Analytics",
                font=ctk.CTkFont(
                    size=24,
                    weight="bold"
                )
            )
        )

        analytics_title.pack(
            pady=20
        )

        self.mode_card = (
            ctk.CTkLabel(
                right_panel,
                text="Mode:\nManual",
                width=220,
                height=90,
                fg_color="#1E293B",
                corner_radius=20,
                font=ctk.CTkFont(
                    size=20
                )
            )
        )

        self.mode_card.pack(
            pady=10
        )

        self.animation_card = (
            ctk.CTkLabel(
                right_panel,
                text="🤖 Animation\nReady",
                width=220,
                height=120,
                fg_color="#1E293B",
                corner_radius=20,
                font=ctk.CTkFont(
                    size=20
                )
            )
        )

        self.animation_card.pack(
            pady=10
        )

        # Keyboard controls
        self.bind(
            "<Up>",
            lambda e:
            self.move_robot(
                "UP"
            )
        )

        self.bind(
            "<Down>",
            lambda e:
            self.move_robot(
                "DOWN"
            )
        )

        self.bind(
            "<Left>",
            lambda e:
            self.move_robot(
                "LEFT"
            )
        )

        self.bind(
            "<Right>",
            lambda e:
            self.move_robot(
                "RIGHT"
            )
        )

        self.focus_set()

    # ---------------- MANUAL MOVE ----------------
    def move_robot(
        self,
        direction
    ):

        if (
            self.game_finished
            or
            self.auto_running
        ):
            return

        status, reward = (
            self.game.move_robot(
                direction
            )
        )

        self.update_ui(
            status,
            reward
        )

    # ---------------- AUTO NAVIGATION ----------------
    def start_auto_navigation(
        self
    ):

        self.auto_running = True

        self.mode_card.configure(
            text="Mode:\nAuto AI"
        )

        self.status_card.configure(
            text="Status:\nTraining..."
        )

        self.animation_card.configure(
            text="🤖 Learning..."
        )

        env = GridEnvironment(
            self.grid_size
        )

        agent = QLearningAgent(
            env
        )

        agent.train(
            episodes=500
        )

        self.path = (
            agent.get_optimal_path()
        )

        self.current_step = 0

        self.after(
            1000,
            self.auto_move_step
        )

    def auto_move_step(
        self
    ):

        if (
            self.current_step
            >=
            len(
                self.path
            )
        ):
            return

        row, col = (
            self.path[
                self.current_step
            ]
        )

        status, reward = (
            self.game.move_to_position(
                row,
                col
            )
        )

        self.update_ui(
            status,
            reward
        )

        self.current_step += 1

        if (
            "Goal"
            not in status
        ):

            self.after(
                700,
                self.auto_move_step
            )

    # ---------------- UPDATE UI ----------------
    def update_ui(
        self,
        status,
        reward
    ):

        self.total_reward += reward
        self.steps += 1

        self.reward_card.configure(
            text=f"Reward: {self.total_reward}"
        )

        self.step_card.configure(
            text=f"Steps: {self.steps}"
        )

        self.status_card.configure(
            text=f"Status:\n{status}"
        )

        self.animation_card.configure(
            text=f"🤖 {status}"
        )

        # Path update
        self.path_box.delete(
            "0.0",
            "end"
        )

        path_text = ""

        for step in (
            self.game.path
        ):

            path_text += (
                f"{step}\n"
            )

        self.path_box.insert(
            "0.0",
            path_text
        )

        # Goal popup
        if (
            "Goal"
            in status
        ):

            self.game_finished = True

            messagebox.showinfo(
                "Mission Complete",
                (
                    "🎉 Goal Reached!\n\n"
                    "Robot Successfully "
                    "Reached Destination."
                )
            )

    # ---------------- CLEAR WINDOW ----------------
    def clear_window(
        self
    ):

        for widget in (
            self.winfo_children()
        ):
            widget.destroy()


app = RobotNavigationApp()
app.mainloop()