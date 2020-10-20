#!/usr/bin/python

# TODO Simple class public attributes
class Foo:
    def __init__(self, num: int):
        self.num = num
    def get_num(self) -> int:
        return self.num

# TODO Use simple class
foo_obj = Foo(5)
print(foo_obj.get_num())
print(foo_obj.num)



# TODO Private attribute class
class FooPrivate:
    def __init__(self, num: int):
        self._num = num             # By convention, no protection (other than static checkers)
    def get_num(self) -> int:
        return self._num

# TODO Use private attribute class
foo_p_obj = FooPrivate(10)
print(foo_p_obj.get_num())
print(foo_p_obj._num)



# TODO Hidden attribute class
class FooHidden:
    def __init__(self, num: int):
        self.__num = num             # By convention, no protection (other than static checkers)
    def get_num(self) -> int:
        return self.__num


# TODO Use hidden attribute class
foo_h_obj = FooHidden(15)
print(foo_h_obj.get_num())
try:
    print(foo_h_obj.__num)          # Protection!
except AttributeError as e:
    print(e)
print(foo_h_obj._FooHidden__num)    # But still accessible through mangled name





# TODO Abstract class with pass or raise NotImplementedError
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
# TODO explain using fake abstract class OK as long as all abstract methods overridden, but error prone.
# TODO use concrete class
abstract_faker_concrete_obj = Abstract_Faker_Concrete(404)
abstract_faker_concrete_obj.abstract_1()
abstract_faker_concrete_obj.abstract_raise()
abstract_faker_concrete_obj.abstract_warning()




# TODO Abstract class with ABC
from abc import ABC, abstractmethod
class Bar(ABC):
    def __init__(self, name):
        self.__name = name
    def __str__(self):
        return self.__name + "\t" + self.speak()
    @abstractmethod
    def speak(self) -> str:
        ...
    # TODO MORE METHODS FROM ABC like staticmethod, classmethod, property

    

# TODO try to to instantiate abstract class
try:
    bar_obj = Bar('should not work')        # Can't instantiate
    print(bar_obj)
except TypeError as e:
    print(e)
# TODO extend abstract class with concrete class
class Bar_Concrete(Bar):
    # TODO first try to not override abstract method, see that it enforces 
    # pass
    # TODO provide implementation
    def speak(self) -> str:
        return 'I am concrete'

bar_conc_obj = Bar_Concrete('concrete')
print(bar_conc_obj)




# TODO Multiple inheritance


# TODO Multiple inheritance conflicts and __mro__



# TODO Interfaces through stateless ABC and multiple inheritance




# TODO dataclass
# TODO immutable dataclass