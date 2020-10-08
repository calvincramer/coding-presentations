#!/usr/bin/python3
import time

# Default Dict

# Normal use of dictionary
my_dict = {}
for n in range(1000):
    elm = n % 5
    if elm in my_dict:
        my_dict[elm] += 1
    else:
        my_dict[elm] = 1

print('Original:')
for k, v in my_dict.items():
    print(f'{k} -> {v}')

# TODO Use defaultdict to replace above 

# TODO Use defaultdict with a starting value from lambda

# TODO Use defaultdict with stating value from function


# Args
# TODO Normal way to apply arguments to function

# TODO apply to function with *args

# TODO function with *args

# TODO Kwargs normal way

# TODO kwargs with dictionary

# TODO use args and kwargs on a function

# TODO function with *args and **kwargs


# Comprehension
# TODO Normal looping method

# TODO comprehension syntax
# [<resulting element expression> for <elm> in <iterable> if <bool condition>]

# TODO list comprehension

# TODO dictionary comprehension

# TODO set comprehension

# TODO generator expression syntax
# even more like functional programming with lazy evaluation



# Speed ups
my_global = 0
def expensive(n):
    result = 0
    for _ in range(n):
        if my_global % 2 == 0:
            result += 1
        else:
            result -= 1
    return result


# start = time.time()
# print(expensive(10_000_000))
# print(time.time() - start)

# TODO use local variables instead

# Other function
def expensive3(n):
    arr = []
    for v in range(n):
        arr.append(v)
    return v

# start = time.time()
# expensive3(50_000_000)
# print(time.time() - start)

# TODO use function directly rather than access through dot
