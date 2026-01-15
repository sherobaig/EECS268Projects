"""Author: Shero Baig
KUID: 3093709
Date: Feb 10, 2023
Last Modified: Feb 10, 2023
"""
from stack import Stack
from function import Function


class Process:
    def __init__(self, filename):
        # initiailization
        self.my_stack = Stack()
        self.filename = filename
        self.list_input = []
        self.main_name = "main"  # default main name
        with open(self.filename, "r") as file_open:
            for line in file_open:
                line_new = line.split()
                self.list_input.append(line_new)

    def start(self):
        # start call stack
        for value in self.list_input:
            if value[0] == "START" and len(value) > 1:
                self.my_stack.push(value[1])
                if not hasattr(self, 'main_name_set') or not self.main_name_set:
                    self.main_name = value[1]
                    self.main_name_set = True
        print(self.my_stack.peek() + " started")

    def call(self):
        # push process to call stack
        self.call_count = 0
        for value in self.list_input:
            if value[0] == "CALL" and len(value) > 1:
                self.my_stack.push(value[1])
                print(self.main_name + " calls " + self.my_stack.peek())
                self.call_count += 1

    def return_top(self):
        # if text file says return, return what is on top of call stack
        self.return_count = 0
        for value in self.list_input:
            if value[0] == "RETURN":
                if self.call_count == self.return_count:
                    print(self.main_name + " has " + "main" + " return")
                    print(self.main_name + " exited normally")
                    break
                else:
                    print(self.main_name + " has " + self.my_stack.pop() + " return")
                    self.return_count += 1

    def raise_exception(self):
        # if RAISE, raise exception and use Function class to store data
        self.list_of_exceptions = []
        for value in self.list_input:
            if value[0] == "CALL":
                if len(value) > 2 and value[2] == "yes":
                    self.list_of_exceptions.append(Function(value[1], True))
                elif len(value) > 2 and value[2] == "no":
                    self.list_of_exceptions.append(Function(value[1], False))

    def handle_exceptions(self):
        # read whether or not call had yes or no and handle exception accordingly
        for value in self.list_input:
            if value[0] == "RAISE":
                exception_by = ""
                # Find the function that raised the exception (should be on top of stack or in call list)
                if not self.my_stack.is_empty():
                    exception_by = self.my_stack.peek()
                print(self.main_name + " encountered a raised exception by: " + exception_by)
                reversed_list = reversed(self.list_of_exceptions)
                for i in reversed_list:
                    my_string = str(i)
                    list = my_string.split(", ")
                    if list[0] == "True":
                        print(self.main_name + " has exception handled by: " + list[1])
                        return
                    elif list[0] == "False":
                        print(self.main_name + " ends " + list[1] + " due to unhandled exception")
                print("Process ending... exceptions not handled")

    def run(self):
        # orchestrate the process execution
        self.start()
        self.raise_exception()
        self.call()
        self.handle_exceptions()
        self.return_top()
