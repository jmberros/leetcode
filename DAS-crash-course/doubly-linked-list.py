from typing import Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.dummy_head = Node("dummy")
        self.dummy_tail = Node("dummy")
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    @property
    def head(self) -> Optional[Node]:
        return self.dummy_head.next

    @property
    def tail(self) -> Optional[Node]:
        return self.dummy_tail.prev

    def add(self, value: int):
        node = Node(value)
        node.next = self.head  # N -> prev head
        self.head.prev = node  # N <- prev head
        node.prev = self.dummy_head  # DH <- N
        self.dummy_head.next = node  # DH -> N

    def move_to_front(self, node: Node):
        self.remove(node)
        self.add(node.value)

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def pop(self):
        if self.tail.value == "dummy":
            raise Exception("No nodes to remove")

        self.remove(self.tail)

    def __repr__(self):
        node = self.dummy_head
        s = ""
        while node:
            s += f"{node.value}"
            if not node.next:
                break
            node = node.next
            s += " -> "
        return s


ll = DoublyLinkedList()

ll.add(1)
ll.pop()
ll.pop()


print(ll)
