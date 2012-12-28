"""We're going to model a much simplified Coke machine.  There is only
one product dispensed.  There are count Cokes in the machine
initially.  Cokes cost COST cents, and as soon as the money deposited
reaches that amount, the Coke is dispensed and any change is
returned."""

# Notice that we put constants at the top to make them easy to modify
# if we decide to change the price.  It is conventional to use all
# caps for such constants. 

# COST is the price of a soda from the machine
COST = 65

######################################################################
#                                                                    #
#                           Machine State                            #
#                                                                    #
######################################################################

# The state of the machine is a tuple (pair) with the following 
# components:
#  - the amount of money that has been deposited
#  - the number of sodas remaining in the machine

# Note: by making the structure of the state abstract, the program 
# becomes very easy to maintain and modify.  Any of the following 
# would be easy to do:
#  - change the state implementation to a list, instead of a tuple
#  - change the order of components of the state
#  - add components to the state 
#  - others

def makeMachineState( money, cokes ):
    """This makes a machine state."""
    return ( money, cokes )

# Accessors for the state components

def getMoneyDeposited( state ):
    """Accessor for the 0th component of state:
    money deposited."""
    return state[0]

def getCokesRemaining( state ):
    """Accessor for the 1st component of state:
    cokes remaining."""
    return state[1]


# Setters for the state components

def addToMoneyDeposited( state, coin ):
    """Increment the money deposited by the
    amount of coin."""
    money = getMoneyDeposited( state ) + coin
    return makeMachineState( money, getCokesRemaining( state ) )

def resetMoneyDeposited( state ):
    """Reset the money deposited to 0."""
    return makeMachineState( 0, getCokesRemaining( state ) )

def decCokesRemaining( state ):
    """Decrement the count of cokes remaining by 1."""
    cokes = getCokesRemaining( state )
    return makeMachineState( getMoneyDeposited( state ), cokes - 1 )

# Notice that nothing past this point needs to know how the machine
# state is structured (i.e., that it's a pair).  This only needs to 
# know that there are components for money deposited and for 
# cokes remaining, and that there are certain functions available
# to manipulate the state.

# We want to be able to print out the state of the machine. Note
# that it's good practice to write a function that returns that 
# in string form, rather than to print it directly.  We'll see 
# why later when we talk about the __str__ function for classes. 

def stateStr( state ):
    """This generates a string representing the current machine
    state in a nicely printable form."""
    money = getMoneyDeposited( state )
    cokes = getCokesRemaining( state )
    return ( "\nValue deposited is: $." + str(money).zfill(2) \
                 + "\n" + str(cokes) + " Cokes remaining" )

def isEmpty( state ):
    """Returns a boolean indicating whether the machine is 
    out of Cokes."""
    return ( getCokesRemaining( state ) == 0 )


######################################################################
#                                                                    #
#                           The Simulator                            #
#                                                                    #
######################################################################

def addCoin( state, coin ):
    """This machine only accepts nickles, dimes and
    quarters.  This assumes there is at least one Coke 
    in the machine."""
    if coin in [5, 10, 25]:
        # If the coin is OK, accept it and add it.
        newstate = addToMoneyDeposited( state, coin )

        # If enough money has been deposited, dispense
        # a soda and return change, if any.  Record one
        # less soda in the machine.
        if getMoneyDeposited( newstate ) >= COST:
            print(" Please take your Coke." )
            newstate = decCokesRemaining( newstate )

            # If the following test is non-zero, then there is
            # change to return.  It should never be negative.
            if ( getMoneyDeposited( newstate ) - COST ):
                change = getMoneyDeposited( newstate ) - COST
                print(" Please take your change of $." + str( change ).zfill(2))
                newstate = resetMoneyDeposited( newstate )
        return newstate
    else:
        print(" Sorry! Coin not recognized.")
        return state


def CokeMachine( money=0, count=3 ):
    """This is the top level process for the Coke machine.
    It accepts coins and dispenses Cokes and change when
    the amount deposited equals or exceeds the cost of the product.
    It has two parameters:
       - money: how much has already been deposited toward a 
                product purchase.
       - count: how many Cokes remain in the machine.
    The simulation ends when the machine is empty or the 
    user enters a zero "coin."
    """

    # Initialize the machine state.
    state = makeMachineState( money, count )

    while True:
        # If the machine is empty, stop the simulation.
        if isEmpty( state ):
            print("\n Sorry! The machine is empty!\n" )
            break

        # Accept input (a coin) from the user. Note that
        # input returns a string, but we need an integer.
        coinString = input("\nAdd a coin: ")
        if not coinString.isdigit():
            print(" Sorry!  Coin not recognized." )
            continue

        coin = int( coinString )

        # Use zero to exit the simulation.
        # Notice, we don't return any change here, but we could.
        if coin == 0:
            print(" Thanks for using our machine!" )
            return

        # Otherwise, accept and process the coin. 
        state = addCoin( state, coin )
        
        # Finally, print out the new state of the machine.
        print( stateStr ( state ) )

CokeMachine()
