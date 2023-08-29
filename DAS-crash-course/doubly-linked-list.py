from typing import Union


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.dhead = Node("dummy")
        self.dtail = Node("dummy")
        self.dhead.next = self.dtail
        self.dtail.prev = self.dhead
        # Initially, we only have dummy nodes
        # DummyHead-> <-DummyTail

    def add(self, value: int):
        node = Node(value)
        old_head = self.dhead.next

        # There are 4 relations to update:
        # Dummy-> <-New Node-> <-Old head
        old_head.prev = node
        node.next = old_head
        self.dhead.next = node
        node.prev = self.dhead

    def remove(self, node: Node):
        # There are 2 relations to update:
        # Prev-> <-Node to remove-> <-Next
        #     ^^                    ^^
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_front(self, node: Node):
        self.remove(node)
        self.add(node.value)

    def pop(self):
        tail = self.dtail.prev
        if tail.value == "dummy":
            raise Exception("No nodes to pop")
        self.remove(tail)

    def __repr__(self):
        node = self.dhead
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
ll.add(2)
# ll.move_to_front(ll.dhead.next.next)
# ll.pop()

print(ll)
