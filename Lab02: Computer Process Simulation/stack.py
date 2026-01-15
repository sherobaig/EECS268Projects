
"""Author: Shero Baig
KUID: 3092709
Date: Feb 10, 2023
Last Modified: Feb 5, 2023
"""
from node import Node
class Stack:
    def __init__(self):
        #initialize
        self.top = None
    
    def push(self,entry):
        #Put the entry at the top of the Stack.
        cur_top = self.top
        self.top = Node(entry)
        self.top.next = cur_top


    def pop(self):
        #Remove and return the value at the top of the stack. Raise RuntimeError otherwise.
        if self.top == None:
            raise RuntimeError
        else:
            popped = self.top
            self.top = self.top.next
            return popped.entry
    
    def peek(self):
        #Return value at the top of the Stack, raise a RuntimeError otherwise.
        if self.is_empty():
            raise RuntimeError
        else:
            return self.top.entry

    def is_empty(self):
        #Return True if Stack is empty, False otherwise.
        return self.top == None
