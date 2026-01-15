"""Author: Shero Baig
KUID: 3093709
Date: April 21, 2023
Lab: Lab8
Purpose: read file and print menu and code to run the program
"""

from binarysearchtree import BinarySearchTree
from pokemon import Pokemon


class FileAndMenu:
    def __init__(self, filename):
        # read in pokedex file and add to bst
        self.my_bst = BinarySearchTree()
        self.filename = filename
        self.list = []
        input_file = open(self.filename, "r")
        for line in input_file:
            self.list.append(line.split())
        for i in self.list:
            self.my_bst.add(Pokemon(i[0], int(i[1]), i[2]))
        self.count_copy = 0

    def pokedex_menu(self):
        # print menu options for user to choose from
        print("1) Search")
        print("2) Add")
        print("3) Print")
        print("4) Remove")
        print("5) Copy")
        print("6) Quit")

    def run_pokedex(self):
        # run pokedex program and allow user to make choice
        user_choice = 0
        while user_choice != "6":
            self.pokedex_menu()
            user_choice = input("Choose your option: ")

            if user_choice == "1":
                # search for pokemon in bst and print if found
                if self.count_copy == 0:
                    try:
                        pokedex_number = int(input("Enter pokedex number: "))
                    except ValueError:
                        print("Please enter a number.")
                        print("")
                        continue
                    if self.my_bst.search(pokedex_number):
                        print("")
                    else:
                        print("Not found.")
                        print("")
                else:
                    choose_tree = input("Which tree? ('original' or 'copy'): ")
                    try:
                        pokedex_number = int(input("Enter pokedex number: "))
                    except ValueError:
                        print("Please enter a number.")
                        print("")
                        continue
                    if choose_tree == "original":
                        if self.my_bst.search(pokedex_number):
                            print("")
                        else:
                            print("Not found.")
                            print("")
                    elif choose_tree == "copy":
                        if copy_bst.search(pokedex_number):
                            print("")
                        else:
                            print("Not found.")
                            print("")
                    else:
                        print("Invalid input.")


            elif user_choice == "2":
                # add pokemon to bst and print if successful
                if self.count_copy == 0:
                    american_name = input("Enter pokemon's american name: ")
                    try:
                        pokedex_number = int(input("Enter pokedex number: "))
                    except ValueError:
                        print("Please enter a number.")
                        print("")
                        continue
                    japanese_name = input("Enter pokemon's japanese name: ")
                    try:
                        self.my_bst.add(Pokemon(american_name, pokedex_number, japanese_name))
                    except RuntimeError:
                        print("No duplicates allowed.")
                        print("")
                else:
                    choose_tree = input("Which tree? ('original' or 'copy'): ")
                    if choose_tree == "original":
                        american_name = input("Enter pokemon's american name: ")
                        try:
                            pokedex_number = int(input("Enter pokedex number: "))
                        except ValueError:
                            print("Please enter a number.")
                            print("")
                            continue
                        japanese_name = input("Enter pokemon's japanese name: ")
                        try:
                            self.my_bst.add(Pokemon(american_name, pokedex_number, japanese_name))
                        except RuntimeError:
                            print("No duplicates allowed.")
                            print("")
                    elif choose_tree == "copy":
                        american_name = input("Enter pokemon's american name: ")
                        try:
                            pokedex_num = int(input("Enter pokedex number: "))
                        except ValueError:
                            print("Please enter a number.")
                            print("")
                            continue
                        japanese_name = input("Enter pokemon's japanese name: ")
                        try:
                            copy_bst.add(Pokemon(american_name, pokedex_num, japanese_name))
                        except RuntimeError:
                            print("No duplicates allowed.")
                            print("")
                    else:
                        print("Invalid input")



            elif user_choice == "3":
                # print bst in order of user's choice
                if self.count_copy == 0:
                    traversal_order = input("What traversal order? (pre-order, in-order, or post-order): ")
                    if traversal_order.lower() == "pre-order":
                        self.my_bst.pre_order_traversal(self.my_bst.visit_node_print)
                    elif traversal_order.lower() == "in-order":
                        self.my_bst.in_order_traversal(self.my_bst.visit_node_print)
                    elif traversal_order.lower() == "post-order":
                        self.my_bst.post_order_traversal(self.my_bst.visit_node_print)
                    else:
                        print("Invalid input. Try again.")
                else:
                    choose_tree = input("Which tree? ('original' or 'copy'): ")
                    if choose_tree == "original":
                        traversal_order = input(
                            "What traversal order? (pre-order, in-order, or post-order): ")
                        if traversal_order.lower() == "pre-order":
                            self.my_bst.pre_order_traversal(self.my_bst.visit_node_print)
                        elif traversal_order.lower() == "in-order":
                            self.my_bst.in_order_traversal(self.my_bst.visit_node_print)
                        elif traversal_order.lower() == "post-order":
                            self.my_bst.post_order_traversal(self.my_bst.visit_node_print)
                        else:
                            print("Invalid input. Try again.")
                    elif choose_tree == "copy":
                        traversal_order = input(
                            "What traversal order? (pre-order, in-order, or post-order): ")
                        if traversal_order.lower() == "pre-order":
                            copy_bst.pre_order_traversal(copy_bst.visit_node_print)
                        elif traversal_order.lower() == "in-order":
                            copy_bst.in_order_traversal(copy_bst.visit_node_print)
                        elif traversal_order.lower() == "post-order":
                            copy_bst.post_order_traversal(copy_bst.visit_node_print)
                        else:
                            print("Invalid input. Try again.")
                    else:
                        print("Invalid input")



            elif user_choice == "4":
                # print bst in reverse order of user's choice
                if self.count_copy == 0:
                    delete_pokedex = int(input("Enter pokedex number: "))
                    if self.my_bst.search(delete_pokedex):
                        self.my_bst.delete(delete_pokedex)
                    else:
                        print("Pokemon not found. Can't delete.")
                else:
                    choose_tree = input("Which tree? ('original' or 'copy'): ")
                    if choose_tree == "original":
                        delete_pokemon = int(input("Enter pokedex number: "))
                        if self.my_bst.search(delete_pokemon):
                            self.my_bst.delete(delete_pokemon)
                        else:
                            print("pokemon not found. can't delete")
                    elif choose_tree == "copy":
                        delete_pokedex = int(input("Enter pokedex number: "))
                        if copy_bst.search(delete_pokedex):
                            copy_bst.delete(delete_pokedex)
                        else:
                            print("pokemon not found. can't delete")
                    else:
                        print("Invalid input")

            elif user_choice == "5":
                # make a copy of the bst
                if self.count_copy < 1:
                    copy_bst = self.my_bst.copy()
                    print("Copy made!")
                    self.count_copy += 1
                else:
                    print("You have already made a copy.")
            elif user_choice == "6":
                # quit program
                print("Program ending...")
                print("")
            else:
                print("Invalid input.")
                print("")
