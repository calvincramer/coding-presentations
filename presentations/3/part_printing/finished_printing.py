#!/usr/bin/python3


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
        print('before ' + 20 + ' after')
    except:
        print("Can't concatenate str and non-str")
    string_var = 'apple'
    print('before ' + str(20) + ' after')
    print('before ' + string_var + ' after')
    print('before ' + str(3.1415) + ' after')

    # TODO print object default / better
    class MyObj:
        # pass
        def __str__(self):
            return 'some value from object'
    my_obj = MyObj()
    print('before ' + str(my_obj) + ' after')

    # TODO print formatted numbers
    # No thanks.
    # TODO print width specifiers
    # No thanks.
    # TODO use as a template
    # Not elegantly.


def percent_format():
    # TODO percent formatting (widely used in python 2.x, considered 'old' way)
    print('%s' % 'string')
    print('%s %s' % ('string', 5))     # No need to call str explicitly

    # TODO width specifiers
    print('%10s %s' % ('string', 5))
    print('%-10s %s' % ('string', 5))

    # TODO numbers
    print('|%8d|%8.2f|' % (1234, 3.1415))
    print('|%08d|%08.2f|' % (1234, 3.1415))
    print('|d %d|o %o|x %x|e %e|f %f|' % (20, 20, 20, 31415, 31415))

    # TODO keywords
    print('|%(pos)d|%(neg)d|' % {'pos': 5, 'neg': -5})
    print('|%(pos)d|%(neg)d|%(pos)d|' % {'pos': 5, 'neg': -5})

    # TODO use as template
    template = '%s %s'
    print(template % ('Hello', 'world'))
    print(template % ('Goodbye',  'world'))


def string_format():
    # TODO string formatting
    print('One: {} Two: {}'.format(1, 2))
    print('One: {1} Two: {0}'.format('apple', 'orange'))   # Reordering by index
    print('{0} {1} {0}'.format('apple', 'orange'))   # Using more than once

    # TODO width specifiers
    print('|{:7}|'.format('hey'))
    print('|{:>7}|'.format('hey'))
    print('|{:<7}|'.format('hey'))
    print('|{:^7}|'.format('hey'))
    
    # TODO numbers
    print('|{:8}|{:8.3}|'.format(5, 3.1415))
    print('|{:08}|{:08.3}|'.format(5, 3.1415))
    print('0b{0:b} {0:d} 0o{0:o} 0x{0:x}|'.format(20))

    # TODO keywords
    print('uname: {name} {bits} {smp_up}'.format(name='ala-john-doe', bits='64', smp_up='smp'))
    description = {
        'name': 'ala-john-doe', 
        'bits': '64', 
        'smp_up': 'smp', 
        'endianness': 'little',
    }
    print('uname: {name} {bits} {smp_up}'.format(**description))

    # TODO use as template
    template = '{} {}'
    print(template.format('Hello', 'world'))
    print(template.format('Goodbye', 'world'))


def f_string():
    # TODO f-strings

    # TODO width specifiers

    # TODO numbers

    # TODO keywords

    # TODO use as template
    pass

def templates():
    from string import Template
    # TODO
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
templates()
# speed_comparison()
print('\n')




"""
Maybe things to add

* string multiplication -> my_str * 5

* ranking of when to use each
    * string concat when extremely simple formatting, only two operands
    * don't use string concat when need any number formatting
    * use percent formatting if really concerned about speed

* syntax for each
    * in powerpoint slides show exact syntax
    * https://docs.python.org/3/library/string.html#format-specification-mini-language

* Template module in string module
"""