# https://leetcode.com/problems/daily-temperatures/

from utils import run_test_cases
from typing import List


test_cases = [
    ([73, 74, 75, 71, 69, 72, 76, 73],
     [1, 1, 4, 2, 1, 1, 0, 0]),
    ([30, 40, 50, 60],
     [1, 1, 1, 0]),
    ([30, 60, 90],
     [1, 1, 0])
]


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                answer[j] = i - j  # i >= j

            stack.append(i)

        return answer


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
