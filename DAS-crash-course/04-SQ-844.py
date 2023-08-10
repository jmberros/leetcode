# https://leetcode.com/problems/backspace-string-compare/

from utils import run_test_cases


test_cases = [
    (dict(s="ab#c", t="ad#c"), True),
    (dict(s="ab##", t="c#d#"), True),
    (dict(s="a#c", t="b"), False),
    (dict(s="a##c", t="#a#c"), True),
]


class Solution:
    # Time: O(S + T)
    # Space: O(S + T)
    def backspaceCompare(self, s: str, t: str, del_char: str = "#") -> bool:
        """Compares two strings of text editor instructions."""
        def build(s):
            stack = []
            for c in s:
                if c == del_char:
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return "".join(stack)
            
        return build(s) == build(t)


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
