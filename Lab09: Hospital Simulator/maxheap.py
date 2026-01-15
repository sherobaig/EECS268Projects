'''
Author: Shero Baig
KUID: 3093709
Date: 4/28/2023
Lab: lab09
Last modified: Date file was most recently modified
Purpose: create maxheap class to run program
'''

class Maxheap:
    def __init__(self):
        # initialization of maxheap
        self.heap_list = []

    def push(self, patient):
        # add patient to the heap
        self.heap_list.append(patient)
        self._heapify_up(len(self.heap_list) - 1)

    def pop(self):
        # remove patient from the heap
        if len(self.heap_list) == 0:
            return None
        patient = self.heap_list[0]
        self.heap_list[0] = self.heap_list[-1]
        self.heap_list.pop()
        self._heapify_down(0)
        return patient

    def peek(self):
        # return the next patient
        return self.heap_list[0] if len(self.heap_list) > 0 else None

    def count(self):
        # return the number of patients
        return len(self.heap_list)

    def _parent(self, index):
        # return the parent of the index
        return (index - 1) // 2

    def _left_child(self, index):
        # return the left child of the index
        return 2 * index + 1

    def _right_child(self, index):
        # return the right child of the index
        return 2 * index + 2

    def _heapify_up(self, index):
        # heapify up the heap
        parent = self._parent(index)
        while index > 0 and self.heap_list[index] < self.heap_list[parent]:
            self.heap_list[index], self.heap_list[parent] = self.heap_list[parent], self.heap_list[index]
            index = parent
            parent = self._parent(index)

    def _heapify_down(self, index):
        # heapify down the heap
        max_index = index
        left = self._left_child(index)
        if left < len(self.heap_list) and self.heap_list[left] < self.heap_list[max_index]:
            max_index = left

        right = self._right_child(index)
        if right < len(self.heap_list) and self.heap_list[right] < self.heap_list[max_index]:
            max_index = right

        if index != max_index:
            self.heap_list[index], self.heap_list[max_index] = self.heap_list[max_index], self.heap_list[index]
            self._heapify_down(max_index)
