#  Files: MyQueue.py, WidgetWorks.py
#
# Description: Define a Queue ADT with operations: Queue, isEmpty,
# enqueue, dequeue, peek,len and print.
#
# Student's Name: Micheal Taylor McCaslin
#
# Student's UT EID: MTM2275
#
# Course Name: CS 313E 
#
# Date Created: 10/12/12
#
# Date Last Modified: 10/12/12


class MyQueue:
    """Define a Queue ADT with operations: Queue, isEmpty,
    enqueue, dequeue, peek,len and print."""
    
    def __init__(self):
        """Initialize the queue"""
        self._items = []
        
    def __str__(self):
        """Print the queue"""
        output = ""
        for x in self._items:
            output = str(x) + " " + output
        return "[ " + output + "]"
            
    def enqueue(self, item):
        """Add item to the queue"""
        self._items.insert(0, item)
    
    def dequeue(self):
        """Remove first item to the queue"""
        return self._items.pop(len(self._items)-1)
    
    def __len__(self):
        """Return length of the queue"""
        return len(self._items)
    
    def isEmpty(self):
        """Boolean of if the queue is empty or not"""
        return self._items == []
    
    def peek(self):
        """Look at the first item in the queue"""
        return self._items[0]
