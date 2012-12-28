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

from Stack import *
import string


######################################################################
#                                                                    #
#                        Evaluation Functions                        #
#                                                                    #
######################################################################


def infixToPostfix(infixexpr):
    """Input may contain positive integer constants and the following operators:
    + (plus), - (minus), * (times), and parentheses. Use spaces to
    separate tokens in your input. That is, you should input "( 12 + 7 ) * 3"
    rather than "(12+7)*3"."""

    # First set up a dictionary mapping symbols to
    # precedence.
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    prec[""]  = 0
    
    # Split the input into tokens.
    tokenList = infixexpr.split()
    
    # We’ll need a stack and an output stream.
    opStack = Stack()
    outputList = []

    for token in tokenList:
        # Is token a number?
        if token.isdigit():
            outputList.append(token)
        elif token.isalpha():
            print("Variables are not allowed")
            return None
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            if opStack.isEmpty():
                print("Ill-formed expression")
                return None
            else:
                topToken = opStack.pop()
                while topToken != "(":
                    outputList.append(topToken)
                    if opStack.isEmpty():
                        print("Ill-formed expression")
                        return None
                    else:
                        topToken = opStack.pop()
        elif token in ('+', '-', '/', '*', '('):
            while (not opStack.isEmpty()) and \
            (prec[opStack.peek()] >= prec[token]):
                if opStack.isEmpty():
                    print("Ill-formed expression")
                    return None
                else:
                    outputList.append(opStack.pop())
                            
            opStack.push(token)
        else:
            print("Ill-formed expression")
            return None
    while not opStack.isEmpty():
        outputList.append(opStack.pop())
    return " ".join(outputList)




def postEval(symbolString):
    """Given a postfix expression, evaluate it"""
    if symbolString == None:
        return None
    
    tokens = symbolString.split()
    stack = Stack()
    
    for token in tokens:
        # Is the token an integer?
        if token.isdigit():
            stack.push(int(token))
        # otherwise, it must be an operator
        elif stack.__len__() <= 1:
            print("Ill-formed expression")
            return None
        else:
            arg1 = stack.pop()
            arg2 = stack.pop()
            # Evaluate operator expressions (handles exceptions)
            val = applyOp(token, arg1, arg2)
            stack.push(val)

    if not stack.__len__() == 1:
        print("Ill-formed expression")
        return None
        
    return stack.pop()



def applyOp(token, arg1, arg2):
    """Calculate the result of an operator on it's arguments"""
    if token == "-":
        return arg2 - arg1
    elif token == "+":
        return arg2 + arg1
    elif token == "*":
        return arg2 * arg1
    elif token == "/":
        if arg1 == 0:
            print("Cannot divide by Zero, please alter the expression")
            return None
        else:
            return arg2 / arg1
    else:
        print("""Invalid operator, please check your expression only includes
        only basic operators '+,-,*,/'""")
        return None



######################################################################
#                                                                    #
#                    Driver Evaluation Functions                     #
#                                                                    #
######################################################################

def runpostfix(symbolString):
    """Run the postfix expression evaluator"""

    #Evaluate Postfix Expression
    answer = postEval(symbolString)

    #something went wrong, report true to allow driver to continue
    if answer == None:
        return True
    else:
        print( "The answer is: ", answer )


def runinfix(symbolString):
    """Run the infix expression evaluator"""

    #Change To Postfix
    postfix = infixToPostfix(symbolString)

    #something went wrong, report true to allow driver to continue
    if postfix == None:
        return True
    
    #Evaluate Postfix Expression
    answer = postEval(postfix)

    #something went wrong, report true to allow driver to continue
    if answer == None:
        return True
    
    else:
        print( "The infix answer is: ", answer )   


######################################################################
#                                                                    #
#                             Main Driver                            #
#                                                                    #
######################################################################

def calculator():
    """   This is a simple calculator.

   Enter expressions in infix (default) or postfix notation.

   Type 'infix' or 'postfix' to toggle the mode.
   Type 'stop' to exit.

   - Tokens in your expression must be separated by spaces.
   - Expressions can involve postive integers and any of +, *, -.
   - Infix expressions can use parentheses to disambiguate."""


    while True:
        # Prompt for an infix expression.
        symbolString = input("\nEnter an infix expression: ")

        # Exit if the input string is empty or contains a stop word.
        if ( symbolString == "" ): break
        if ( symbolString == ("stop" or "Stop" or "STOP") ): break

        # Allow direct to Postfix 
        if ( symbolString == "postfix" ):

            #allow user to say in postfix, until break or type 'infix'
            while True:
            
                #ask for a postfix expression
                symbolString = input("\nEnter an postfix expression: ")

                #allow escape back to infix
                if ( symbolString == "infix" ):
                    #runinfix expression evaluator
                    break
            
                #run the postfix evaluator functions
                else:
                    runpostfix(symbolString)
                
        elif ( symbolString == "infix" ):        
        #return to top of loop (stupid catcher)
            continue

        #runinfix expression evaluator
        else:
            runinfix(symbolString)
        

print("""   This is a simple calculator.

   Enter expressions in infix (default) or postfix notation.

   Type 'infix' or 'postfix' to toggle the mode.
   Type 'stop' to exit.

   - Tokens in your expression must be separated by spaces.
   - Expressions can involve postive integers and any of +, *, -.
   - Infix expressions can use parentheses to disambiguate.""")


calculator()
