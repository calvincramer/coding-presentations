# Topics to do for Python presentations

* number types -> imaginary, Decimal(), Fraction()
* string vs. bytes
* string encoding decoding
* string formatting
	* append
	* %
	* format
	* f-strings
* functional programming
	* `lambda` functions
	* list, map, filter, accumulate, chain, reverse, sort, sorted, reduce
	* first-class functions
		* objects can be functions, functions can be passed, functions can return functions, etc
	* closure, `nonlocal`
	* partial application of functions
		* `from functools import partial`
	* currying -> `f(1)(2)(3)`



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
* generators
* decorators
	* manually
	* simple
	* with decorator arguments
	* with function arguments
	* decorators as Classes (have internal state)
	* decorators as cache / memoization
* context managers
* coroutines
* python project management
	* `__init__.py`
	* requirements.txt
* OOP stuff (kind of)
	* private attributes, hidden attributes, name mangling
	* Abstract classes `from abc import ABC, abstractmethod`
	* multiple inheritance and name conflicts, `__mro__`
	* interfaces through stateless abstract base classes and multiple inheritance
	* data class -> easier init functions (kind of like namedtuple)
		* immutable data class
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
* useful libraries:
	* requests
	* itertools.permutations
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
	* numpy
	* numba
	* cython
	* pypy
	* c extensions
	* strace
	* bloom filter
	* python `async`, `await`, `async with`, `async for ... in ...`



# Topics in process of creating presentation for

## Presentation 1:
* `*args` and `**kwargs`
* defaultdict
* comprehension -> list, dict, set comprehension
* faster python:
	* access global variables is SLOWER than local variables
	* accessing functions through obj.func is slower than storing func as local variable (cost for function lookup on object)


# Topics done
