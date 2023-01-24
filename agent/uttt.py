from typing import List, Tuple

import numpy as np

###############################################################
#   You most likely will not need to edit this file at all,   #
#   but you should include it as part of your submission.     #
###############################################################


class BaseAgent:
    def __init__(self) -> None:
        self.player = None
        self.opponent = None

    def set_player(self, player: str) -> None:
        """Sets the current player and opponent.

        Args:
            player (str): Either R for red or B for blue.
        """

        self.player = player
        self.opponent = "B" if player == "R" else "R"

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

        raise NotImplementedError()


class RemoteUTTTGame:
    def __init__(self, agent: BaseAgent) -> None:
        self.agent = agent
        self.player = None

        self.boards = np.zeros((9, 9), dtype="<U1")
        self.board_winners = np.zeros((9,), dtype="<U1")

    def _determine_player(self) -> str:
        """Determines whether the current player is R or B."

        Raises:
            ValueError: An invalid player was received.
        Returns:
            str: The current player
        """

        message = input()
        if message in ("INIT R", "INIT B"):
            print("OK")
            return message[-1]

        raise ValueError(
            f"The first message should be either `INIT R` or `INIT B`, but `{message}` was received."
        )

    def _request_move(self, playable_boards: List[int]) -> Tuple[int, int]:
        """Requests a move from the player's agent.

        Args:
            playable_boards (List[int]): A list of local boards in which the player's agent can play

        Returns:
            Tuple[int, int]: The local board and tile to mark
        """

        move = self.agent.make_move(
            boards=self.boards.copy(),
            board_winners=self.board_winners.copy(),
            playable_boards=playable_boards,
        )

        if self.boards[move]:
            raise ValueError(
                f"The agent tried to make an illegal move: the tile {move} is already occupied by {self.boards[move]}."
            )

        if self.board_winners[move[0]]:
            raise ValueError(
                f"The agent tried to make an illegal move: the tile {move} is in a board already won by {self.board_winners[move[0]]}."
            )

        return move

    def _place_tile(self, player: str, board: int, tile: int) -> None:
        """Marks a tile in the specified local board for the player specified.

        Args:
            player (str): The player placing the tile (R for red or B for blue)
            board (int): The local board position in the global board
            tile (int): The tile position
        """

        self.boards[board, tile] = player

    def _set_board_winner(self, player: str, board: int) -> None:
        """Marks a local board in the global boad as won for the player specified.

        Args:
            player (str): The winning player (R for red, B for blue or S for stalemate)
            board (int): The local board won
        """

        self.board_winners[board] = player

    def play(self):
        """Runs the main game loop."""

        self.player = self._determine_player()
        self.agent.set_player(self.player)

        while True:
            # Get the next line of input and then split it at each space
            parts = input().split(" ")

            # Agent action request
            if parts[0] == "A":
                playable_boards = [int(board) for board in parts[1].split(",")]

                move = self._request_move(playable_boards)
                self._place_tile(player=self.player, board=move[0], tile=move[1])

                print(f"M {move[0]} {move[1]}")

            # Tile placement update
            elif parts[0] == "P":
                self._place_tile(
                    player=parts[1], board=int(parts[2]), tile=int(parts[3])
                )

            # Local board win
            elif parts[0] == "W":
                self._set_board_winner(player=parts[1], board=int(parts[2]))

            # Unknown command
            else:
                break
