#!/usr/bin/python3


def concat():
    print('\n concat')
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

    # TODO print formatted numbers
    # No thanks.

    # TODO print width specifiers
    # No thanks.

    # TODO use as a template
    # as a function
    def concat_template(a, b):
        return str(a) + str(b)
    print(concat_template('concatenate me', ' please'))


def percent_format():
    print('\n percent')
    # TODO percent formatting (widely used in python 2.x, considered 'old' way)
    print('%s' % 'string')
    print('%s %s' % ('string', 5))     # No need to call str explicitly

    # TODO width specifiers
    print('%10s %s' % ('string', 5))
    print('%-10s %s' % ('string', 5))

    # TODO number formatting
    print('|%8d|%8.2f|' % (1234, 3.1415))
    print('|%08d|%08.2f|' % (1234, 3.1415))
    print('|d %d|o %o|x %x|e %e|f %f|' % (20, 20, 20, 31415, 31415))

    # TODO keywords
    print('|%(pos)d|%(neg)d|' % {'pos': 5, 'neg': -5})
    print('|%(pos)d|%(neg)d|%(pos)d|' % {'pos': 5, 'neg': -5})

    # TODO use as template
    # variable or function
    template = '%s %s'
    print(template % ('Hello', 'world'))
    print(template % ('Goodbye',  'world'))


def string_format():
    print('\n format')
    # TODO string formatting
    print('One: {} Two: {}'.format(1, 2))
    print('One: {1} Two: {0}'.format('apple', 'orange'))   # Reordering by index
    print('{0} {1} {0}'.format('apple', 'orange'))   # Using more than once

    # TODO width specifiers
    print('|{:7}|'.format('hey'))
    print('|{:>7}|'.format('hey'))
    print('|{:<7}|'.format('hey'))
    print('|{:^7}|'.format('hey'))
    
    # TODO number formatting
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
    # variable or function
    template = '{} {}'
    print(template.format('Hello', 'world'))
    print(template.format('Goodbye', 'world'))


def f_string():
    print('\n f-strings')
    # TODO f-strings
    print(f'I am {2020-1960} years old')
    age = 50
    print(f'I am {age} years old')
    make_younger = lambda x: x * 3 // 4
    print(f'I am {make_younger(age)} years old')

    # TODO width specifiers
    my_str = 'hey'
    print(f'|{my_str:7}|')
    print(f'|{my_str:>7}|')
    print(f'|{my_str:<7}|')
    print(f'|{my_str:^7}|')

    # TODO number formatting
    num1 = 20
    num2 = 3.1415
    print(f'|{num1:8}|{num2:8.3}|')
    print(f'|{num1:08}|{num2:08.3}|')
    print(f'0b{num1:b} {num1:d} 0o{num1:o} 0x{num1:x}|')

    # TODO use as template
    # not directly, need to use a function
    def f_string_template(a, b):
        return f'{a} {b}'
    print(f_string_template('this is a', 'template'))

    print(f'{"Hello" + str(5)} asdf')


def templates():
    from string import Template
    print()
    # TODO templates
    my_template = Template('$number_1 score and ${number_2}years ago')
    print(my_template.substitute(number_1=4, number_2=7))

    # TODO width specifiers
    # No support. Need to use percent for string.format
 
    # TODO number formatting
    # No support. Need to use percent for string.format


def speed_comparison():
    from timeit import timeit
    print('\n speed comparison')
    times = 7_000_000
    micro_per_s = 1_000_000

    total_to_indiv = lambda total: total * micro_per_s / times 
    def print_result(name, total):
        print(f'{name:10}: total: {total:>6.3f}s: each: {total_to_indiv(total):>6.3f}μs')
    
    print_result('concat',   timeit("""a = 50; b = 'asdf'; c = str(a) + b""", number=times))
    print_result('percent',  timeit("""a = 50; b = 'asdf'; c = '%d%s' % (a, b)""", number=times))
    print_result('format',   timeit("""a = 50; b = 'asdf'; c = '{}{}'.format(a, b)""", number=times))
    print_result('f-string', timeit("""a = 50; b = 'asdf'; c = f'{a}{b}'""", number=times))

    # TODO template
    # TODO


print('\n')
concat()
percent_format()
string_format()
f_string()
templates()
speed_comparison()
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

* multiline formatting for each method
"""
