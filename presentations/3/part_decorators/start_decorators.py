#!/usr/bin/python3
import time
from typing import Tuple

print()



# TODO functions are first class objects

# TODO You can pass functions as arugments



# TODO You can assign functions as variables, and call variables that are functions




# TODO You can have inner functions




# TODO You can return functions from functions




# TODO closures and inner functions




# TODO later maybe? Partial application of function and currying








# TODO what is a decorator?
"""
The decorator design pattern allows behavior to be added to 
an individual object, dynamically, without affecting the 
behavior of other objects from the same class
"""


# TODO decorator functionality manually

# TODO function, decorate outside function when called
def do_something(a, b):
    print(f'do_something(): {a} + {b} = ', end='')
    time.sleep(1/2)
    print(a + b)
    return a + b




# TODO wrap functionality around existing function



# TODO compose function again, because why not



# TODO use decorator syntactical sugar




# TODO multiple decorators equivalent syntax and ordering






# TODO decorate class methods









# TODO decorator with arguments

# def print_n(n):
#     print(n)

# for n in range(50):
#     print_n(n)
 










# TODO decorators as classes (more natual internal decorator state)
# TODO example decorator as cache / memoization









print()