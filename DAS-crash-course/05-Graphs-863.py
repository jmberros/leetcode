# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

from collections import deque, defaultdict
from binarytree import Node as TreeNode
from binarytree import build2
from typing import List

from utils import run_test_cases

test_cases = [
    (dict(root=[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], target=5, k=2), [7, 4, 1]),
    (dict(root=[1], target=1, k=3), []),
]


class Solution:
    # Time: O(N)
    # Space: O(N)
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        root, target = build2(root), TreeNode(target)
        graph = defaultdict(set)

        def dfs(node):
            if node.left:
                graph[node.val].add(node.left.val)
                graph[node.left.val].add(node.val)
                dfs(node.left)
            if node.right:
                graph[node.val].add(node.right.val)
                graph[node.right.val].add(node.val)
                dfs(node.right)

        dfs(root)

        queue = deque([(target.val, [])])  # (node, nodes visited from target)
        visited = set([target.val])
        result = []
        while queue:
            val, path = queue.popleft()
            if len(path) == k:
                result.append(val)
            elif len(path) < k:
                next_vals = graph[val]
                for next_val in next_vals:
                    if next_val not in visited:
                        queue.append((next_val, path + [next_val]))
                        visited.add(next_val)

        return result

    # Editorial solution, modifing the nodes, adds parent link to each
    def distanceK_2(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        root = build2(root)
        root.parent = None

        def add_parent_link(node):
            nonlocal target
            if node.val == target:
                target = node
            if node.left:
                node.left.parent = node
                add_parent_link(node.left)
            if node.right:
                node.right.parent = node
                add_parent_link(node.right)

        add_parent_link(root)

        queue = deque([(target, [])])
        visited = set()
        result = []
        while queue:
            node, path = queue.popleft()
            if len(path) == k:
                result.append(node.val)
            for next_node in [node.left, node.right, node.parent]:
                if next_node and next_node.val not in visited and len(path) < k:
                    queue.append((next_node, path + [node]))
                    visited.add(next_node)

        return result


if __name__ == "__main__":
    run_test_cases(Solution, test_cases)
