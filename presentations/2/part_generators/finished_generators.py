#!/usr/bin/python3
import time
from typing import Iterator, Generator, Optional
print()


def generate_new_element(n: int) -> int:
    print(f'Generating a new number based on {n}')
    time.sleep(1 / 10)
    return n * 2

# TODO generator expression
gen = (generate_new_element(n) for n in range(5))
for elm in gen:
    print(elm)

# TODO same but use list
my_list = [generate_new_element(n) for n in range(5)]
for elm in my_list:
    print(elm)




# TODO generator function
def gen_func(num: int) -> Iterator[int]:
    while num > 0:
        print(f'Giving {num}')
        time.sleep(1/10)
        yield num
        num = num // 2

for n in gen_func(2**8):
    print(f'Got {n}')
    time.sleep(1/10)



# TODO call generator manually, to control iteration precisely
my_gen = (n for n in range(20))
res = []
while True:
    try:
        obj = my_gen.__next__()     # Dunder method
        obj_next = next(my_gen)     # alternative
    except StopIteration:
        print('End of gen!')
        break
    res.append( (obj, obj_next) )
print(res)



# TODO recursive generator function
class BTN:  # Binary tree node
    def __init__(self, val, l = None, r = None):
        self.val = val
        self.l = l
        self.r = r
root = BTN(10)
root.l = BTN(5)
root.r = BTN(20)
root.l.l = BTN(3)
root.l.r = BTN(7)
root.r.l = BTN(15)
root.r.r = BTN(25)

"""
         10
      5      20 
     3 7   15  25
"""

def infix_gen(node: Optional[BTN]):
    if node is None:
        return
    # Left
    yield from infix_gen(node.l)
    # Visit
    print(f'Giving {node.val}')
    yield node.val
    # Right
    yield from infix_gen(node.r)

for value in infix_gen(root):
    print(f'Got {value}')



# TODO speed / size comparison
import os
import gc
import psutil
import random
def get_mem_bytes() -> int:
    return psutil.Process(os.getpid()).memory_info().rss

SIZE = 1_000_000

# TODO list
gc.collect()
start_time_list = time.time()
start_mem_list = get_mem_bytes()
my_list = [n for n in range(1_000_000)]
sum_list = 0
for n in my_list:
    sum_list += n
end_mem_list = get_mem_bytes()
end_time_list = time.time()
print('List:')
print(f'Mem: {end_mem_list - start_mem_list}')
print(f'Sum: {sum_list}')
print(f'Time: {end_time_list - start_time_list}')

print()

# TODO generator
gc.collect()
start_time_gen = time.time()
start_mem_gen = get_mem_bytes()
my_gen = (n for n in range(1_000_000))
sum_gen = 0
for n in my_gen:
    sum_gen += n
end_mem_gen = get_mem_bytes()
end_time_gen = time.time()
print('Gen:')
print(f'Mem: {end_mem_gen - start_mem_gen}')
print(f'Sum: {sum_gen}')
print(f'Time: {end_time_gen - start_time_gen}')

# TODO exploration of when more memory requested
arr = []
last_mem = get_mem_bytes()
for i in range(100_000):
    arr.append(random.random())
    if i % 1000 == 0:
        cur_bytes = get_mem_bytes()
        print(cur_bytes - last_mem)
        last_mem = cur_bytes



# TODO generator makes infinite sequence generation simple
def fib() -> Iterator[int]:
    num_1 = 0
    yield num_1
    num_2 = 1
    yield num_2
    while True:
        num_1, num_2 = num_2, num_1 + num_2
        yield num_2

for n in fib():
    print(n)
    if n > 999_999_999_999:
        break


# TODO generator as a class by overriding some dunder functions
class GenClass:
    def __init__(self):
        self.n = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        self.n += 1
        if self.n % 2 == 0:
            return self.n
        else:
            return self.n, 'odd!'


obj = GenClass()
for value in obj:
    print(value)
    if type(value) is int and value > 100:
        break



# TODO sending values back
def stat_collector():
    _sum = 0
    _min = None
    _max = None
    _avg = None
    _count = 0
    while True:
        value = yield       # Wait for value to be sent
        _sum += value
        _count += 1
        _avg = _sum / _count
        if _min is None or value < _min:
            _min = value
        if _max is None or value > _max:
            _max = value
        print(f'sum: {_sum}, min: {_min}, max: {_max}, avg: {_avg:.2f}, count: {_count}')


stat_collector_gen = stat_collector()
next(stat_collector_gen)    # Need to 'prime' the generator
stat_collector_gen.send(5)
stat_collector_gen.send(10)
stat_collector_gen.send(-5)
stat_collector_gen.send(50)


# TODO sending values back AND forth
def stat_collector():
    _sum = 0
    _min = None
    _max = None
    _avg = None
    _count = 0
    while True:
        value = yield _sum, _min, _max, _avg, _count        # Wait for value to be sent
        _sum += value
        _count += 1
        _avg = _sum / _count
        if _min is None or value < _min:
            _min = value
        if _max is None or value > _max:
            _max = value

stat_collector_gen = stat_collector()
print(next(stat_collector_gen))    # Need to 'prime' the generator
print(stat_collector_gen.send(5))
print(stat_collector_gen.send(10))
print(stat_collector_gen.send(-5))
print(stat_collector_gen.send(50))




# TODO make CLI menu
import sys
def menu():
    top_level_menu = {}
    option1_menu = {}
    option2_menu = {}
    current_menu = top_level_menu

    def quit_func():
        print('Quitting!')
        exit()

    def print_current_menu():
        for k, v in current_menu.items():
            print(f'{v[0]}: [{k}]')
        print()

    top_level_menu['1'] = ['option1', option1_menu]
    top_level_menu['2'] = ['option2', option2_menu]
    top_level_menu['q'] = ['quit', quit_func]
    option1_menu['h'] = ['say hello', lambda: print('Hey there!')]
    option1_menu['b'] = ['back', top_level_menu]
    option2_menu['s'] = ['say something', lambda: print('Saying something else')]
    option2_menu['b'] = ['back', top_level_menu]

    while True:
        print_current_menu()
        print('input>> ', end='')
        inp = yield
        if inp not in current_menu:
            print('Bad selection, try again.')
            continue
        name, thing = current_menu[inp]
        if type(thing) is dict:
            current_menu = thing
            continue
        else:
            thing()
            print()

menu_gen = menu()
next(menu_gen)
while True:
    menu_gen.send(input())









print()
