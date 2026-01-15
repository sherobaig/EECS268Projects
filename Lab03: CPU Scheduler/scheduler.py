"""Author: Shero Baig
Lab: 3
KUID: 3093709
Date: Feb 17, 2023
Last Modified: Feb 17, 2023
"""

from linkedqueue import LinkedQueue
from process import Process


class Scheduler:
    # initialize scheduler
    def __init__(self, filename):
        self.my_linkedqueue = LinkedQueue()
        self.filename = filename
        with open(self.filename, "r") as file_open:
            self.user_list = []
            for i in file_open:
                line_new = i.split()
                self.user_list.append(line_new)

    def add_process(self):
        # create processes if input file says START, and add them to a queue
        for user in self.user_list:
            if user[0] == "START":
                self.entry = Process(user[1])
                print(self.entry.name + " added to queue")
                self.my_linkedqueue.enqueue(self.entry)

    def run_processes(self):
        # run processes in a queue and then said the process in the back
        for user in self.user_list:
            if self.my_linkedqueue.is_empty():
                # No processes left in queue, skip remaining commands
                continue
            if user[0] == "CALL":
                self.ahead = self.my_linkedqueue.peek_front()
                self.ahead.call(user[1], user[2])
                self.my_linkedqueue.dequeue()
                self.my_linkedqueue.enqueue(self.ahead)
            elif user[0] == "RETURN":
                self.ahead = self.my_linkedqueue.peek_front()
                self.ahead.return_top()
                self.my_linkedqueue.dequeue()
                if self.ahead.stack.is_empty() == False:
                    self.my_linkedqueue.enqueue(self.ahead)
                else:
                    print(self.ahead.name + " process has ended")
            elif user[0] == "RAISE":
                self.ahead = self.my_linkedqueue.peek_front()
                self.my_linkedqueue.dequeue()
                self.ahead.handle_exceptions()
                if not self.ahead.stack.is_empty():
                    self.my_linkedqueue.enqueue(self.ahead)

    def run(self):
        self.add_process()
        self.run_processes()
