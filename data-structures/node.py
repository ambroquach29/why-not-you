class Node:
    __slot__ = 'element', 'prev', 'next'

    def __init__(self, element, prev_node=None, next_node=None):
        self.element = element
        self.prev = prev_node
        self.next = next_node
