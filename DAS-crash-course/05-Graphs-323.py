# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/

from typing import List
from utils import run_test_cases
from collections import defaultdict

test_cases = [
    (dict(n=5, edges=[[0, 1], [1, 2], [3, 4]]), 2),
    (dict(n=5, edges=[[0, 1], [1, 2], [2, 3], [3, 4]]), 1),
    (dict(n=4, edges=[[2, 3], [1, 2], [1, 3]]), 2),
]


class Solution:
    # Time: O(E + V)
    # Space: O(E + V)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 1<= N <= 2000 nodes
        # 1 <= edges.length <= 5000
        # edges[i] = [ai, bi], undirected edge a <-> b
        # no self-edges, no duplicated edges
        # How many connected components?
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node):
            for other in graph[node]:
                if other in nodes_to_visit:
                    nodes_to_visit.remove(other)
                    dfs(other)

        num_components = 0
        nodes_to_visit = set(range(n))
        while nodes_to_visit:
            node = nodes_to_visit.pop()
            dfs(node)
            num_components += 1

        return num_components


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
