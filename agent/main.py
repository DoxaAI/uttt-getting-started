import random
from typing import List, Tuple

import numpy as np
from uttt import BaseAgent, RemoteUTTTGame

#################################################################
#   Modify the Agent class below to implement your own agent.   #
#   You may define additional methods as you see fit.           #
#################################################################


class Agent(BaseAgent):
    """An agent for the ultimate tic-tac-toe competition on DOXA."""

    def make_move(
        self, boards: np.ndarray, board_winners: np.ndarray, playable_boards: List[int]
    ) -> Tuple[int, int]:
        """Makes a move.

        Args:
            boards (np.ndarray): An array with shape (9, 9) containing all the
                                 local boards. Elements are either "R" (red),
                                 "B" (blue), "S" (stalemate) or "" (empty).
            board_winners (np.ndarray): A 9-element array with the certified
                                        winners of each local board.
            playable_boards (List[int]): A list of local boards in which a move
                                         may be played this round.

        Returns:
            Tuple[int, int]: The local board and tile to play in.
        """

        # Find all the free tiles across all playable boards
        possible_moves = [
            (board, tile)
            for board in playable_boards
            for tile in range(0, 9)
            if not boards[board, tile]
        ]

        # Pick a valid move uniformly at random
        return random.choice(possible_moves)


def main():
    # Instantiate the agent
    agent = Agent()

    # Start playing the game on DOXA
    RemoteUTTTGame(agent).play()


if __name__ == "__main__":
    main()
