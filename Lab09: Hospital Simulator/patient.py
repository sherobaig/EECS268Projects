'''
Author: Shero Baig
KUID: 3093709
Date: 4/28/2023
Lab: lab09
Last modified: Date file was most recently modified
Purpose: create patient class to run program
'''

class Patient:
    def __init__(self, first_name, last_name, age, illness, severity):
        # initialization of patient class
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.illness = illness
        self.severity = severity

    def __lt__(self, other):
        # magic method for less than
        if self.severity == other.severity:
            if self.age == other.age:
                return True
            return self.age > other.age
        return self.severity > other.severity

    def __repr__(self):
        # magic method to print
        return f"Name: {self.last_name}, {self.first_name}\nAge: {self.age}\nSuffers from: {self.illness}\nIllness severity: {self.severity}"
