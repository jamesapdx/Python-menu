#!/usr/bin/python

""" use: "{red}{0}{reset}".format(variable, **printformats.print_formats)
from https://stackoverflow.com/questions/287871/print-in-terminal-with-colors
"""
print_formats = {
    'reset' : '\033[0m',
    'bold' : '\033[01m',
    'disable' : '\033[02m',
    'underline' : '\033[04m',
    'reverse' : '\033[07m',
    'strikethrough' : '\033[09m',
    'invisible' : '\033[08m',
    'italic' : '\33[3m',
    'line' : '=',
    'space' : ' ',
    'default' : '',

    'black' : '\033[30m',
    'red' : '\033[31m',
    'green' : '\033[32m',
    'orange' : '\033[33m',
    'blue' : '\033[34m',
    'purple' : '\033[35m',
    'cyan' : '\033[36m',
    'lightgrey' : '\033[37m',
    'darkgrey' : '\033[90m',
    'lightred' : '\033[91m',
    'lightgreen' : '\033[92m',
    'yellow' : '\033[93m',
    'lightblue' : '\033[94m',
    'pink' : '\033[95m',
    'lightcyan' : '\033[96m',

    'black_bg' : '\033[40m',
    'red_bg' : '\033[41m',
    'green_bg' : '\033[42m',
    'orange_bg' : '\033[43m',
    'blue_bg' : '\033[44m',
    'purple_bg' : '\033[45m',
    'cyan_bg' : '\033[46m',
    'lightgrey_bg' : '\033[47m'
    }