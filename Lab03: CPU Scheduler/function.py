"""Author: Shero Baig
Lab: 3
KUID: 3093709
Date: Feb 17, 2023
Last Modified: Feb 17, 2023
"""




class Function:
    def __init__(self, name, can_handle_exception):
        # initialize
        self.name = name
        self.can_handle_exception = can_handle_exception

    def __repr__(self):
        # magic method for reading list
        return (f'Function({self.name}, {self.can_handle_exception})')

    def __str__(self):
        # magic method to print data
        return f"{self.can_handle_exception}, {self.name}"
