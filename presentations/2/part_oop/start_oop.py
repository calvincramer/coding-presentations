#!/usr/bin/python3
import time
import math
from typing import List, Dict, Optional
print()


# TODO Public, private, hidden
class Foo:
    def __init__(self, pub, pri, hidden):
        self.pub = pub
        self._pri = pri
        self.__hidden = hidden

    def get_hidden(self):
        return self.__hidden

# TODO Access attributes
# foo_obj = Foo(5, 10, 15)
# print(foo_obj.pub)
# print(foo_obj._pri)
# try:
#     print(foo_obj.__hidden)
# except:
#     print("can't access hidden")
# print(foo_obj.get_hidden())
# print(foo_obj._Foo__hidden)
# help(Foo)












# TODO Abstract class with pass or raise NotImplementedError
class Abstract_Faker:
    def __init__(self, state):
        self.state = state
    def __str__(self):
        return str(self.state)

    def abstract_1(self):
        # pass
        ...

    def abstract_2(self):
        raise NotImplementedError("Oops!")

    def abstract_3(self):
        print("I'm not implemented")




# TODO instantiate "abstract" class
# abstract_faker_obj = Abstract_Faker(42)
# print(abstract_faker_obj)
# # abstract_faker_obj.abstract_2()
# abstract_faker_obj.abstract_3()


# TODO override "abstract" class
from abc import ABC, abstractmethod

class Bar(ABC):
    def __init__(self, numlegs):
        # self._num_legs = numlegs
        pass

    @abstractmethod
    def speak(self) -> str:
        ...
    @abstractmethod
    def convert(self, num):
        return num // 10
    @staticmethod
    def foo():
        pass
    @property
    @abstractmethod
    def num_legs(self):
        ...

    @num_legs.setter
    @abstractmethod
    def num_legs(self):
        ...


# bar_obj = Bar()



# TODO is it smart to do it this way?: 

# TODO use concrete class
class Bar_Concrete(Bar):
    def speak(self) -> str:
        return "I'm concrete"
    def convert(self, num):
        if num < 0:
            return super().convert(num)
        return num * -1
    @property
    def num_legs(self):
        if not hasattr(self, '_num_legs'):
            self._num_legs = 1_000
        return self._num_legs
    @num_legs.setter
    def num_legs(self, value):
        if value < 1_000:
            print('Warning! Less than 1000 legs')
        self._num_legs = value
    

# bar_conc_obj = Bar_Concrete()
# print(bar_conc_obj.speak())
# print(bar_conc_obj.convert(-50))
# print(bar_conc_obj.num_legs)

# bar_conc_obj.num_legs = 999
# print(bar_conc_obj.num_legs)








# TODO Abstract class with ABC

# TODO extend abstract class with concrete class
        
# TODO try to to instantiate abstract class













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
    # def f1(self):
    #     ...

    def call_test(self):
        print(super().f1())
        print(Base1.f1(self))
        print(Base2.f1(self))
    pass

# child = Child()
# print(f'f1 -> {child.f1()}')
# print(f'f_base1 -> {child.f_base1()}')
# print(f'f_base2 -> {child.f_base2()}')
# child.call_test()

# TODO Show multiple inheritance conflicts

# TODO Swap order of multiple inheritance to change MRO

# TODO show __mro__ "method resolution order"
# print(f'mro = {Child.__mro__}')
# print(f'mro = {Child.mro()}')

# TODO explain: MRO maintains that parents always come before children










# TODO Interfaces through stateless ABC and multiple inheritance
# INTERFACE
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
    ...

class Square(Shape, HasArea, Drawable):
    def __init__(self, length):
        self._side_length = length

    @property
    def area(self) -> float:
        return self._side_length ** 2

    def draw(self):
        print()
        for _ in range(int(self._side_length)):
            print('.' * int(self._side_length))
        print()

# sq = Square(4.5)
# print(f'square area: {sq.area}')
# sq.draw()







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

    def __post_init__(self):
        self._blah = str(self.a) + self.b

    def do_something(self):
        print(self.__dict__)

big_smart = BigSmart('hello', 'asdf', [1, 2, 3, 4], {1: 'one'}, 3.1415, None, 2)
big_smart.do_something()
big_smart.a = 'something else'
big_smart.do_something()

# TODO remember, type is not enforced









# TODO immutable dataclass
@dataclass(frozen=True)
class BankAccount:
    money: int

account = BankAccount(100_000_000)
print(account.money)
account.money *= 2
print(account.money)













print()