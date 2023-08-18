# https://leetcode.com/problems/snakes-and-ladders/description/

from typing import List
from utils import run_test_cases
from collections import defaultdict, deque


test_cases = [
    (
        [[-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 35, -1, -1, 13, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 15, -1, -1, -1, -1]],
        4
    ),
    (
        [[-1, -1], [-1, 3]],
        1
    ),
    (
        [[-1, -1, -1],
         [-1, 9, 8],
         [-1, 8, 9]],
        1
    ),
    (
        [[1, 1, -1],
         [1, 1, 1],
         [-1, 1, 1]],
        -1
    ),
    (
        [[-1, 1, 2, -1],
         [2, 13, 15, -1],
         [-1, 10, -1, -1],
         [-1, 6, 2, 8]],
        2
    ),
    (
        [[-1, -1, -1, 30, -1, 144, 124, 135, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1, 167, 93, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1, -1, 77, -1, -1, 90, -1, -1],
         [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 122, -1],
         [-1, -1, -1, 23, -1, -1, -1, -1, -1, 155, -1, -1, -1],
         [-1, -1, 140, 29, -1, -1, -1, -1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, 115, -1, -1, -1, 109, -1, -1, 5],
         [-1, 57, -1, 99, 121, -1, -1, 132, -1, -1, -1, -1, -1],
         [-1, 48, -1, -1, -1, 68, -1, -1, -1, -1, 31, -1, -1],
         [-1, 163, 147, -1, 77, -1, -1, 114, -1, -1, 80, -1, -1],
         [-1, -1, -1, -1, -1, 57, 28, -1, -1, 129, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1, -1, -1, -1, 87, -1, -1, -1]],
        6
    ),
    (
        [[-1, -1, 128, -1, -1, -1, 136, -1, -1, -1, 109, -1],
         [-1, -1, -1, -1, -1, 103, -1, -1, 56, 10, -1, -1],
         [-1, -1, -1, -1, -1, -1, 116, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1, -1, -1, 50, -1, 67, 107],
         [-1, 40, -1, -1, -1, 20, -1, 59, -1, 67, -1, -1],
         [-1, -1, -1, -1, -1, -1, 112, 133, 111, -1, -1, -1],
         [-1, -1, 112, -1, 74, -1, -1, -1, -1, -1, -1, -1],
         [23, -1, 115, -1, 129, 126, -1, -1, -1, -1, -1, -1],
         [106, 143, 81, -1, -1, -1, -1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1, -1, -1, 26, 102, 1, 29],
         [26, -1, -1, -1, -1, -1, -1, -1, 27, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]],
        "?"
    )
]


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # N x N board, cells labeld from 1 to N^2, Boustrophedon, starting bottom left
        # You start on square 1
        # Each move, choose a destination in the range [curr + 1, min(curr + 6, N^2)]
        # (simulates a 6-sided die roll), 6 destinations at most
        # The game ends if you reach N^2
        # Cell != -1, snake or ladder, and the destination is board[r][c]
        # Don't follow a second snake or ladder
        # Return the min number of moves to reach N^2, or -1 if not possible
        n = len(board)

        def cell_to_row_col_val(cell):
            row, col = divmod(cell - 1, n)  # ! FIXME rethink this
            row = n - 1 - row  # First row is the bottom one
            if (n - 1 - row) % 2 != 0:
                col = n - 1 - col
            return row, col, board[row][col]

        # Build a graph connecting each cell to its possible destinations
        # NOTE: this way of building the graph turned out to be suboptimal
        # Snakes and ladders should be followed immediately and this can be
        # reflected with direct edges, jumping over those cells.
        graph = defaultdict(list)
        for cell in range(1, n**2 + 1):
            r, c, val = cell_to_row_col_val(cell)
            for next_cell in range(cell + 1, min(cell + 6, n**2) + 1):
                graph[cell].append(next_cell)

            # print(f"{r}, {c} | {cell = } ({val}) => {graph[cell]}")

        # BFS starting on square 1
        queue = deque([(1, 0, [1])])  # (Cell number, num steps, path)
        visited_cells = set([1])
        while queue:
            cell, n_steps, path = queue.popleft()
            r, c, val = cell_to_row_col_val(cell)

            if val != -1:
                # Snake or ladder must be followed immediately,
                # but it doesn't add to the number of steps.
                cell = board[r][c]
                path += [f"{cell}*"]

            print(n_steps, path, "=>", graph[cell])
            if cell == n**2:
                return n_steps

            for next_cell in graph[cell]:
                if next_cell in visited_cells:
                    # Prevent circularities. Also, if a different path came to
                    # this cell earlier, then *that* path will be shorter than
                    # this one, so there's no point of following this fork.
                    continue
                queue.append((next_cell, n_steps + 1, path + [next_cell]))
                visited_cells.add(next_cell)

        return -1


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
