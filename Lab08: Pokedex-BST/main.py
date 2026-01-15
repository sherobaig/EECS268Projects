"""Author: Shero Baig
KUID: 3093709
Date: April 21, 2023
Lab: Lab8
Purpose: allow user to enter file name to run the program
"""

from fileandmenu import FileAndMenu

def main():
    # allow user to enter a file name and run program
    file_name = input("Enter filename: ")
    try:
        my_file = FileAndMenu(file_name)
        my_file.run_pokedex()
    except FileNotFoundError:
        print("File not found.")
if __name__ == "__main__":
    main()
