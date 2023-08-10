# https://leetcode.com/problems/simplify-path/description/

import re
from utils import run_test_cases


test_cases = [
    ("/home/", "/home"),
    ("/.../", "/..."),
    ("/../", "/"),
    ("/home//foo/", "/home/foo"),
    ("/home//foo//../bar", "/home/bar"),
    ("/home/.", "/home"),
    ("/home/./bar", "/home/bar"),
]


class Solution:
    # Time: O(N)
    # Space: O(N)
    def simplifyPath(self, path: str) -> str:
        """Simplifies a Unix-style path to the canonical path."""
        # . current dir
        # .. parent dir
        # multiple slashes are like one slash
        # anything else is a dir name (e.g. "...")
        # Canonical path:
        # * starts with exactly one /
        # * two dirs are separated by a single /
        # * has no trailing /
        # * no periods or double periods
        stack = []
        for path_part in path.split("/"):
            if path_part == "..":
                if stack:
                    stack.pop()
            elif path_part == "." or not path_part:
                continue
            else:
                stack.append(path_part)

        print(f"{stack = }")
        return "/" + "/".join(stack)


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
