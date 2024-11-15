class Stack:
    def __init__(self, stack=None):
        self.stack = stack if stack is not None else []
        self.size = len(self.stack)

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return 'Stack is empty.'

        stack_repr = 'Top -> ' + \
            ' '.join(str(el) for el in self.stack) + ' |'
        return f'{stack_repr}\nSize: {self.size}\n'

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty():
            return 'Stack is empty. No elements to peek.'
        return self.stack[0]

    def push(self, element):
        self.stack.insert(0, element)
        self.size += 1

    def pop(self):
        if self.is_empty():
            return 'Stack is empty. No elements to pop.'
        popped_el = self.stack.pop(0)
        self.size -= 1
        return popped_el
