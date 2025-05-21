# 1. Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
# in this case we can use Nested Functions (Inner Functions) Functions defined inside another function.
# A function defined inside another function.

def example_one ():
    print ("This is the example number one")
    example_two ()

def example_two (): 
    print("This is the example two")

example_one()

#here I can call the first function, which will also call the second one
    





