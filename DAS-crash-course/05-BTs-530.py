# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

from collections import deque
from typing import Optional, List

from binarytree import Node, build2
from utils import run_test_cases


test_cases = [
    ([4, 2, 6, 1, 3], 1),
    ([1, 0, 48, None, None, 12, 49], 1),
    ([40, 20, 60, 10, 30], 10),
]


class Solution:
    # Time: O(N)
    # Space: O(N) worst case
    def getMinimumDifference(self, root) -> int:
        root = build2(root)
        print(root)
        upper_bounds = [float("+inf")]
        lower_bounds = [float("-inf")]
        min_diff = float("+inf")

        def backtrack(node, level=0):
            nonlocal upper_bounds
            nonlocal lower_bounds
            nonlocal min_diff
            ub = upper_bounds[-1]
            lb = lower_bounds[-1]
            min_diff = min(min_diff, ub - node.val, node.val - lb)
            print(f"{level * ' '}{node.val = }, {lb = }, {ub = }, {min_diff = }")

            if node.left:
                upper_bounds.append(node.val)
                backtrack(node.left, level + 1)
                upper_bounds.pop()
            if node.right:
                lower_bounds.append(node.val)
                backtrack(node.right, level + 1)
                lower_bounds.pop()

        backtrack(root)
        return min_diff

    # Smarter, using the fact that if you traverse DFS inorder a BST, then
    # the nodes are visited in increasing order! So you can compare any node
    # with the previous one and update the min difference.
    def getMinimumDifference(self, root) -> int:
        root = build2(root)

        previous_value = float("-inf")
        mindiff = float("+inf")

        def dfs_inorder(node):
            nonlocal previous_value
            nonlocal mindiff
            if not node:
                return

            dfs_inorder(node.left)
            mindiff = min(mindiff, node.val - previous_value)
            previous_value = node.val
            dfs_inorder(node.right)

        dfs_inorder(root)
        return mindiff


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
