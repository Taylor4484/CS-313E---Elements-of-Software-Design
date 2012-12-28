#  Files: Stack.py, Calculator.py
#
# Description: Hand Class, defines a hand of 5 playing cards for poker.
#
# Student's Name: Micheal Taylor McCaslin
#
# Student's UT EID: MTM2275
#
# Course Name: CS 313E 
#
# Date Created: 10/6/12
#
# Date Last Modified: 10/6/12


class Stack:
    """Define a Stack ADT with operations: Stack, isEmpty,
    push, pop, peek, and len."""
    
    def __init__(self):
        """Initialize the stack"""
        self._items = []
        
    def isEmpty(self):
        """Boolean of if the stack is empty or not"""
        return self._items == []
    
    def push(self, item):
        """Push an item onto the stack"""
        self._items.insert(0, item)
        
    def pop(self):
        """Pop the first item off the stack and return it"""
        return self._items.pop(0)
    
    def peek(self):
        """Look at the first item in the stack"""
        return self._items[0]
    
    def __len__(self):
        """Return the length of the stack"""
        return len(self._items)
    
    def __str__(self):
        """Print the Stack"""
        output = ""
        for x in self._items:
            output = output + str(x) + " "
        return "[ " + output + "]"
