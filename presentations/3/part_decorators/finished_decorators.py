#!/usr/bin/python3
import time
from typing import Tuple

print()



# TODO functions are first class objects
# TODO You can pass functions as arugments
def run(function):
    print(f'I am now going to call {function.__name__}()')
    function()

def say_hi():
    print('Hey there!')

run(say_hi)

# TODO You can assign functions as variables
def div_3(n):
    return n // 3
def div_2(n):
    return n // 2

num = 2**8 * 3**5
for _ in range(14):
    print(num)
    if num % 2 == 0:
        f = div_2
    else:
        f = div_3
    num = f(num)

# TODO You can have inner functions (not apart of "first class" definition)
def main_function():
    def is_prime(n):
        if n <= 1:
            return False
        elif n == 2: 
            return True
        return all(n % d != 0 for d in range(2, int(n ** 0.5) + 1))
    for num in range(0, 50):
        if is_prime(num):
            print(num)

main_function()

# TODO You can return functions from functions
def choose(num):
    def choice_1():
        print('choice1!')
    def choice_2():
        print('choice2!')
    return choice_1 if num % 2 == 0 else choice_2

f = choose(10)
f()
choose(11)()

# TODO later maybe? Partial application of function and currying











# TODO decorator functionality manually
# TODO function, decorate outside function when called
def do_something(a, b):
    print(f'do_something(): {a} + {b} = ', end='')
    time.sleep(1/2)
    print(a + b)
    return a + b


start = time.time()
print(f'returned: {do_something(1, 2)}')
print(f'Took {time.time() - start:.3f}s')

# TODO compose function
def timer(func):
    def inner(*args, **kwargs):
        # print('Before')
        start = time.time()
        ret = func(*args, **kwargs)
        elapsed = time.time() - start
        # print('After')
        print(f'Timer took: {elapsed:.3f}s')
        return ret
    return inner

print()
do_something_better = timer(do_something)
do_something_better(1, 2)

# TODO compose function again
def counter(func):
    _count = 0
    def inner(*args, **kwargs):
        nonlocal _count
        ret = func(*args, **kwargs)
        _count += 1
        print(f'Times called: {_count}')
        return ret
    return inner

do_something_even_better = counter(do_something_better)
print()
do_something_even_better(3, 4)
print()
do_something_even_better(5, 6)






# TODO use decorator syntactical sugar
def print_after(func):
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        print()
        return ret
    return inner

@print_after
@counter
@timer
def do_something2(a, b):
    print(f'do_something2(): {a} - {b} = ', end='')
    time.sleep(1/2)
    print(a - b)
    return a - b

do_something2(1, 2)
do_something2(3, 4)











# TODO multiple decorators equivalent syntax and ordering
def do_something3(a, b):
    print(f'do_something3(): {a} - {b} = ', end='')
    time.sleep(1/2)
    print(a - b)
    return a - b

f = print_after(counter(timer(do_something3)))
f(1, 2)
f(3, 4)











# TODO decorate class methods
import random
random.seed()

def obfuscate(func):
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        if type(ret) in [int, float]:
            diff = abs(ret) / 10
            ret += random.randrange(-diff, diff)
        return ret
    return inner

class Person:

    def __init__(self, age):
        self._age = max(0, age)
    
    @obfuscate
    def get_age(self):
        return self._age

    def check_age_arg(func):
        def inner(*args, **kwargs):
            if kwargs['age'] < 0:
                raise ValueError('age needs to be positive')
            return func(*args, **kwargs)
        return inner
    
    def flip_age(func):
        def inner(self, *args, **kwargs):
            ret = func(self, *args, **kwargs)
            self._age *= -1
            return ret
        return inner
    
    @flip_age
    # @check_age_arg
    def set_age(self, *, age):
        self._age = age

    
jeff = Person(age=20)
print(f"Jeff's age: {jeff.get_age()}")
jeff.set_age(age=-100)
print(f"Jeff's age: {jeff.get_age()}")











# TODO decorator with arguments
def print_every(n, message):
    def print_every_decorator(func):
        _count = 0
        def inner(*args, **kwargs):
            nonlocal _count
            ret = func(*args, **kwargs)
            _count += 1
            if _count >= n:
                _count = 0
                print(message)
            return ret
        return inner
    return print_every_decorator

@print_every(10, 'Called 10 times')
@print_every(5, 'Called 5 times')
def print_n(n):
    print(n)

for n in range(50):
    print_n(n)
 










# TODO decorators as classes (more natual internal decorator state)
# TODO example decorator as cache / memoization
class Memo:
    def __init__(self, function):
        self._func = function
        self._memo = {}

    @staticmethod
    def _hash(*args, **kwargs) -> Tuple:
        return hash(tuple([*args, *kwargs.values()]))

    def __call__(self, *args, **kwargs):
        # In memo?
        arg_hash = Memo._hash(*args, **kwargs)
        if arg_hash in self._memo:
            print('Using cached value')
            return self._memo[arg_hash]
        # Compute
        val = self._func(*args, **kwargs)
        # Place in memo
        self._memo[arg_hash] = val
        return val

@timer
@Memo
def sqrt(a: float) -> float:
    print(f'computing sqrt({a}) first time (very slow)')
    time.sleep(1/2)
    return a ** 0.5


print(f'sqrt(5) = {sqrt(5)}\n')
print(f'sqrt(5) = {sqrt(5)}\n')
print(f'sqrt(5) = {sqrt(5)}\n')









print()