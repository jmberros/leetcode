# https://leetcode.com/problems/number-of-provinces/

from utils import run_test_cases
from collections import deque
from typing import List
import functools


test_cases = [
    ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
    ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
    ([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]], 1),
]


class Solution:
    # Time: O(N^2)
    # Space: O(N^2)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """Count the total number of provinces (i.e. connected components).
        Args:
            isConnected: An NxN matrix (2D list) of connections between cities,
                where 1 <= N <= 200 is the number of cities, and:
                * isConnected[i][j] is 1 or 0.
                * isConnected[i][i] == 1  # Cities are connected to themselves
                * isConnected[i][j] == isConnected[j][i]
        Returns:
            The number of provinces, where a province is group of directly or
            indirectly connected cities and no other cities outside of the
            group.
        """
        seen = set()
        provinces = []
        for i, connections in enumerate(isConnected):
            if i not in seen:
                is_new_province = True
                province = {i}
                seen.add(i)
            else:
                is_new_province = False
                # Find the province(s) where this node has already been seen
                node_provinces = [p for p in provinces if i in p]
                # If this node has been observed in multiple provinces, then it
                # means it connects previously disconnected components of the graph.
                # We need to merge those and add it as a new (bigger) province!
                for p in node_provinces:
                    provinces.remove(p)
                province = functools.reduce(set.union, node_provinces)
                provinces.append(province)

            for j, is_connected in enumerate(connections):  # Only the upper triangle
                if j > i and is_connected:
                    print(f"{i = }, {j = }, {is_connected = }")
                    province.add(j)
                    seen.add(j)

            if is_new_province:
                provinces.append(province)

        print(provinces)
        return len(provinces)

    # Time: O(N^2)
    # Space: O(N)
    def findCircleNum_Dfs(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = [0] * N

        def recursive_visit_dfs(i):
            nonlocal visited
            visited[i] = 1
            for j in range(N):
                if isConnected[i][j] and not visited[j]:
                    recursive_visit_dfs(j)

        num_components = 0
        for i in range(N):
            if not visited[i]:
                num_components += 1
                recursive_visit_dfs(i)

        return num_components

    # Time: O(N^2)
    # Space: O(N)
    def findCircleNum_Bfs(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = [0] * N

        def recursive_visit_bfs(i):
            nonlocal visited
            q = deque([i])
            while q:
                i = q.popleft()
                visited[i] = 1
                for j in range(N):
                    if not visited[j] and isConnected[i][j]:
                        q.append(j)

        num_components = 0
        for i in range(N):
            if not visited[i]:
                num_components += 1
                recursive_visit_bfs(i)

        return num_components

    # Using a Disjoint-Set data structure (aka Union-Find or Merge-Find)
    # because of their APIs
    # Time: O(N^2)
    def findCircleNum_DS(self, isConnected: List[List[int]]) -> int:
        from disjoint_set import DisjointSet

        ds = DisjointSet()
        for i, connections in enumerate(isConnected):
            for j, is_connected in enumerate(connections):
                if is_connected and ds.find(i) != ds.find(j):
                    ds.union(i, j)

        # print(list(ds.itersets()))
        return len(list(ds.itersets()))


if __name__ == '__main__':
    run_test_cases(Solution, test_cases)
