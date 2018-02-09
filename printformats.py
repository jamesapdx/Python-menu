#!/usr/bin/python

""" use in format: "{RED_FG}{0}{RESET}".format(variable, **printformats.print_formats)
from https://stackoverflow.com/questions/287871/print-in-terminal-with-colors
"""

formatting = {
    'RESET' : '\033[0m',
    'END' : '\033[0m',
    'BOLD' : '\033[01m',
    'UNDERLINE' : '\033[04m',
    'REVERSE' : '\033[07m',
    'STRIKETHROUGH' : '\033[09m',
    'ITALIC' : '\33[3m',

    'LINE' : '=',
    'BLANK' : ' ',
    'SPACER' : ' ',
    'DEFAULT' : '',
    'MARK' : 'X',

    'BLACK_FG' : '\033[30m',
    'RED_FG' : '\033[31m',
    'GREEN_FG' : '\033[32m',
    'ORANGE_FG' : '\033[33m',
    'BLUE_FG' : '\033[34m',
    'PURPLE_FG' : '\033[35m',
    'CYAN_FG' : '\033[36m',
    'LIGHTGREY_FG' : '\033[37m',
    'DARKGREY_FG' : '\033[90m',
    'LIGHTRED_FG' : '\033[91m',
    'LIGHTGREEN_FG' : '\033[92m',
    'YELLOW_FG' : '\033[93m',
    'LIGHTBLUE_FG' : '\033[94m',
    'PINK_FG' : '\033[95m',
    'LIGHTCYAN_FG' : '\033[96m',

    'BLACK_BG' : '\033[40m',
    'RED_BG' : '\033[41m',
    'GREEN_BG' : '\033[42m',
    'ORANGE_BG' : '\033[43m',
    'BLUE_BG' : '\033[44m',
    'PURPLE_BG' : '\033[45m',
    'CYAN_BG' : '\033[46m',
    'LIGHTGREY_BG' : '\033[47m'
    }