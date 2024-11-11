class Queue:
    def __init__(self, queue=None):
        self.queue = queue if queue is not None else []
        self.size = len(self.queue)

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return 'Queue is empty.'

        queue_repr = 'Front -> ' + \
            ' '.join(str(el) for el in self.queue) + ' |'
        return f'{queue_repr}\nSize: {self.size}\n'

    def is_empty(self):
        return self.size == 0
    
    def peek(self):
        if self.is_empty():
            return 'Queue is empty. No elements to peek.'
        return self.queue[0]

    def enqueue(self, element):
        self.queue.append(element)
        self.size += 1
        
    def dequeue(self):
        if self.is_empty():
            return 'Queue is empty. No elements to dequeue.'
        popped_el = self.queue.pop(0)
        self.size -= 1
        return popped_el
