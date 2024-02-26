"""
WRITE YOUR PROGRAM HEADER HERE
"""

# Implementation of a Stack
class Stack():
    def __init__(self):
        # Initialize an empty list to store the elements of the stack
        self.__items = []

    def isEmpty(self):
        # Check if the stack is empty by examining the length of the internal list
        return len(self.__items) == 0

    def add(self, item):
        # Add an item to the top of the stack by appending it to the list
        self.__items.append(item)

    def remove(self):
        # Remove and return the top item from the stack if it is not empty
        if not self.isEmpty():
            return self.__items.pop()


# Implementation of a Queue data structure
class Queue():
    def __init__(self):
        # Initialize an empty list to store the elements of the queue
        self.__items = []

    def isEmpty(self):
        # Check if the queue is empty by examining the length of the internal list
        return len(self.__items) == 0

    def add(self, item):
        # Add an item to the end of the queue by appending it to the list
        self.__items.append(item)

    def remove(self):
        # Remove and return the front item from the queue if it is not empty
        if not self.isEmpty():
            return self.__items.pop(0)