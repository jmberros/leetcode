# https://leetcode.com/problems/next-greater-element-i/editorial/

from utils import run_test_cases
from typing import List


test_cases = [
    (
        dict(nums1=[0, 4, 1, 3], nums2=[3, 0, 1, 4, 2]),
        [1, -1, 4, 4]
    ),
    (
        dict(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]),
        [-1, 3, -1]
    ),
    (
        dict(nums1=[2, 4], nums2=[1, 2, 3, 4]),
        [3, -1],
    )
]

#
# Solve it like this first, manually, and see what you think while doing it:
#
# [3, 0, 1, 4, 2]

# [3]
# [3, 0]
# [3, 0, <==1] -> pop 0, say NGE[0] = 1, append 1 -> [3, 1]
# [3, 1, <==4] -> pop 1, NGE[1] = 4, pop 3, NGE[3] = 4 -> [4]
# [4, 2]

# NGE = {0: 1, 1: 4, 3: 4}


class Solution:
    # Time: O(N2 + N1)
    # Space: O(N2 + N1)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_great = {}
        stack = []
        for num2 in nums2:
            while stack and num2 > stack[-1]:
                next_great[stack.pop()] = num2
            stack.append(num2)

        answer = []
        for num1 in nums1:
            answer.append(next_great.get(num1, -1))

        return answer


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
