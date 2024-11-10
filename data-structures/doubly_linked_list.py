from node import Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        '''Return the size of the list'''
        return self.size

    def __str__(self):
        '''
            Display the list both forward and backward
            Doubly Linked List
            None <-head-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-tail-> None
        '''
        if self.is_empty():
            return 'The list is empty.'

        current = self.head
        print('Doubly Linked List: ')
        print('head -> ', end='')
        while current is not None:
            if current.next is not None:
                print(f'{current.element} <-> ', end='')
            else:
                print(f'{current.element}', end='')
            current = current.next
        print(' <- tail')
        return f'Head = {self.head.element}, Tail = {self.tail.element}, Size = {len(self)}\n'

    def is_empty(self):
        return self.size == 0

    # Insert Methods
    def insert_at_head(self, value):
        new_node = Node(value)  # e.g. Node(element=1, prev=None, next=None)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
        return f'Element: "{new_node.element}" inserted'

    def insert_at_tail(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return f'Element: "{new_node.element}" inserted'

    def insert_at_position(self, index, value):
        if index < 0 or index > len(self):
            print('Index is out of range.')
            return

        if index == 0 or self.is_empty():
            return f'{self.insert_at_head(value)} at position {index}.'
        if index == len(self):
            return f'{self.insert_at_tail(value)} at postion {index}.'

        current = self.head
        new_node = Node(value)
        for _ in range(index - 1):  # Traverse to the node before the target position
            current = current.next

        # update new_node_next to keep reference of remaining list
        new_node.next = current.next
        new_node.prev = current  # update new_node_prev to point to current
        current.next.prev = new_node  # update next_node_prev point back to new node
        current.next = new_node  # update current_node_next to point to new_node

        self.size += 1
        return f'Element: "{value}" inserted at position {index}.'

    # Delete Methods
    def delete_from_head(self):
        if self.is_empty():
            return

        current = self.head
        if len(self) == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            current.next = None

        self.size -= 1
        return f'Element: "{current.element}" removed'

    def delete_from_tail(self):
        if self.is_empty():
            return

        current = self.tail
        if len(self) == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            current.prev = None

        self.size -= 1
        return f'Element: "{current.element}" removed'

    def delete_by_value(self, value):
        if self.is_empty():
            return 'List is empty. Nothing to remove.'
        if len(self) == 1 or value == self.head.element:
            return f'{self.delete_from_head()}.'

        current = self.head
        while current is not None and current.element != value:
            current = current.next

        if current == self.tail:
            return f'{self.delete_from_tail()}.'
        if current is None:
            return f'Element: "{value}" is not found.'

        current.prev.next = current.next
        current.next.prev = current.prev
        current.next = current.prev = None

        self.size -= 1
        return f'Element: "{current.element}" removed.'

    def delete_at_position(self, index):
        if self.is_empty():
            return 'List is empty. Nothing to remove.'
        if index < 0 or index >= len(self):
            return 'Index is out of bound.'

        if len(self) == 1 or index == 0:
            return f'{self.delete_from_head()} at position {index}.'
        if index == len(self) - 1:
            return f'{self.delete_from_tail()} at position {index}.'

        current = self.head
        for _ in range(index):
            current = current.next

        current.prev.next = current.next
        current.next.prev = current.prev
        current.next = current.prev = None

        self.size -= 1
        return f'Element: "{current.element}" removed at position {index}.'

    # Traversal Methods
    def traverse_forward(self):
        current = self.head

        print('List traversed forward: ', end='')
        while current is not None:
            print(f'{current.element} ', end='')
            current = current.next
        print()

    def traverse_backward(self):
        current = self.tail

        print('List traversed backward: ', end='')
        while current is not None:
            print(f'{current.element} ', end='')
            current = current.prev
        print()

    # Utility Methods
    def search(self, value):
        index = 0
        current = self.head
        while current is not None:
            if current.element == value:
                print(
                    f'Element: "{current.element}" found at position: {index}')
                return
            else:
                current = current.next
                index += 1
        print(f'No element found with the specified value: "{value}".')
