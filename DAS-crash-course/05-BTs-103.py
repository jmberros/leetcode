# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/editorial/
from collections import deque
from typing import Optional, List

from binarytree import Node, build2
from utils import run_test_cases


test_cases = [
    ([3, 9, 20, None, None, 15, 7], [[3], [20, 9], [15, 7]]),
    ([1], [[1]]),
    ([], []),
    ([1, 2, 3, 4, None, None, 5], [[1], [3, 2], [4, 5]]),
]


class Solution:
    # Time: O(N)
    # Space: O(N)
    def zigzagLevelOrder(self, root) -> List[List[int]]:
        if not root:
            return []

        root = build2(root)
        nodes_by_level = []
        queue = deque([root])
        going_right = True
        while queue:
            level_values = []

            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                level_values.append(node.val)

            if not going_right:
                level_values = list(reversed(level_values))
            nodes_by_level.append(level_values)
            going_right = not going_right  # Toggle the direction each level

        return nodes_by_level


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
