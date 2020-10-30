#!/usr/bin/python3
import time
import math
from typing import List, Dict, Optional
print()


# TODO Public, private, hidden
class Foo:
    def __init__(self, pub: int, private: int, hidden: int):
        # TODO public attribute
        self.pub = pub
        # TODO private attribute
############################################# ASK WHO KNOWS HOW TO DO PRIVATE VARIABES #############################################
        self._pri = private
        # TODO hidden attribute
        self.__hidden = hidden

    def get_public(self) -> int:
        return self.pub
    def get_private(self) -> int:
        return self._pri
    def get_hidden(self) -> int:
        return self.__hidden

# TODO Access attributes
foo_obj = Foo(5, 10, 15)

print(f'public: {foo_obj.get_public()}')
print(f'public: {foo_obj.pub}')

print(f'private: {foo_obj.get_private()}')
print(f'private: {foo_obj._pri}')

print(f'hidden: {foo_obj.get_hidden()}')
############################################# ASK WHAT DO YOU THINK WILL HAPPEN #############################################
try:
    print(f'hidden: {foo_obj.__hidden}')          # Protection!
except AttributeError as e:
    print(f'ERROR: {e}')
print(f'hidden: {foo_obj._Foo__hidden}')    # But still accessible through mangled name





# TODO Abstract class with pass or raise NotImplementedError
############################################# ASK WHAT IS AN ABSTRACT CLASS #############################################
class Abstract_Faker:
    def __init__(self, state):
        self.state = state
    def __str__(self):
        return str(self.state)

    def abstract_1(self):
        # The "do nothing" silent error waiting to happen
        pass

    def abstract_raise(self):
        raise NotImplementedError("Don't call me or you'll be sorry!")

    def abstract_warning(self):
        print('Make sure you implement this method!')

# TODO instantiate "abstract" class
abstract_faker_obj = Abstract_Faker(154)
print(abstract_faker_obj)
abstract_faker_obj.abstract_1()
abstract_faker_obj.abstract_warning()
try:
    abstract_faker_obj.abstract_raise()
except:
    print('oops! The program will crash if not caught...')

# TODO override "abstract" class
class Abstract_Faker_Concrete(Abstract_Faker):
    def abstract_1(self):
        print('abstract_1 work')
    def abstract_raise(self):
        print('abstract_raise work')
    def abstract_warning(self):
        print('abstract_warning work')

# TODO is it smart to do it this way?:
# using fake abstract class OK as long as all abstract methods overridden, but error prone.

# TODO use concrete class
abstract_faker_concrete_obj = Abstract_Faker_Concrete(404)
abstract_faker_concrete_obj.abstract_1()
abstract_faker_concrete_obj.abstract_raise()
abstract_faker_concrete_obj.abstract_warning()





# TODO Abstract class with ABC
from abc import ABC, abstractmethod
class Bar(ABC):
    # 1. TODO default abstract instance method
    @abstractmethod
    def speak(self) -> str:
        ...
    # 2. TODO default abstract instance method WITH an implementation
    @abstractmethod
    def convert(self, num: int) -> int:
        return num // 10
    # 3. TODO abstract class method (useful for Factory patterns)
    @classmethod
    @abstractmethod
    def factory(cls, num):
        ...
    # 4. TODO abstract static method (useful for simple utility functions)
    @staticmethod
    @abstractmethod
    def run(input: int) -> int:
        ...
    # 5. TODO abstract property (getter)
    @property
    @abstractmethod
    def num_legs(self):
        ...
    # 6. TODO abstract property setter
    @num_legs.setter
    @abstractmethod
    def num_legs(self, value):
        ...

# TODO extend abstract class with concrete class
class Bar_Concrete(Bar):
    # TODO first try to not override abstract method, see that it enforces
############################################# ASK WHAT DO YOU THINK WILL HAPPEN #############################################
    # pass

    # 1. TODO implement default abstract instance method
    def speak(self) -> str:
        return 'I am concrete'
    # 2. TODO implement default abstract instance method WITH an implementation
    def convert(self, num: int) -> int:
        if num < 0:
            # Special case, use super implementation
            return super().convert(num)
        return int(''.join(str(d) for i, d in enumerate(str(num)) if i % 2 == 0))
    # 3. TODO implement abstract class method
    @classmethod
    def factory(cls, num):
        obj = cls()
        obj.value = num
        return obj
    # 4. TODO implement abstract static method
    @staticmethod
    def run(ms: int) -> int:
        seconds = ms / 1_000
        print(f'Running for {seconds:.2f} seconds')
        time.sleep(seconds)
    # 5. TODO implement abstract properties
    @property
    def num_legs(self):
        if not hasattr(self, '_num_legs'):
            self._num_legs = 1_000
        return self._num_legs  # I'm a millipede
    # 6. TODO abstract property setter
    @num_legs.setter
    def num_legs(self, value):
        if value < 1_000:
            print('Warning, I am supposed to be a millipede, I need more legs!')
        self._num_legs = value     # Doesn't cause infinite recursion

# TODO try to to instantiate abstract class
try:
    bar_obj = Bar()        # Can't instantiate
except TypeError as e:
    print(e)

bar_conc_obj = Bar_Concrete()
print(f'speak(): {bar_conc_obj.speak()}')
print(f'convert(): {bar_conc_obj.convert(123456789)}')
print(f'convert(): {bar_conc_obj.convert(-100)}')
new_obj = bar_conc_obj.factory(1234)
print(f'value= {new_obj.value}')
bar_conc_obj.run(1_500)

print(f'num legs: {bar_conc_obj.num_legs}')
bar_conc_obj.num_legs = 900
print(f'num legs: {bar_conc_obj.num_legs}')








# TODO Multiple inheritance
class Base1:
    def f1(self):
        return 'Base1 f1'
    def f_base1(self):
        return 'Base1 f_base1'

class Base2:
    def f1(self):
        return 'Base2 f1'
    def f_base2(self):
        return 'Base2 f_base2'

class Child(Base1, Base2):
    # TODO: Add this after
    def call_test(self):
        print('Call test')
        print(super().f1())
        print(super().f_base1())
        print(super().f_base2())
        # Call specific parents
        print(Base1.f1(self))
        print(Base2.f1(self))


# TODO Show multiple inheritance conflicts
child = Child()
print(f'f1 -> {child.f1()}')
print(f'f_base1 -> {child.f_base1()}')
print(f'f_base2 -> {child.f_base2()}')
child.call_test()
# TODO Swap order of multiple inheritance to change MRO


# TODO show __mro__
print(Child.__mro__)
print(Child.mro())
# TODO explain: MRO maintains that parents always come before children







# TODO Interfaces through stateless ABC and multiple inheritance
############################################# ASK WHAT IS AN INTERFACE #############################################
class HasArea(ABC):
    @property
    @abstractmethod
    def area(self) -> float:
        ...

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        ...

class Shape:
    # More stuff here
    ...

class Square(Shape, HasArea, Drawable):
    def __init__(self, length):
        self._side_length = length
    @property
    def area(self) -> float:
        return self._side_length ** 2

    def draw(self):
        print()
        for _ in range(self._side_length):
            print('.' * self._side_length)
        print()

class Triangle(Shape, HasArea, Drawable):
    def __init__(self, base, height):
        self._base = base
        self._height = height
    @property
    def area(self) -> float:
        return self._base * self._height / 2.0

    def draw(self):
        for row in range(1, self._height + 1):
            tri_chars = int(float(row) / self._height * self._base)
            tri_chars = '.' * tri_chars
############################################# ASK WHAT IS THE AREA OF A TRIANGLE #############################################
            prepend_chars = ' ' * ((self._base - len(tri_chars)) // 2)
            print(prepend_chars + tri_chars)


sq = Square(5)
print(f'area square: {sq.area}')
sq.draw()

tri = Triangle(11, 6)
print(f'area triangle: {tri.area}')
tri.draw()






# TODO dataclass
# TODO normal way
class Big:
    def __init__(self, a: int, b: str, c: List[str], d: Dict[int, str], e: float, f: Optional[str], g: int, h: int = 0, i: int = 1, j: int = 2):
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self._e = e
        self._f = f
        self._g = g
        self._h = h
        self._i = i
        self._j = j

    def do_something(self):
        print(self.__dict__)


big = Big(1, 'asdf', [1, 2, 3, 4], {1: 'one'}, 3.1415, None, 2)
big.do_something()

# TODO dataclass way
from dataclasses import dataclass, field

def make():
    return ['asdf', 1234, 'blah blah']

@dataclass
class BigSmart:
    a: int
    b: str
    c: List[str]
    d: Dict[int, str]
    e: float
    f: Optional[str]
    g: int
    h: int = 0
    i: int = 0
    j: int = 0
    complex_var: List = field(default_factory=make)

    def __post_init__(self):
        self._blah = self.a + self.e

    def do_something(self):
        print(self.__dict__)

big_smart = BigSmart(1, 'asdf', [1, 2, 3, 4], {1: 'one'}, 3.1415, None, 2)
big_smart.do_something()
# TODO remember, type is not enforced





# TODO immutable dataclass
@dataclass(frozen=True)
class BankAccount:
    money: int

account = BankAccount(100)
print(f'I have {account.money} dollars')
try:
    account.money = 1_000_000
except Exception as e:
    print(e)
print(f'Now I have {account.money} dollars')














print()