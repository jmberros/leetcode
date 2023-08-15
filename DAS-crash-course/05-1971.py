# https://leetcode.com/problems/find-if-path-exists-in-graph/description/

from typing import List
from utils import run_test_cases
from collections import defaultdict, deque

test_cases = [
    (dict(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2), True),
    (dict(n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5), False),
    (dict(n=10, edges=[
        [2, 9], [7, 8], [5, 9], [7, 2], [3, 8], [2, 8], [1, 6], [3, 0], [7, 0], [8, 5]
    ], source=1, destination=0), False),
]


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Bi-directional graph
        # N vertices labeld 0, ..., N - 1
        # edges[i] = [ui, vi] bi-directional edge, ui != vi ∀i
        # no duplicated edges, no self edges
        # Is there a vaild path from source to destination?
        # 1 <= N <= 2 * 200_000
        # 0 <= len(edges) <= 200_000
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        found_destination = False
        queue = deque([source])
        visited = set([source])
        while queue:
            node = queue.popleft()
            if node == destination:
                found_destination = True
                break
            for other in graph[node]:
                if other not in visited:
                    queue.append(other)
                    visited.add(other)

        # DFS proved to be slow
        # def dfs(node):
        #     nonlocal found_destination
        #     visited.add(node)
        #     if node == destination:
        #         found_destination = True
        #         return

        #     for other in graph[node]:
        #         if other not in visited:
        #             dfs(other)
        # dfs(source)

        return found_destination


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
