# https://leetcode.com/problems/binary-tree-right-side-view/

from collections import deque
from typing import Optional, List

from binarytree import Node, build
from utils import run_test_cases


test_cases = [
    (
        [1, 2, 3, None, 5, None, 4],
        [1, 3, 4],
    ),
    (
        [1, None, 3],
        [1, 3],
    ),
    ([], []),
]


class Solution:
    # Time: O(N)
    # Space: O(N)
    def rightSideView(self, root: List[int]) -> List[int]:
        if not root:
            return []

        root = build(root)
        q = deque([root])
        view = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # When for loop finishes, the last `node` is the rightmost one
            view.append(node.val)
        return view


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
