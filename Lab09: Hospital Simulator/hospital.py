'''
Author: Shero Baig
KUID: 3093709
Date: 4/28/2023
Lab: lab09
Last modified: Date file was most recently modified
Purpose: create hospital class to run program
'''

from maxheap import Maxheap
from patient import Patient
class Hospital:
    def __init__(self):
        # initialization of hospital class
        self.my_heap = Maxheap()

    def arrive(self, first_name, last_name, age, illness, severity):
        # add patient to the heap
        self.my_heap.push(Patient(first_name, last_name, age, illness, severity))

    def next(self):
        # return the next patient
        return self.my_heap.peek()

    def treat(self):
        # treat the next patient
        return self.my_heap.pop()

    def count(self):
        # return the number of patients
        return self.my_heap.count()
