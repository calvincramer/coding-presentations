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
an individual object (or function), dynamically, without affecting the
behavior of other objects from the same class
"""


# TODO decorator functionality manually

# TODO function, decorate outside function when called


# TODO wrap functionality around existing function


# TODO Implement kind-of decorator by passing function and arguments at same time




# TODO compose function again, because why not



# TODO use decorator syntactical sugar




# TODO multiple decorators equivalent syntax and ordering





# TODO decorate class methods



# TODO can also apply decorators to class itself
# no example...







# TODO decorator with arguments









# TODO decorators as classes (more natual internal decorator state)
# TODO example decorator as cache / memoization



def sqrt(a: float) -> float:
    print(f'computing sqrt({a}) first time (very slow)')
    time.sleep(1/2)
    return a ** 0.5

print(f'sqrt(5) = {sqrt(5)}\n')
print(f'sqrt(5) = {sqrt(5)}\n')
print(f'sqrt(5) = {sqrt(5)}\n')







print()