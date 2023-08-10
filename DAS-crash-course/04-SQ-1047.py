# 1047. Remove All Adjacent Duplicates In String

from utils import run_test_cases


test_cases = [
    ("abbaca", "ca"),
    ("azxxzy", "ay"),
]


class Solution:
    # Time: O(N)
    # Space: O(N) worst case (no dupes, the stack contians all letters in s)
    def removeDuplicates(self, s: str) -> str:
        """Iteratively removes all contiguous duplicated letters."""
        stack = []
        for letter in s:
            if stack and letter == stack[-1]:
                stack.pop()
            else:
                stack.append(letter)
        return "".join(stack)


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
