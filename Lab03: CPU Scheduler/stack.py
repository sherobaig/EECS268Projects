"""Author: Shero Baig
Lab: 3
KUID: 3093709
Date: Feb 17, 2023
Last Modified: Feb 17, 2023
"""
from node import Node


class Stack:
    def __init__(self):
        # initialize
        self.above = None

    def push(self, entry):
        # add to top of  stack
        new_top = self.above
        self.above = Node(entry)
        self.above.next = new_top

    def pop(self):
        # remove and return top of  stack
        if self.above == None:
            raise RuntimeError
        else:
            entry = self.above.entry
            self.above = self.above.next
            return entry

    def peek(self):
        # return what is on top of  stack
        if self.is_empty():
            raise Exception
        else:
            return self.above.entry

    def is_empty(self):
        # check whether stack is empty or not
        return self.above == None
