# https://leetcode.com/problems/deepest-leaves-sum/editorial/

from collections import deque
from typing import Optional, List

from binarytree import Node, build2
from utils import run_test_cases


test_cases = [
    (
        [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8],
        15,
    ),
    (
        [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5],
        19
    ),
]


class Solution:
    # Time: O(N)
    # Space: O(N)
    def deepestLeavesSum(self, root: Optional[Node]) -> int:
        """Sums the values of the leaves of the deepest level.
        Args:
            root: a Node instance.
        Returns:
            The sum of the deepest leaves.
        """
        root = build2(root)
        queue = deque([root])
        while queue:
            sum_of_current_level = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                sum_of_current_level += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return sum_of_current_level


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
