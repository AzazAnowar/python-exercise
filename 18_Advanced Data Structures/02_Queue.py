"""
Develop a queue structure with methods for enqueue, dequeue, and
displaying the current queue, using collections.deque.
"""

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return "Queue is empty"

    def display(self):
        return list(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

# Example usage:
q = Queue()
q.enqueue(10)
q.enqueue(20)
print("Queue:", q.display())
print("Dequeued item:", q.dequeue())
