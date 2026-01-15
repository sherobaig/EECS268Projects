"""
Author: Shero Baig
KUID: 3093709
Lab: Lab 6
Date: March 31, 2023
Last Modified: March 31, 2023
Purpose: Read in file
"""

# reading in the file and adding the content in the file onto the lists that were created
class ReadFile:
    def __init__(self,filename):
        self.filename = filename
        input_file = open(self.filename,"r")
        self.user_list = []
        self.flood_map_list = []
        for i in input_file:
            self.user_list.append((i.split()))
            self.flood_map_list.append(list(i.rstrip()))
    # this method provides a way to access this list outside the class
    def import_user_list(self):
        return self.user_list

    # this method provides a way to access a slice from this list outside the class. The slice is from the third element to the last element in the list
    def import_flood_map_list(self):
        return self.flood_map_list[2:]
