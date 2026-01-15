"""Author: Shero Baig
Lab: 4
KUID: 3093709
Date: Feb 24, 2023
Last Modified: Feb 24, 2023
"""




from node import Node
class LinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def insert(self, index, entry):
        if index < 0 or index > self.length:
            raise ValueError("Index out of bounds")

        node_new = Node(entry)
        if self.front is None:
            self.front = node_new
            self.rear = node_new
        elif index == 0:
            node_new.next = self.front
            self.front = node_new
        elif index == self.length:
            self.rear.next = node_new
            self.rear = node_new
        else:
            node_current = self.front
            for i in range(index - 1):
                node_current = node_current.next
            node_new.next = node_current.next
            node_current.next = node_new
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            raise ValueError("Index out of bounds")
        if index == 0:
            self.front = self.front.next
            if self.length == 1:
                self.rear = None
        else:
            node_current = self.front
            for node in range(index - 1):
                node_current = node_current.next
            if index == self.length - 1:
                self.rear = node_current
                node_current.next = None
            else:
                node_current.next = node_current.next.next
        self.length -= 1

    def get_entry(self, index):
        if index < 0 or index >= self.length:
            raise ValueError("Index out of bounds")
        node_current = self.front
        for node in range(index):
            node_current = node_current.next
        return node_current.value

    def set_entry(self, index, entry):
        if index < 0 or index >= self.length:
            raise ValueError("Index out of bounds")
        node_current = self.front
        for node in range(index):
            node_current = node_current.next
        node_current.value = entry

    def clear(self):
        self.front = None
        self.rear = None
        self.length = 0
