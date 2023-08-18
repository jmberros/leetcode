# https://leetcode.com/problems/shortest-path-with-alternating-colors/

from typing import List
from utils import run_test_cases
from collections import defaultdict, deque

test_cases = [
    (
        dict(n=3, redEdges=[[0, 1]], blueEdges=[[2, 1]]),
        [0, 1, -1]
    )
    (
        dict(n=3, redEdges=[[0, 1], [1, 2]], blueEdges=[]),
        [0, 1, -1]
    ),
    (
        dict(n=6,
             redEdges=[[0, 1], [0, 3], [4, 5]],
             blueEdges=[[3, 4], [3, 5], [5, 2], [2, 1]]),
        [0, 1, 4, 1, 2, 2],
    )
]


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # N nodes in a directed graph, labeled from 0, ..., N - 1
        # There can be self-edges, parallel edges
        # Each edge is red or blue
        # redEdges[i] = [ai, bi], a red edge from ai to bi
        # same for blue ones
        # Return array of N entries, answer[x] = length of the shortest path
        # from node 0 to node x, such that the edge colors alternate.
        # -1 if that's not possible.
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)

        for a, b in redEdges:
            red_graph[a].append(b)
        for a, b in blueEdges:
            blue_graph[a].append(b)

        answer = [-1] * n

        path_length_r = 0
        path_length_b = 0
        for node in range(n):
            answer[node] = path_length
            for next_node in red_graph:
                pass

        return answer


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
