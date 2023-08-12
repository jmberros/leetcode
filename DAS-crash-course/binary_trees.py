from collections import deque
from typing import Generator, Optional

from binarytree import Node


def dfs(
    node: Optional[Node],
    traversal: str = "preorder"
) -> Generator[Node, None, None]:
    if node is None:
        return
    if traversal == "preorder":
        yield node
    yield from dfs(node.left, traversal)
    if traversal == "inorder":
        yield node
    yield from dfs(node.right, traversal)
    if traversal == "postorder":
        yield node


def bfs(root: Optional[Node]) -> Generator[Node, None, None]:
    if root is None:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        yield node
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
