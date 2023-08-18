# https://leetcode.com/problems/open-the-lock/editorial/

from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def get_next_positions(pos: str) -> str:
            numbers = [int(char) for char in pos]
            for i, num in enumerate(numbers):
                for diff in [-1, 1]:
                    next_pos = list(numbers)
                    next_pos[i] = (num + diff) % 10
                    yield "".join(str(n) for n in next_pos)

        start_value = "0000"
        if start_value in deadends:
            return -1

        # BFS
        seen = set(deadends)  # Prevent deadends to be visited in a solution
        queue = deque([(start_value, 0)])
        seen.add(start_value)
        while queue:
            curr, n_steps = queue.popleft()

            if curr == target:
                return n_steps

            for next_pos in get_next_positions(curr):
                if next_pos not in seen:
                    queue.append((next_pos, n_steps + 1))
                    seen.add(next_pos)

        return -1
