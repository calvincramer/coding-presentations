#!/usr/bin/python3
import time
print()

# TODO decorator functionality manually

# def do_something(a, b):
#     print(f'do_something(): {a} + {b} = ', end='')
#     time.sleep(1/2)
#     print(a + b)
#     return a + b


# start = time.time()
# print(f'returned: {do_something(1, 2)}')
# print(f'Took {time.time() - start:.3f}s')

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

# print()
# do_something_better = timer(do_something)
# do_something_better(1, 2)

def counter(func):
    _count = 0
    def inner(*args, **kwargs):
        nonlocal _count
        ret = func(*args, **kwargs)
        _count += 1
        print(f'Times called: {_count}')
        return ret
    return inner

# do_something_even_better = counter(do_something_better)
# print()
# do_something_even_better(3, 4)
# print()
# do_something_even_better(5, 6)


def print_after(func):
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        print()
        return ret
    return inner


# TODO simple decorator
@print_after
@counter
@timer
def do_something2(a, b):
    print(f'do_something2(): {a} - {b} = ', end='')
    time.sleep(1/2)
    print(a - b)
    return a - b

# do_something2(1, 2)
# do_something2(3, 4)

# TODO multiple decorators equivalent syntax and ordering
f = print_after(counter(timer(do_something2)))
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

    
# jeff = Person(age=20)
# print(f"Jeff's age: {jeff.get_age()}")
# jeff.set_age(age=-100)
# print(f"Jeff's age: {jeff.get_age()}")





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

# for n in range(50):
#     print_n(n)
        







# TODO decorators as classes

# TODO example decorator as cache / memoization











print()