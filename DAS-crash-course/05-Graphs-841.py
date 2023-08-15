# https://leetcode.com/problems/keys-and-rooms/

from collections import deque
from utils import run_test_cases
from typing import List


test_cases = [
    ([[1], [2], [3], []], True),
    ([[1, 3], [3, 0, 1], [2], [0]], False),
    ([[1, 2, 3], [3, 4, 5], [], [0], [], [], [7], []], False)
]


class Solution:
    # Time: O(N + E)
    # Space: O(N)
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # N rooms labeled 0, ..., N - 1 (2 <= N <= 1000)
        # rooms[i] is the set of keys found at room i, (0 <= room[i] <= 1000)
        # 1 <= Σ rooms[i] <= 1
        # 0 <= rooms[i][j] < n, all unique, no repeated keys in a single room
        # Want to visit all rooms, need the key. Start from 0.
        # Say if you can or cannot visit all the rooms.

        # DFS Solution

        def dfs(room):
            keys = rooms[room]
            visited.add(room)
            for other_room in keys:
                if other_room not in visited:
                    dfs(other_room)

        visited = set()
        dfs(0)
        return len(visited) == len(rooms)

    def canVisitAllRooms2(self, rooms: List[List[int]]) -> bool:
        # BFS Solution
        rooms_to_visit = deque([0])
        visited = set()
        while rooms_to_visit:
            room = rooms_to_visit.popleft()
            keys = rooms[room]
            visited.add(room)
            for other_room in keys:
                if other_room not in visited:
                    rooms_to_visit.append(other_room)

        return len(visited) == len(rooms)


if __name__ == '__main__':
    run_test_cases(Solution, test_cases)
