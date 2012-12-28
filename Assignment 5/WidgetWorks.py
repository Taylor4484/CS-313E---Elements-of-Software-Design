#  Files: MyQueue.py, WidgetWorks.py
#
# Description: An interactive widget ordering system to handle orders of widgets
# containing data about customer name, widget color and quantity.
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




#import MyQueue ADT
from MyQueue import *



######################################################################
#                                                                    #
#                          Order Class                               #
#                                                                    #
######################################################################

class Order:
    """ An order contains four fields: an order number (assigned
    sequentially when an order is created), a customer name, widget color,
    and quantity. The last three are supplied by the customer at the
    prompt. """

    NumberOfOrders = 1

    def __init__(self, name, color, qty):
        """Initialize the order object with a Customer Name, Order Color
        and order quantity"""
        
        self._num = Order.NumberOfOrders
        self._name = name
        self._color = color
        self._qty = qty
       
        #increase the numberOfOrders counter
        Order.NumberOfOrders += 1
                
    def getNumber(self):
        """Return Order number"""
        return self._num

    def getName(self):
        """Return customer name for an order"""
        return self._name

    def getColor(self):
        """Return the color of the order"""
        return self._color

    def getQty(self):
        """Return the order quanity"""
        return self._qty

    def __str__(self):
        """Return the order summary"""
        return "Order " + str(self.getNumber()) + ": customer " + self.getName() + \
        " requests " + str(self.getQty()) + " " + self.getColor() + " widgets."


######################################################################
#                                                                    #
#                          Main Driver                               #
#                                                                    #
######################################################################


def TestFactory():
    """An interactive widget ordering system to handle orders of widgets
    containing data about customer name, widget color and quantity."""

    #Order Variable Reset
    name = ""
    color = ""
    num = ""

    #Order queue
    queue = MyQueue()

    #Keep program running until exit
    while True:

        #welcome message
        print("\nWelcome to the Waskelly Wabbit Widget Works automated ordering system!")

        #user inputs name (or type 'exit')           
        name = input("\n\tPlease input customer name (or exit): ")

        #check for actual input, if none, re-ask
        if name == "":
            continue

        #check lower case name for the word 'exit'
        if name.lower() == "exit":
            break

        #user inputs order color    
        color = input("\tPlease select desired widget color (red, white, blue): ").lower()

        #if not defined color, cancel order
        if not color in ["red", "white", "blue"]:
            print("\t\tSorry, %s not a color we offer. Order cancelled." %color)
            continue

        #iser inputs order quantity
        num = input("\tExcellent choice. How many %s widgets do you want? " %color)

        #if value not a positive whole number, cancel order
        if not num.isnumeric():
            print("\t\tBad quantity. Order cancelled.")
            continue

        #if made this far, all values are valid, create order
        newOrder = Order(name, color, num)

        #add new order to the order queue
        queue.enqueue(newOrder)

        #order confimation message
       

    #on exit process orders     
    print("\nNow processing orders:\n")

    #iterate over order queue, dequeue orders
    for order in range(len(queue)):
        print("  Order shipped:\t", queue.dequeue())

    #all orders processed message
    print("\nQueue empty")


TestFactory()
