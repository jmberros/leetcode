# https://leetcode.com/problems/01-matrix/

from typing import List
from utils import run_test_cases
from collections import deque

test_cases = [
    (
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
    ),
    (
        [[0, 0, 0], [0, 1, 0], [1, 1, 1]],
        [[0, 0, 0], [0, 1, 0], [1, 2, 1]],
    ),
    (
        [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1],
         [1, 1, 1],
         [1, 1, 1],
         [1, 1, 1],
         [1, 1, 1],
         [1, 1, 1],
         [1, 1, 1],
         [1, 1, 1],
         [1, 1, 1],
         [1, 1, 1],
         [1, 1, 1],
         [1, 1, 1],
         [1, 1, 1],
         [1, 1, 1],
         [1, 1, 1],
         [1, 1, 1],
         [1, 1, 1],
         [0, 0, 0]],
        []
    ),
]


class Solution:
    # Time
    # Space
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # MxN binary matrix (M rows, N cols)
        # There is at least one 0 in the matrix
        # Return the distance of the nearest 0 for each cell
        m = len(mat)
        n = len(mat[0])

        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < m

        cells_to_visit = deque()
        for y in range(m):
            for x in range(n):
                if mat[y][x] == 0:
                    cells_to_visit.append((x, y))
        visited = set(cells_to_visit)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def get_adjacent_cells(x, y):
            for dx, dy in directions:
                x2, y2 = x + dx, y + dy
                if is_valid(x2, y2):
                    yield x2, y2

        solution = [row[:] for row in mat]
        current_layer_dist = 0
        while cells_to_visit:
            # Visit all the cells of the current layer
            for _ in range(len(cells_to_visit)):
                x, y = cells_to_visit.popleft()
                solution[y][x] = current_layer_dist
                print(f"{x}, {y} -> {current_layer_dist}")
                for x2, y2 in get_adjacent_cells(x, y):
                    if (x2, y2) not in visited:
                        cells_to_visit.append((x2, y2))
                        visited.add((x2, y2))
            # Advance to the next layer irradiating outwards from each zero-cell
            current_layer_dist += 1

        return solution


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
