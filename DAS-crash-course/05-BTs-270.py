# https://leetcode.com/problems/closest-binary-search-tree-value/editorial/

from collections import deque
from typing import Optional, List

from binarytree import Node, build2
from utils import run_test_cases, isValidBST, TreeNode


test_cases = [
    (dict(root=[4, 2, 5, 1, 3], target=3.714286), 4),
    (dict(root=[1], target=4.428571), 1),
    (dict(root=[4, 1, 5], target=-10), 1),
    (dict(root=[4, 2, 5, 1, 3], target=3.5), 3),
]


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """Finds the node value closest to target. Chooses the smallest if there's a tie.

        Args:
            root: An instance of TreeNode, the root of a BST.
            target: A float to use as condition for the search.
        Returns:
            The node value that's closest to the target.
        """
        # Contraints:
        # 0 <= Node.val <= 1e9, int
        # -1e9 <= target <= 1e9, float
        root = build2(root)
        answer = None

        # Special case:
        # If the target is < 0, then the answer is the smallest (i.e. the leftmost) node
        if target < 0:
            node = root
            while node.left:
                node = node.left
            return node.val

        def compare(t, others):
            # FIXME : Make this clearer?
            tuples_to_compare = [(abs(t - other), other) for other in others]
            return min(tuples_to_compare)[1]

        def find_recursively(node, lb, ub):  # lb, ub: {lower, upper} bound
            nonlocal answer
            if target > node.val:
                if node.right:
                    find_recursively(node.right, lb=node.val, ub=ub)
                else:
                    answer = compare(target, others=[lb, ub, node.val])
            elif target < node.val:
                if node.left:
                    find_recursively(node.left, lb=lb, ub=node.val)
                else:
                    answer = compare(target, others=[lb, ub, node.val])
            else:
                answer = node.val

        find_recursively(root, float("-inf"), float("+inf"))
        return answer


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
