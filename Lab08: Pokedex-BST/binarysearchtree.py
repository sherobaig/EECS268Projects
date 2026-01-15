"""Author: Shero Baig
KUID: 3093709
Date: April 21, 2023
Lab: Lab8
Purpose: binary search tree
"""

from binarynode import BinaryNode


class BinarySearchTree:
    #initialization
    def __init__(self, root=None):
        self.root = root

    def add(self, item):
        # add to tree
        if self.root == None:
            self.root = BinaryNode(item)
        else:
            self.rec_add(item, self.root)

    def rec_add(self, item, current_node):
        # behind the scenes recursive func to add
        if item < current_node.entry:
            if current_node.left == None:
                current_node.left = BinaryNode(item)
            else:
                self.rec_add(item, current_node.left)
        elif item > current_node.entry:
            if current_node.right == None:
                current_node.right = BinaryNode(item)
            else:
                self.rec_add(item, current_node.right)
        else:
            raise RuntimeError

    def visit_node_print(self, current_node):
        # print visited node
        print(current_node.entry)

    def in_order_traversal(self, function):
        # in order traversal
        if self.root != None:
            self.rec_in_order_traversal(self.root, function)

    def rec_in_order_traversal(self, current_node, function):
        # recursive in order traversal function
        if current_node != None:
            self.rec_in_order_traversal(current_node.left, function)
            function(current_node)
            self.rec_in_order_traversal(current_node.right, function)

    def pre_order_traversal(self, function):
        # pre order traversal
        if self.root != None:
            self.rec_pre_order_traversal(self.root, function)

    def rec_pre_order_traversal(self, current_node, function):
        # recursive pre order traversal
        if current_node != None:
            function(current_node)
            self.rec_pre_order_traversal(current_node.left, function)
            self.rec_pre_order_traversal(current_node.right, function)

    def post_order_traversal(self, function):
        # post order traversal
        if self.root != None:
            self.rec_post_order_traversal(self.root, function)

    def rec_post_order_traversal(self, cur_node, func):
        # recursive post order traversal
        if cur_node != None:
            self.rec_post_order_traversal(cur_node.left, func)
            self.rec_post_order_traversal(cur_node.right, func)
            func(cur_node)

    def search(self, target_key):
        # search for target key in tree and return true if found and false if not found
        return self.rec_search(target_key, self.root)

    def rec_search(self, target_key, current_node):
        # recursive search function
        if current_node == None:
            return False
        elif current_node.entry == target_key:
            print(current_node.entry)
            return True
        else:
            if self.rec_search(target_key, current_node.left):
                return True
            if self.rec_search(target_key, current_node.right):
                return True
            return False

    def delete(self, val):
        # delete node from tree
        self.rec_delete(val, self.root)

    def rec_delete(self, val, current_node):
        # recursive delete function
        if current_node is None:
            return current_node
        if val < current_node.entry:
            current_node.left = self.rec_delete(val, current_node.left)
        elif val > current_node.entry:
            current_node.right = self.rec_delete(val, current_node.right)
        else:
            # 0 child case
            if current_node.left is None and current_node.right is None:
                current_node = None

            # 1 child case
            elif (current_node.left != None and current_node.right == None) or (
                    current_node.left == None and current_node.right != None):
                if current_node.left is None:
                    current_node = current_node.right
                else:
                    current_node = current_node.left

            # 2 child case
            else:
                temp = self.minimum_value(current_node.left)
                print(temp.entry)
                current_node.entry = temp.entry
                current_node.left = self.rec_delete(temp.entry, current_node.left)
        return current_node

    def copy(self):
        # copy tree
        if not self.root:
            return self.root
        copy_creation = self.rec_copy(self.root)
        new_copy_bst = BinarySearchTree(copy_creation)
        return new_copy_bst

    def rec_copy(self, current_node):
        # recursive copy function
        if not current_node:
            return current_node
        root_copy = BinaryNode(current_node.entry)
        root_copy.left = self.rec_copy(current_node.left)
        root_copy.right = self.rec_copy(current_node.right)
        return root_copy

    def minimum_value(self, current_node):
        # find minimum value in tree
        while current_node.right is not None:
            current_node = current_node.right
        return current_node
