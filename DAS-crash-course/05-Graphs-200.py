# https://leetcode.com/problems/number-of-islands/


from utils import run_test_cases
from typing import List


test_cases = [
    (
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ],
        1
    ), (
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ],
        3
    )
]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        num_islands = 0
        visited = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def walk_in_every_direction(x, y):
            if is_visited(x, y) or not is_valid(x, y) or not is_land(x, y):
                return

            # print(f"Visit: {x}, {y}")
            visited.add((x, y))
            for dx, dy in directions:
                walk_in_every_direction(x + dx, y + dy)

        def is_visited(x, y):
            return (x, y) in visited

        def is_land(x, y):
            return grid[y][x] == "1"

        def is_valid(x, y):
            return (0 <= x < n) and (0 <= y < m)

        for y in range(m):
            for x in range(n):
                # print(f"Starting from {x}, {y}")
                if is_land(x, y) and not is_visited(x, y):
                    num_islands += 1
                    walk_in_every_direction(x, y)
                # print("---")

        return num_islands


if __name__ == '__main__':
    run_test_cases(Solution, test_cases)
