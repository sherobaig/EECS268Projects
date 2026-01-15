
"""
Author: Shero Baig
KUID: 3093709
Lab: Lab 6
Date: March 31, 2023
Last Modified: March 31, 2023
Purpose: Run the program
"""


# from the flood file, importing the Flood class
from flood import Flood
# provides user to enter a file name
def main():
    name_file = input("Enter filename: ")
    try:
        user_flood = Flood(name_file)
        user_flood.run()
    except FileNotFoundError:
        print("File not found.")
if __name__ == "__main__":
    main()
