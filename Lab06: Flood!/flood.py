"""
Author: Shero Baig
KUID: 3093709
Lab: Lab 6
Date: March 31, 2023
Last Modified: March 31, 2023
Purpose: Tranverse the flood
"""

# importing from readfile.py
from readfile import ReadFile

# initialization
class Flood:
    def __init__(self, filename):
        file_reading = ReadFile(filename)
        self.user_list = file_reading.import_user_list()
        self.flood_map = file_reading.import_flood_map_list()
        self.row = int(self.user_list[0][0])
        self.col = int(self.user_list[0][1])
        self.water_left = int(self.user_list[1][0]) - 1

    # prints the size
    def size_print(self):
        print(f'Size: {len(self.flood_map)},{len(self.flood_map[0])}')

    # print starting position
    def start_position_print(self):
        print(f'Starting position: {self.row},{self.col}')

    # function that solves the flood
    def solve_flood(self, row, col):

        # mark starting position
        self.mark(row, col)
        # if there is no more water left, no more need to solve the flood
        if self.water_left == 0:
            return True
        # check if space is full
        if self.full_map():
            return True
        # check up
        if self.is_valid_move(row - 1, col):
            self.water_left -= 1
            if self.solve_flood(row - 1, col):
                return True
        # check right
        if self.is_valid_move(row, col + 1):
            self.water_left -= 1
            if self.solve_flood(row, col + 1):
                return True
        # check down
        if self.is_valid_move(row + 1, col):
            self.water_left -= 1
            if self.solve_flood(row + 1, col):
                return True
        # check left
        if self.is_valid_move(row, col - 1):
            self.water_left -= 1
            if self.solve_flood(row, col - 1):
                return True
        return False

        # mark with a "~" if there is a space that does not have an "H"
    def mark(self, row, col):
        if self.flood_map[row][col] != "H":
            self.flood_map[row][col] = "~"

    def unmark(self, row, col):
        self.flood_map[row][col] = " "

        # if space is not there then that space is full
    def full_map(self):
        for i in self.flood_map:
            if " " in i:
                return False
        return True
        # run the program under some circumstances
    def run(self):
        if len(self.flood_map) < 1 or len(self.flood_map[0]) < 1:
            return print("Invalid map dimensions.")
        elif self.row > len(self.flood_map) or self.col > len(self.flood_map[0]):
            return print("Invalid starting position.")
        elif self.flood_map[self.row][self.col] != " " or self.row > len(self.flood_map) or self.col > len(self.flood_map[0]):
            return print("Invalid starting position.")
        else:
            self.size_print()
            self.start_position_print()
            self.solve_flood(self.row, self.col)
        # if flood ran out of water, print a statement saying that it ran out of water
        if self.water_left == 0:
            for i in self.flood_map:
                print("".join(i))
            print("Flood ran out of water.")
        else:
        # else, print a statement that flood is complete
            for i in self.flood_map:
                print("".join(i))
            print("Flood complete.")

        # check if each move is valid or not
    def is_valid_move(self, row, col):
        if row < len(self.flood_map) and col < len(self.flood_map[0]):
            if self.flood_map[row][col] == " ":
                return True
