"""
   A Simple Calculator
   Programmer: Bill Young

   This is an example of imperative Python programming (no classes).
   It's a very simple interactive calculator, emulating a single address
   computer.  This version only accepts non-negative integer
   arguments, though it can yield negative and float results.

   The instructions are:
     clear     ; zero the accumulator
     show      : display the accumulator value
     add k     ; add k to the accumulator
     sub k     ; subtract k from the accumulator
     mult k    ; multiply accumulator by k
     div k     ; divide accumulator by k
     help      ; show commands
     exit      ; terminate the computation
"""

def zeroaryOp( op ):
    "Recognize an operator of 0 arguments"
    return op in ["clear", "show", "exit", "help"] 

def unaryOp( op ):
    "Recognize an operator of 1 argument"
    return op in ["add", "sub", "mult", "div"]


def legalCommand ( tokens ):
    """Given a list of tokens, decide whether or not it
    represents a legal command."""
    if not tokens:
        return False
    # Every instruction has an operator.
    # For safety, remove extra white space and
    # put into lower case. 

    op = tokens[0].strip().lower()

    # The zeroary ops should not have an argument.
    if zeroaryOp( op ):
        return ( len( tokens ) == 1 )

    # The unary ops should have one integer argument.
    if unaryOp( op ):
        return (     len( tokens ) == 2 \
                 and tokens[1].isdigit() )
    return False

def printAccumulator( value ):
    """Print the accumulator in a nice format."""
    print( "The accumulator contains: ", value )

def helpMessage():
    """This is the message printed when 'help' is entered."""
    return( """
The available instructions are:
     clear     ; zero the accumulator
     show      : display the accumulator value
     add k     ; add k to the accumulator
     sub k     ; subtract k from the accumulator
     mult k    ; multiply accumulator by k
     div k     ; divide accumulator by k
     help      ; show commands
     exit      ; terminate the computation
""")



def flatCalc ():
    """Implements the top level loop of our calculator.  Accept
    commands, parse them, and execute them."""
    # The accumulator is initially 0.
    accumulator = 0

    while True:
        command = input("\nEnter a command: " )
        # Break the command into tokens (words).
        tokens = command.split()
        # print( tokens )

        # If the command is not syntactically legal,
        # give the user another try. 
        if not legalCommand( tokens ):
            print( "Illegal command.  Try again." )
            continue
            
        # Every command must have an operator; extract it.
        op = tokens[0].lower()

        # Some commands (the unary ones) also have an argument.
        if unaryOp( op ):
            # This value in tokens is a string;
            # we need an integer.
            arg = int( tokens[1] )

        # Branch on the operator to do the right thing. 
        if op == "clear":
            accumulator = 0
        elif op == "show":
            pass
        elif op == "add":
            accumulator += arg
        elif op == "sub":
            accumulator -= arg
        elif op == "mult":
            accumulator *= arg
        elif op == "div":
            if arg == 0:
                print( "Can't divide by 0.  Try again!" )
            else:
                accumulator /= arg
        elif op == "exit":
            break
        elif op == "help":
            print( helpMessage() )
        # This last case shouldn't occur, but better safe
        # than sorry.
        else:
            print( "Operator not recognized.")

        # Re-display the accumulator value.
        printAccumulator( accumulator )


flatCalc()


# FURTHER WORK:
#
# Think how you could modify this program to do each of the following:
# 
#   1. Add the neg command to negate the accumulator value.  
#   2. Accept negative as well as positive integer arguments. 
#   3. Make the driver interface more permissive to allow "mul" and "dv" in 
#         addition to "mult" and "div".  
#   4. Add sqrt and mod to the interfaces.  You'll need to import math.
#   5. Add a zeroary factorial function, that only operates if the accumulator
#         contains a positive integer.
#
