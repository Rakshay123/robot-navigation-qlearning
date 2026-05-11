import random
import numpy as np


class QLearningAgent:

    def __init__(
        self,
        environment
    ):

        self.env = environment

        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.epsilon = 1.0
        self.epsilon_decay = 0.995
        self.min_epsilon = 0.01

        self.q_table = np.zeros(
            (
                self.env.grid_size,
                self.env.grid_size,
                len(
                    self.env.actions
                )
            )
        )

    def choose_action(
        self,
        state
    ):

        row, col = state

        if (
            random.uniform(
                0,
                1
            )
            < self.epsilon
        ):

            return random.randint(
                0,
                3
            )

        return np.argmax(
            self.q_table[
                row,
                col
            ]
        )

    def train(
        self,
        episodes=500
    ):

        rewards_history = []

        for _ in range(
            episodes
        ):

            state = (
                self.env.start
            )

            done = False
            total_reward = 0

            while not done:

                action_index = (
                    self.choose_action(
                        state
                    )
                )

                action = (
                    self.env.actions[
                        action_index
                    ]
                )

                (
                    next_state,
                    reward,
                    done
                ) = (
                    self.env.get_next_state(
                        state,
                        action
                    )
                )

                row, col = state

                next_row, next_col = (
                    next_state
                )

                old_q = (
                    self.q_table[
                        row,
                        col,
                        action_index
                    ]
                )

                next_max = np.max(
                    self.q_table[
                        next_row,
                        next_col
                    ]
                )

                new_q = (
                    old_q
                    +
                    self.learning_rate
                    * (
                        reward
                        +
                        self.discount_factor
                        * next_max
                        -
                        old_q
                    )
                )

                self.q_table[
                    row,
                    col,
                    action_index
                ] = new_q

                state = (
                    next_state
                )

                total_reward += (
                    reward
                )

            # epsilon decay
            self.epsilon = max(
                self.min_epsilon,
                self.epsilon
                *
                self.epsilon_decay
            )

            rewards_history.append(
                total_reward
            )

        return rewards_history

    def get_optimal_path(
        self
    ):

        path = []

        state = (
            self.env.start
        )

        visited = set()

        while (
            state
            != self.env.goal
        ):

            if state in visited:
                break

            visited.add(
                state
            )

            path.append(
                state
            )

            row, col = state

            action_index = (
                np.argmax(
                    self.q_table[
                        row,
                        col
                    ]
                )
            )

            action = (
                self.env.actions[
                    action_index
                ]
            )

            (
                next_state,
                _,
                _
            ) = (
                self.env.get_next_state(
                    state,
                    action
                )
            )

            state = (
                next_state
            )

        path.append(
            self.env.goal
        )

        return path