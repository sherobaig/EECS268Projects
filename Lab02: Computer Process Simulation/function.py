"""Author: Shero Baig
KUID: 3093709
Date: Feb 10, 2023
Last Modified: Feb 10, 2023
"""
class Function:
    def __init__(self,name, can_handle_exception):
        #initialize
        self.name = name
        self.can_handle_exception = can_handle_exception

    def __repr__(self):
        #reading list magic method
        return (f'Function({self.name}, {self.can_handle_exception})')
    
    def __str__(self):
        #print data magic method
        return f"{self.can_handle_exception}, {self.name}"
