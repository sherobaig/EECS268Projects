"""Author: Shero Baig
Lab: 3
KUID: 3093709
Date: Feb 17, 2023
Last Modified: Feb 17, 2023
"""


class Node:
    #create node class
    def __init__(self, entry):
        self.entry = entry
        self.next = None
