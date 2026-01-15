"""Author: Shero Baig
Lab: 3
KUID: 3093709
Date: Feb 17, 2023
Last Modified: Feb 17, 2023
"""
from stack import Stack
from function import Function


class Process:
    def __init__(self, name):
        # initiailization
        self.name = name
        self.stack = Stack()
        self.stack.push(Function("main", False))

    def call(self, program_name, bool):
        # make sure for process to call stack
        can_handle = (bool.lower() == "yes")
        self.stack.push(Function(program_name, can_handle))
        print(self.name + " calls " + program_name)

    def return_top(self):
        # if text file returns, then return whatever is on top of the call stack
        if self.stack.is_empty():
            print(self.name + " process has ended")
        else:
            print(self.name + " has " + self.stack.pop().name + " return")

    def handle_exceptions(self):
        # read if the call said yes or not then handle the exception
        print(self.name + " encountered a raised exception by " + self.stack.peek().name)
        while True:
            if self.stack.is_empty():
                print(self.name + " ends due to unhandled exception")
                break
            elif self.stack.peek().can_handle_exception == False:
                print(self.name + " ends " + self.stack.pop().name + " due to unhandled exception")
            elif self.stack.peek().can_handle_exception == True:
                print(self.name + " has exception handled by: " + self.stack.pop().name)
                break
