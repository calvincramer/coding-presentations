# Topics to do for Python presentations

* pygdb gdb for python
	* debugging python not in ide

* eval() and exec() -> run python code from a string
	* modifiable code

* number types -> imaginary, Decimal(), Fraction()

* string types:
	* string (unicode)
	* bytes (ascii)
	* r, f other prefixes for string

* string encoding decoding

* '...' dot dot dot syntax

* functional programming
	* `lambda` functions
	* list, map, filter, accumulate, chain, reverse, sort, sorted, reduce
	* first-class functions
		* objects can be functions, functions can be passed, functions can return functions, etc
	* closure, `nonlocal`
	* partial application of functions
		* `from functools import partial`
	* currying -> `f(1)(2)(3)`
	* last statement in function implicit return

* walrus operator

* variable scope differences
	* can access variable outside of an if, for, while, try
	* can't access outside of a function
	* as opposed to curly braces languages that don't allow this
	* use `del` to delete variables

* `del` syntax
	* use to delete variables
	* delete items in list, dictionary?
	* what else?

* Counter()
* OrderedDict()
* collections module
	* deque
* Enum
	* unique, auto values
* dunder methods
	* `__str__`
	* `__repr__`
	* eq, ge, lt
	* getattribute, setattr, getattr
* logging
* context managers
* coroutines
* python project management
	* `__init__.py`
	* requirements.txt

* python 2 to 3 conversion
* testing
	* unittest
	* pytest
* simple standard library stuff:
	* calendar
	* os
	* os.path
	* shutil
	* urllib.request
	* re
	* timefile
	* zipfile
	* threading
	* multuprocessing
	* datetime
	* textwrap
	* html.parser
	* json
	* itertools.permutations
* useful libraries:
	* requests
	* tkinter
	* numpy
	* simpleaudio
	* opencv
	* imageio
	* matplotlib
	* flask
	* jinja2
	* csv
	* pillow
	* pandas
	* xml
	* lxml
	* BeautifulSoup
	* selenium
	* nltk
	* sqlite3
	* redis

* FASTER python
	* `perf_counter()`
	* timeit module
	* line_profiler
	* tracemalloc
	* look at python disassembly to optimize
	* attributes stored in dictionary, dictionary only 1/3 full waste a lot of memory
		* use `__slots__` to reduce memory
	* lru_cache `from functools import lru_cache`
	* Joblib
	* parallel computing
		* Amdahl's law
		* io bound -> threads
			* ThreadPoolExecutor
			* threads as classes
			* thread as function
			* locking
		* cpu bound
			* ProcessPoolExecutor
		* asyncio
		* multi thread
		* multi processor?
		* multi python interpreters?
		* GIL problem
	* numpy
	* numba
	* cython
	* pypy
	* c extensions
	* strace
	* bloom filter
	* python `async`, `await`, `async with`, `async for ... in ...`

* pyenv - separate package environments
	* http://bitbucket.wrs.com/projects/CT/repos/jivetwiki/browse/README-setup-pyenv.md

# Topics in process of creating presentation for:

## Presentation 4:
* generators
	* last vs. non-lazy computation
	* generator expressions
	* generator functions with yield
		* recursive generators with yield from
	* speed / size comparison
	* infinite data structures with generators
* need something else


# Topics done in presentations before

## Presentation 1: (Oct 16, 2020)
* `*args` and `**kwargs`
* defaultdict
* comprehension -> list, dict, set comprehension
* faster python:
	* access global variables is SLOWER than local variables
	* accessing functions through obj.func is slower than storing func as local variable (cost for function lookup on object)
* what's new in python 3.9

## Presentation 2: (planned Oct 30th, 2020)
* OOP stuff (kind of)
	* private attributes, hidden attributes, name mangling
	* Abstract classes `from abc import ABC, abstractmethod`
	* multiple inheritance and name conflicts, `__mro__`
	* interfaces through stateless abstract base classes and multiple inheritance
	* data class -> easier init functions (kind of like namedtuple)
		* immutable data class

## Presentation 3:
* string formatting
	* string append
	* %
	* format
	* f-strings
	* Template strings
* decorators
	* manually
	* simple
	* with decorator arguments
	* with function arguments
	* decorators as Classes (have internal state)
	* decorators as cache / memoization