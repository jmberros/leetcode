# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

from collections import deque
from collections import defaultdict
from utils import run_test_cases
from typing import List


test_cases = [
    (dict(n=6, connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]), 3),
    (dict(n=5, connections=[[1, 0], [1, 2], [3, 2], [3, 4]]), 2),
    (dict(n=3, connections=[[1, 0], [2, 0]]), 0)
]


class Solution:
    # Time: O(N)
    # Space: O(N)
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # N cities (0, 1, ..., N - 1)
        # N - 1 roads
        # Only one way to travel between two cities
        # The network is a tree
        # connections[i] = [ai, bi] is a road from ai to bi, aᵢ != bᵢ ∀i
        # Reorient some roads such that each city can visit city 0
        # Return the min number of edges changed
        # 2 <= n <= 5 * 10^4

        # Preprocessing
        out_connections = defaultdict(list)
        in_connections = defaultdict(list)
        for a, b in connections:
            out_connections[a].append(b)
            in_connections[b].append(a)

        # The idea is to irradiate from 0 to any connected cities, iteratively.
        # Whenever a road leads "outwards" (i.e. it goes _away_ from 0), then
        # the road needs to be reversed. "Inwards" roads (i.e. they already
        # point to 0) don't need any reversal, but we still have to follow them
        # to find new cities.
        num_changes = 0
        queue = deque([0])
        visited = set()
        while queue:
            city = queue.pop()
            visited.add(city)
            for other in out_connections[city]:
                if other not in visited:
                    # print(f"Road needs reversal: {city} -> {other}")
                    num_changes += 1
                    queue.append(other)
            for other in in_connections[city]:
                if other not in visited:
                    queue.append(other)

        return num_changes

    def minReorder_DFS(self, n: int, connections: List[List[int]]) -> int:
        roads = set()
        graph = defaultdict(list)
        for x, y in connections:
            roads.add((x, y))
            graph[x].append(y)
            graph[y].append(x)

        visited = set()

        def helper(node):
            num_changes = 0
            visited.add(node)

            for other in graph[node]:
                if other not in visited:
                    if (node, other) in roads:  # Needs reversal
                        # print(f"Reverse {node}->{other}")
                        num_changes += 1
                    num_changes += helper(other)

            return num_changes

        return helper(0)


if __name__ == '__main__':
    run_test_cases(Solution, test_cases)
