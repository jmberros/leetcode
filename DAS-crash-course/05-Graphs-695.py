# https://leetcode.com/problems/max-area-of-island/editorial/

from utils import run_test_cases
from typing import List


test_cases = [
    (
        [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]],
        6
    ),
    (
        [[0, 0, 0, 0, 0, 0, 0, 0]],
        0
    ),
    (
        [[1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 0, 1, 1],
         [0, 0, 0, 1, 1]],
        4
    )
]


class Solution:
    # Time: O(N * M)
    # Space: O(N * M)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # TODO: Docstring
        # M x N binary matrix, 1 <= M, N <= 50
        # An island is a group of 1s connected horiz/vert
        # All edges of the grid are surrounded by water
        # Area of an island = num cells
        # Return the area of the biggest island, or 0 if no islands.
        n_rows = len(grid)
        n_cols = len(grid[0])

        def is_valid(x, y):
            return (0 <= y < n_rows) and (0 <= x < n_cols)

        def is_land(x, y):
            return grid[y][x] == 1

        def walk_in_all_directions(x, y):
            nonlocal size_current_island
            if is_valid(x, y) and is_land(x, y) and not (x, y) in walked:
                size_current_island += 1
                walked.add((x, y))
                walk_in_all_directions(x - 1, y)
                walk_in_all_directions(x + 1, y)
                walk_in_all_directions(x, y - 1)
                walk_in_all_directions(x, y + 1)

        walked = set()
        max_size = 0
        for y, row in enumerate(grid):
            for x, value in enumerate(row):
                if (x, y) in walked:
                    continue

                if is_land(x, y):
                    size_current_island = 0
                    walk_in_all_directions(x, y)
                    max_size = max(size_current_island, max_size)

        return max_size


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
