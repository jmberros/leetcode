# https://leetcode.com/problems/validate-binary-search-tree/description/

from collections import deque
from typing import Optional, List

from binarytree import Node, build2
from utils import run_test_cases


test_cases = [
    ([2, 1, 3], True),
    ([5, 1, 4, None, None, 3, 6], False),
    ([5, 4, 6, None, None, 3, 7], False),
    ([2, 2, 2], False),
]


class Solution:
    # Time: O(N)
    # Space: O(N) worst case
    def isValidBST(self, root) -> bool:
        if isinstance(root, list):
            root = build2(root)
        print(root)

        def validate(node, lb, ub):
            # Test if current node is within valid limits or raise
            if node.val <= lb or node.val >= ub:
                return False
            left_is_valid = (node.left is None) or validate(node.left, lb=lb, ub=node.val)
            right_is_valid = (node.right is None) or validate(node.right, lb=node.val, ub=ub)
            return left_is_valid and right_is_valid

        return validate(root, float("-inf"), float("+inf"))


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
