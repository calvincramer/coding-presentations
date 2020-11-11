#!/usr/bin/python3

class TreeNode():
    def __init__(self, value, left, right):
        self._v = value
        self._l = left
        self._r = right

    def __str__(self):
        return 'TreeNode: ' + str(self._v) + ' left: ' + str(self._l) + ' right: ' + str(self._r)

var_num = 42
var_big_num = 165_643
var_num_neg = -14
var_str = 'string'
var_float = 3.14159265 * 100
var_obj = TreeNode(value=5, left=None, right=None)


def concat():
    # TODO Useful things to know about python strings
    # TODO characters are just 1-length strings
    assert type("c") is str
    assert type("string") is str
    assert type("d") is str
    assert type("orange") is str

    # TODO single and double quotes are basically the same
    assert type('single') is type("double")
    print('single "quoted" string \'no\' escape needed for "')
    print("double 'quoted' string \"no\" escape needed for '")

    # TODO print string by appending
    try:
        # TODO string append drawbacks
        print('before ' + var_num + ' after')
    except:
        print("Can't concatenate str and non-str")
    print('before ' + str(var_num) + ' after')
    print('before ' + var_str + ' after')
    print('before ' + str(var_float) + ' after')

    # TODO print object default / better
    print('before ' + str(var_obj) + ' after')

    # TODO print formatted numbers
    # No thanks.


def percent_format():
    # TODO percent formatting (widely used in python 2.x, considered 'old' way)
    print('%s' % var_str)
    print('%s %s' % (var_str, var_num))     # No need to call str explicitly

    # TODO width specifiers
    print('%10s %s' % (var_str, var_num))
    print('%-10s %s' % (var_str, var_num))

    # TODO numbers
    print('|%d|%f|' % (var_num, var_float))
    print('|%8d|%8.2f|' % (var_big_num, var_float))
    print('|%08d|%08.2f|' % (var_big_num, var_float))
    print('|d %d|o %o|x %x|e %e|f %f|' % (var_num, var_num, var_num, var_float, var_float))

    # TODO keywords
    print('|%(pos)d|%(neg)d|' % {'pos': var_num, 'neg': var_num_neg})
    print('|%(pos)d|%(neg)d|%(pos)d|' % {'pos': var_num, 'neg': var_num_neg})


def string_format():
    pass


def f_string():
    pass


def speed_comparison():
    import random
    import time
    random.seed()
    TIMES = 3_000_000

    def _concat():
        start = time.time()
        for _ in range(TIMES):
            string = 'asdf' + str(0xf00dfeed) + str(3.1415)
        print(f'contact: {time.time() - start:.4f}')

    def _percent():
        start = time.time()
        for _ in range(TIMES):
            string = '%s%d%f' % ('asdf', 0xf00dfeed, 3.1415)
        print(f'percent: {time.time() - start:.4f}')

    def _format():
        start = time.time()
        for _ in range(TIMES):
            string = '{}{}{}'.format('asdf', 0xf00dfeed, 3.1415)
        print(f'format: {time.time() - start:.4f}')

    def _f_string():
        start = time.time()
        for _ in range(TIMES):
            string = f"{'asdf'}{0xf00dfeed}{3.1415}"
        print(f'f-string: {time.time() - start:.4f}')

    # TODO compare results
    _concat()       # this / fastest = 2.09
    _percent()      # fastest
    _format()       # this / fastest = 1.85
    _f_string()     # this / fastest = 1.68
    
    # TODO explain:
    # Percent formatting is faster probably because of syntax.
    #    It does not need to implicitly call a function like format or append


print('\n')
concat()
percent_format()
string_format()
f_string()
speed_comparison()
print('\n')




"""
Maybe things to add

* string multiplication -> my_str * 5

* ranking of when to use each
    * string concat when extremely simple formatting, only two operands
    * don't use string concat when need any number formatting
    * use percent formatting if really concerned about speed
"""