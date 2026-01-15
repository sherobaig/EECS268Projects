'''
Author: Shero Baig
KUID: 3093709
Date: 4/28/2023
Lab: lab09
Last modified: Date file was most recently modified
Purpose: Process the file and print the output
'''

from hospital import Hospital
from maxheap import Maxheap

class Processfile:
    def __init__(self):
        # initialization of process file class
        self.my_heap = Maxheap()



    def process(file_name, hospital):
        # process the file and print the output

        try:
            with open(file_name, 'r') as file:
                for every_line in file:
                    order = every_line.strip().split()

                    if order[0] == "ARRIVE":
                        hospital.arrive(order[1], order[2], int(order[3]), order[4], int(order[5]))
                    elif order[0] == "NEXT":
                        patient = hospital.next()
                        if patient:
                            print("\nNext patient:")
                            print(patient)
                        else:
                            print("")
                            print("No patients waiting.")
                    elif order[0] == "TREAT":
                        if hospital.count() == 0:
                            print("")
                            print("No patients left to treat.")
                        else:
                            hospital.treat()

                    elif order[0] == "COUNT":
                        if hospital.count() > 1:
                            print("")
                            print(f"There are {hospital.count()} patients waiting.")
                        elif hospital.count() == 1:
                            print("")
                            print(f"There is {hospital.count()} patient waiting.")
                        else:
                            print("")
                            print("There are no patients waiting.")
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
        except ValueError:
            print("Invalid input in the file. Check the file format.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    hospital = Hospital()

    file_name = input("Enter the name of the file: ")
    Processfile.process(file_name, hospital)
