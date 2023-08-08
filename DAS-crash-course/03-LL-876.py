# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/description/

# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

from utils import run_test_cases
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


test_cases = [
    ([1, 2, 3, 4, 5], [3, 4, 5]),
    ([1, 2, 3, 4, 5, 6], [4, 5, 6]),
]


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Finds the middle node of a linked list."""
        # Linked List of length 0
        if head is None:
            return None

        # Linked List of length 1
        if head.next is None:
            return head

        # lengths >= 2
        left = right = head
        print(f"{left = }, {right = }")

        while right is not None and right.next is not None:
            left = left.next
            right = right.next.next

        return left

# Odd length case:
# (0) -> (1)L -> (2)R
# Even length case:
# (0) -> (1)L -> (2)R -> (3) -> None
# (0) -> (1) -> (2)L -> (3) -> None R


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
