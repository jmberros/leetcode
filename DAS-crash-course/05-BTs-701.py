# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/

from collections import deque
from typing import Optional, List

from binarytree import Node, build2
from utils import run_test_cases, isValidBST, TreeNode


test_cases = [
    (dict(root=[4, 2, 7, 1, 3], val=5),
     [4, 2, 7, 1, 3, 5]),
    (dict(root=[40, 20, 60, 10, 30, 50, 70], val=25),
     [40, 20, 60, 10, 30, 50, 70, None, None, 25]),
    (dict(root=[4, 2, 7, 1, 3, None, None, None, None, None, None], val=5),
     [4, 2, 7, 1, 3, 5]),
    (dict(root=[8, None, 55, 39, None, 11, None, None, 23, None, None], val=17),
     [8, None, 55, 39, None, 11, None, None, 23, 17]),
    (dict(root=[], val=1),
     [1])
]


class Solution:
    # Time: Expected O(log N), Worst O(N)
    # Space: Expected O(log N), Worst O(N)
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        root = build2(root)
        print(root)

        if not root:
            return TreeNode(val)

        def recursive_insert(node, new_val):
            if new_val > node.val:
                if node.right:
                    recursive_insert(node.right, new_val)
                else:
                    node.right = TreeNode(new_val)
            else:  # new_val < node.val
                if node.left:
                    recursive_insert(node.left, new_val)
                else:
                    node.left = TreeNode(new_val)

        recursive_insert(root, val)
        assert isValidBST(root)
        print(root)
        # return root
        return list(node.val for node in root)


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
