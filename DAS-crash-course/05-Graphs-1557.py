# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/


from utils import run_test_cases
from typing import List


test_cases = [
    (dict(n=6, edges=[[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]), [0, 3]),
    (dict(n=5, edges=[[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]), [0, 2, 3]),
]


class Solution:
    # Time:
    # Space:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # DAG, N vertices from 0 to N - 1
        # edges[i] = [from i, to i] directed edge, all distinct
        # Find the smallest set of vertices from which ALL the nodes can be reached.
        # A unique solution is guaranteed to exist.
        # 2 <= n <= 10⁵
        # 1 <= edges.length <= min(10^5, n * (n - 1) / 2)
        nodes_with_incoming_connections = {y for x, y in edges}
        # Reasoning:
        # Any node that is in roots is there because it has *no incoming edges*.
        # This means by definition that it can't be reached from any other node.
        # So they should all be included in the final set. Now, are they enough
        # to cover the full list of nodes? They should, because any node that
        # can't be reached from any other node will have 0 in-edges, hence it
        # would be in the roots group.
        return [x for x in range(n) if x not in nodes_with_incoming_connections]


if __name__ == '__main__':
    run_test_cases(Solution, test_cases)
