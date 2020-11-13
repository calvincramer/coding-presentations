#!/usr/bin/python3


def concat():
    print(' concat')
    # TODO Useful things to know about python strings
    # TODO characters are just 1-length strings

    # TODO single and double quotes are basically the same

    # TODO print string by appending

    # TODO print formatted numbers

    # TODO print width specifiers

    # TODO use as a template
    # as a function


def percent_format():
    print('\n percent')
    # TODO percent formatting (widely used in python 2.x, considered 'old' way)

    # TODO width specifiers

    # TODO number formatting

    # TODO keywords

    # TODO use as template


def string_format():
    print('\n format')
    # TODO string formatting

    # TODO width specifiers

    # TODO number formatting

    # TODO keywords

    # TODO use as template


def f_string():
    print('\n f-strings')
    # TODO f-strings

    # TODO width specifiers

    # TODO number formatting

    # TODO use as template


def templates():
    from string import Template
    print('\n Template')
    # TODO templates

    # TODO width specifiers

    # TODO number formatting


def speed_comparison():
    from timeit import timeit
    print('\n speed comparison')
    # TODO compare concat, %, string format, f-string, template speeds


print('\n')
concat()
percent_format()
string_format()
f_string()
templates()
speed_comparison()
print('\n')
