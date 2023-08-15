# https://leetcode.com/problems/reachable-nodes-with-restrictions/editorial/

from collections import defaultdict
from typing import List

from utils import run_test_cases


test_cases = [
    (dict(n=7, edges=[[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], restricted=[4, 5]), 4),
    (dict(n=7, edges=[[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]], restricted=[4, 2, 1]), 3),
]


class Solution:
    # Time: O(N + E)
    # Space: O(N + E)
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # Undirected *TREE* with N nodes, labels from 0 ... N - 1
        # N - 1 edges
        # edges is 2D, length N - 1
        # edges[i] = [ai, bi]
        # How many nodes can you reach from node 0 without stepping in a restricted node?
        # 0 will never be restricted.
        # 2 <= n <= 10^5
        restricted = set(restricted)
        graph = defaultdict(list)
        for x, y in edges:
            if x in restricted or y in restricted:
                continue
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node):
            nonlocal visited
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        visited = {0}
        dfs(0)
        return len(visited)


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
