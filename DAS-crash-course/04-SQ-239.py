# https://leetcode.com/problems/sliding-window-maximum/

from typing import List
from collections import deque
from utils import run_test_cases


test_cases = [
    (dict(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3), [3, 3, 5, 5, 6, 7]),
    (dict(nums=[1], k=1), [1]),
    (dict(nums=[1, -1], k=1), [1, -1]),
    (dict(nums=[7, 2, 4], k=2), [7, 4]),
]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """Finds the maximum element of each k-sliding window."""
        # 1 <= k <= nums.length
        n = len(nums)
        answer = [None] * (n - k + 1)
        queue = deque()

        for i, num in enumerate(nums):

            while queue and num > nums[queue[-1]]:
                # Remove any elements necessary to keep a decreasing order in the queue
                queue.pop()

            queue.append(i)

            # NOTE: the while loop is not necessary. Since we add one element
            # at a time, you need only delete one element on each pass.
            while queue[0] < i + 1 - k:
                queue.popleft()

            if i + 1 - k >= 0:
                # Since the queue is kept in decreasing order, the first element is the max
                answer[i + 1 - k] = nums[queue[0]]
                # This works as well:
                # answer.append(nums[queue[0]])

            print(f"{i = }, {num = }, {queue = }, {answer = }")

        return answer


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
