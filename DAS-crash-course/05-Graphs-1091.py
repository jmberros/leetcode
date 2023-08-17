# https://leetcode.com/problems/shortest-path-in-binary-matrix/

from collections import deque
from typing import List

from utils import run_test_cases


test_cases = [
    (
        [[0, 1],
         [1, 0]],
        2
    ), (
        [[0, 0, 0],
         [1, 1, 0],
         [1, 1, 0]],
        4
    ), (
        [[1, 0, 0],
         [1, 1, 0],
         [1, 1, 0]],
        -1
    )
]


class Solution:
    # Time: O(N^2)
    # Space: O(N^2)
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # TODO: Docstring
        # N x N binary matrix, 1 <= N <= 100
        # Return the length of the shortest CLEAR PATH in the matrix, or -1.
        # a clear path traverses only 0s, from (0, 0), to (N-1, N-1)
        # you can move diagonally
        n = len(grid)
        destination_tile = (n - 1, n - 1)  # Bottom right tile of an NxN grid

        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < n

        def is_walkable(x, y):
            return grid[y][x] == 0

        def was_visited(x, y):
            return (x, y) in visited

        def mark_as_visited(x, y):
            nonlocal visited
            visited.add(next_tile)

        def get_adjacent_tiles(x, y):
            directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1),
                          (0, 1),  (1, 1)]
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if is_valid(new_x, new_y):
                    yield new_x, new_y

        start_tile = (0, 0)
        if not is_walkable(*start_tile) or not is_walkable(*destination_tile):
            return -1

        tiles_to_visit = deque([(start_tile, 1)])  # ((X, Y), path length)
        visited = {start_tile}
        successful_path_length = -1
        while tiles_to_visit:
            tile, path_length = tiles_to_visit.popleft()
            # print(f"Jumping into {tile} ({grid[tile[1]][tile[0]]}) | {path_length = } | {visited = }")
            if tile == destination_tile:
                successful_path_length = path_length
                break
            for next_tile in get_adjacent_tiles(*tile):
                if is_walkable(*next_tile) and not was_visited(*next_tile):
                    tiles_to_visit.append((next_tile, path_length + 1))
                    mark_as_visited(*next_tile)

        return successful_path_length


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
