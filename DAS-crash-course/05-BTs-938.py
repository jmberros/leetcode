# https://leetcode.com/problems/range-sum-of-bst/

from collections import deque
from typing import Optional, List

from binarytree import Node, build2
from utils import run_test_cases


test_cases = [
    (dict(root=[10, 5, 15, 3, 7, None, 18], low=7, high=15), 32),
    (dict(root=[10, 5, 15, 3, 7, 13, 18, 1, None, 6], low=6, high=10), 23),
]


class Solution:
    # Time: O(N)
    # Space: O(log2 N), O(N) worst case
    def rangeSumBST(self, root, low: int, high: int) -> int:
        if not root:
            return 0

        root = build2(root)
        sum_ = 0
        # Traverse DFS, preorder

        def dfs_traversal(node):
            if not node:
                return

            nonlocal sum_
            if node.val >= low and node.val <= high:
                sum_ += node.val

            if node.val > low:
                dfs_traversal(node.left)
            if node.val < high:
                dfs_traversal(node.right)

        dfs_traversal(root)
        return sum_


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
