"""Author: Shero Baig
KUID: 3093709
Date: April 21, 2023
Lab: Lab8
Purpose: Pokemon and magic methods
"""
class Pokemon:
    def __init__(self,american_name, number, japanese_name):
        #initializes pokemon class with american name, pokedex number, and japanese name
        self.american_name = american_name
        self.number = number
        self.japanese_name = japanese_name

    def __gt__(self,other):
        #magic method for greater than
        if self.number > other:
            return True
        else:
            return False
    def __eq__(self,other):
        #magic method for equal to
        if self.number == other:
            return True
        else:
            return False
    def __lt__(self,other):
        #magic method for less than
        if self.number < other:
            return True
        else:
            return False

    def __str__(self):
        #magic method to print
        magic_string = "American name: " + str(self.american_name) + "     Japanese name: " + str(self.japanese_name) + "    Pokedex number: " + str(self.number)
        return magic_string
