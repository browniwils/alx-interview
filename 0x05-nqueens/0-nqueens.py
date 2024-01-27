#!/usr/bin/python3
"""Script for running N queens program: solution finder."""

import sys


class NQueens:
    """Class for N Queens objects."""

    possible_solutions = []
    number_of_chessboard = 0
    position = None

    def __init__(self):
        """Instanciate N Queen object."""

        self.possible_solutions = []
        self.number_of_chessboard = 0
        self.position = None

    def req_input(self):
        """Receives program's inputs as argument.

        Returns:
            int: size of the chessboard.
        """

        self.number_of_chessboard = 0
        if len(sys.argv) != 2:
            print("Usage: nqueens N")
            sys.exit(1)
        try:
            self.number_of_chessboard = int(sys.argv[1])
        except Exception:
            print("N must be a number")
            sys.exit(1)
        if self.number_of_chessboard < 4:
            print("N must be at least 4")
            sys.exit(1)
        return self.number_of_chessboard

    def _attacking(self, first_position, second_position):
        """Checks if two queens are in attacking mode.

        Args:
            first_position (list or tuple): first queen's position.
            second_position (list or tuple): second queen's position.

        Returns:
            bool: true if the queens are in an attacking position else false.
        """
        condition_1 = first_position[0] == second_position[0]
        condition_2 = first_position[1] == second_position[1]
        if condition_1 or condition_2:
            return True
        con_1 = abs(first_position[0] - second_position[0])
        con_2 = abs(first_position[1] - second_position[1])
        return con_1 == con_2

    def group_exists(self, lists):
        """Checks if there is a group the list of solution.

        Args:
            lists (list of integers): group of possible positions.

        Returns:
            bool: True if it exists, otherwise False.
        """

        for solution in self.possible_solutions:
            i = 0
            for solution_pos in solution:
                for _list in lists:
                    l_1 = solution_pos[1]
                    l_2 = _list[1]
                    if (solution_pos[0] == _list[0] and l_1 == l_2):
                        i += 1
            if i == self.number_of_chessboard:
                return True
        return False

    def create_solution(self, row, group):
        """Creates solution for n queens problem.

        Args:
            row (int): current row in the chessboard.
            group (list of lists of integers): group of valid positions.
        """

        if row == self.number_of_chessboard:
            _temp = group.copy()
            if not self.group_exists(_temp):
                self.possible_solutions.append(_temp)
        else:
            for column in range(self.number_of_chessboard):
                actual = (row * self.number_of_chessboard) + column
                matches = zip(
                    list([self.position[actual]]) * len(group), group)
                used_positions = map(
                    lambda x: self._attacking(x[0], x[1]), matches)
                group.append(self.position[actual].copy())
                if not any(used_positions):
                    self.create_solution(row + 1, group)
                group.pop(len(group) - 1)

    def get_solutions(self):
        """Retrieves solution for the given chessboard size."""
        cb = self.number_of_chessboard
        self.position = list(map(lambda x: [x // cb, x % cb], range(cb ** 2)))
        self.create_solution(0, [])

    def display_solutions(self) -> None:
        """Print solution to standard output."""
        for solution in self.possible_solutions:
            print(solution)


if __name__ == "__main__":
    queen = NQueens()
    queen.req_input()
    queen.get_solutions()
    queen.display_solutions()
