from node import Node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        '''Return the number of elements in the list.'''
        return self.size

    def __str__(self):
        '''Traverse and print all element in the list '''
        if self.is_empty():
            return 'The list is empty.'

        current = self.head
        print('Singly Linked List: ')
        while current is not None:
            if current.next is not None:
                print(f'{current.element} -> ', end='')
            else:
                print(f'{current.element}', end='')
            current = current.next
        print(' -> None')
        return (f'Head = {self.head.element}, Tail = {self.tail.element}, Size = {len(self)}\n')

    def is_empty(self):
        '''Return True if the list is empty, False if not empty'''
        return self.size == 0

    def add_first(self, element):
        new_node = Node(element)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size += 1

    def add_last(self, element):
        new_node = Node(element)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def pop_first(self):
        if self.is_empty():
            return

        popped_node = self.head.element
        self.head = self.head.next
        self.size -= 1
        if self.size == 0:  # Set tail = None if last element was popped
            self.tail = None

        return f'Removed element: {popped_node}'

    def pop_last(self):
        if self.is_empty():
            return

        popped_node = self.tail.element

        if self.head == self.tail:  # When list has only 1 element
            self.head = self.tail = None
        else:
            current = self.head
            while current.next is not self.tail:
                current = current.next

            current.next = None
            self.tail = current
        self.size -= 1

        return f'Removed element: {popped_node}'

    def insert(self, element, index):
        if index > len(self):
            print('Index is out of range.')
            return

        if index == 0 or self.is_empty():  # Insert at head when list is empty
            self.add_first(element)
            return
        if index == len(self):  # Insert at tail when index = len(list)
            self.add_last(element)
            return

        # Insert at input position
        new_node = Node(element)
        current = self.head
        for _ in range(index - 1):  # index - 1 to offset current being ahead
            if current is not None:
                current = current.next
        if current:
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def remove_element(self, element):
        if self.is_empty():
            return 'List is empty. Nothing to remove.'
        if self.size == 1 or self.head.element == element:
            return self.pop_first()

        previous = None
        current = self.head
        while current and current.element is not element:
            previous = current
            current = current.next
        if current:
            previous.next = current.next
            current = None
            self.size -= 1
            return f'Removed element: {element}'

        return 'Element not found.'

    def remove_at_index(self, index):
        if index >= self.size:
            return 'Index is out of range.'
        if self.is_empty():
            return 'List is empty. Nothing to remove.'
        if self.size == 1 or index == 0:
            return self.pop_first()

        previous = None
        current = self.head
        for _ in range(index):
            if current is not None:
                previous = current
                current = current.next
                print(f'Prev: {previous.element}, Curr: {current.element}')

        previous.next = current.next
        removed_el = current.element
        current = None
        self.size -= 1
        return f'Removed element: {removed_el}'
