# https://leetcode.com/problems/make-the-string-great/description/

from utils import run_test_cases


test_cases = [
    ("leEeetcode", "leetcode"),
    ("abBAcC", ""),
    ("s", "s"),
]


class Solution:
    # Time: O(N)
    # Space: O(N)
    def makeGood(self, s: str) -> str:
        # S has lower and upper case English letters (26 * 2)
        # Adjacent letters can't be the same letter in different cases
        # If pairs like that are found, remove BOTH letters
        stack = []
        for letter in s:
            if stack:
                is_same_letter = stack[-1].casefold() == letter.casefold()
                has_different_case = stack[-1].isupper() != letter.isupper()
                combination_is_banned = is_same_letter and has_different_case
                if combination_is_banned:
                    stack.pop()
                    continue
    
            stack.append(letter)

        return "".join(stack)


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
