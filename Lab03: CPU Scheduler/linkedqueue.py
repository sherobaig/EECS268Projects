"""Author: Shero Baig
Lab: 3
KUID: 3093709
Date: Feb 17, 2023
Last Modified: Feb 17, 2023
"""




from node import Node


class LinkedQueue:
    def __init__(self):
        self.ahead = None
        self.rear = None

    def enqueue(self, entry):
        node_new = Node(entry)
        if self.ahead == None:
            self.ahead = node_new
            self.rear = node_new
        else:
            self.rear.next = node_new
            self.rear = node_new

    def dequeue(self):
        if self.ahead == None:
            raise RuntimeError
        value_popped = self.ahead.entry
        self.ahead = self.ahead.next
        if self.ahead == None:
            self.rear = None
        return value_popped

    def peek_front(self):
        if self.is_empty():
            raise RuntimeError
        else:
            return self.ahead.entry

    def is_empty(self):
        return self.ahead is None
