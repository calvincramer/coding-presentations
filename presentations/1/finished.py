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
from collections import defaultdict

my_dict = defaultdict(int)
for n in range(1000):
    my_dict[n % 5] += 1

print('Default dict:')
for k, v in my_dict.items():
    print(f'{k} -> {v}')

# TODO Use defaultdict with a starting value from lambda
my_dict = defaultdict(lambda: 5)
my_dict[1] += 1

for k, v in my_dict.items():
    print(f'{k} -> {v}')

# TODO Use defaultdict with stating value from function
def complex_func():
    return [1, 2, 3, 4]
my_dict = defaultdict(complex_func)
my_dict['test'].append(5)
for k, v in my_dict.items():
    print(f'{k} -> {v}')



# Args
# TODO Normal way to apply arguments to function
def f(a, b, c, d):
    print('f:', a, b, c, d)

my_args = [1, 2, 3, 4]
f(my_args[0], my_args[1], my_args[2], my_args[3])

# TODO apply to function with *args
f(*my_args)

# TODO function with *args
def g(a, *args):
    print('g:', a, end='')
    for arg in args:
        print(arg, end='')
    print()

g(1, 2, 3, 4)


# TODO Kwargs normal way
def foo(a=5, b=6, c=7, d=8):
    print('foo:', a, b, c, d)

my_kwargs = {'a': 100, 'b': 101, 'c': 102, 'd': 103}
foo(a=my_kwargs['a'], b=my_kwargs['b'], c=my_kwargs['c'], d=my_kwargs['d'])

# TODO kwargs with dictionary
foo(**my_kwargs)

# TODO use args and kwargs on a function
def bar(a, b, c, d, e=6, f=7):
    print('bar:', a, b, c, d, e, f)

my_kwargs = {'e': 10, 'f': 11}
bar(*my_args, **my_kwargs)

# TODO function with *args and **kwargs
def baz(normal_arg, *args, **kwargs):
    print('baz:', normal_arg)
    for arg in args:
        print('baz:', arg)
    for kw, val in kwargs.items():
        print('baz:', kw, val)
    if 'discount' in kwargs:
        print('found discount argument')

baz('normal', 1, 2, 3, 4, discount=5, something_else='blah')


# Comprehension
# TODO Normal looping method
my_list = list(range(16))
new_list = []
for i in range(len(my_list)):
    if my_list[i] % 5 == 0:
        new_list.append(my_list[i] + 4)

print(my_list)
print(new_list)

# TODO comprehension syntax
# [<resulting element expression> for <elm> in <iterable> if <bool condition>]

# TODO list comprehension
new_list = [n + 4 for n in my_list if n % 5 == 0]

# TODO dictionary comprehension
orig_dict = {1: 2, 2: 4, 3: 6, 4: 8}
new_dict = {k: v for (k, v) in orig_dict.items() if k % 2 == 0}
print(orig_dict)
print(new_dict)

# TODO set comprehension
orig_set = {1, 2, 3, 4, 5, 6}
new_set = {str(v) + ' blah' for v in orig_set if v % 2 == 0}
print(orig_set)
print(new_set)

new_set = set()
for v in orig_set:
    if v % 2 == 0:
        new_set.add(str(v) + ' blah')
print(new_set)

# TODO generator expression syntax
# even more like functional programming with lazy evaluation
my_list = [x for x in range(10)]
print(my_list)

my_gen = (x for x in range(10))
print(my_gen)
for v in my_gen:
    print(v)
print(list(my_gen)) # Values only collected once.

my_gen = (x for x in range(10))
print(list(my_gen))



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


start = time.time()
print(expensive(10_000_000))
print(time.time() - start)

# TODO use local variables instead
def expensive2(n):
    result = 0
    my_local = 0
    for _ in range(n):
        if my_local % 2 == 0:
            result += 1
        else:
            result -= 1
    return result

start = time.time()
print(expensive2(10_000_000))
print(time.time() - start)

# Other function
def expensive3(n):
    arr = []
    for v in range(n):
        arr.append(v)
    return v

start = time.time()
expensive3(50_000_000)
print(time.time() - start)

# TODO use function directly rather than access through dot
def expensive4(n):
    arr = []
    f = arr.append
    for v in range(n):
        f(v)
    return v

start = time.time()
expensive4(50_000_000)
print(time.time() - start)







# EXTRA
# Python 3.9 features
"""
1. special dictionary syntax for merging and updating
    dict_a | dict_b  (merge),  dict_a |= dict_b (update)

2. string functions to remove prefixes and suffixes

3. type hinting no longer needs special types from the typing module
    * previously
        from typing import List
        def foo(a: List[int]) -> List[float]:
            pass

    * python 3.9:
        def foo(a: list[int]) -> list[float]:
            pass

4. PEG parser rather than LL(1) parser (Cpython specific)
    * LL(1) parser is top-down left to right parser, one-token of lookahead
        * "Left-to-right, leftmost derivation"
        * doesn't allow for two rules to start with the same token:
            * rule1: token1 token2
            * rule2: token1 token3
        * doesn't allow for left recursive rules
            * rule: rule token
    * PEG (Parsing Expression Grammar)
        * main difference with LL(1)
        * different than context-free grammar
        * usually implemented as recursive descent parser
        * rule: A | B
            * PEG: try to run with A first, if it fails, try B (order of A and B matters now)
            * LL(1): always knows which choice to take, since A and B cannot have the same first tokens
    * currently there are some hacky things python does that stretch the limits of LL parsers
    * exploiting the benefits of PEG parser will be seen in python 3.10



"""