#!/usr/bin/python

import os

class Menus():
    """each class instance stores a list of line item descriptions
        and a list of corresponding functions that the items should run
        """
    def __init__(self, menu_title, menu_footer):
        self.menu_title = menu_title
        self.menu_footer = menu_footer
        self.menu_items = []
        self.menu_functions = []

    def add_item(self, menu_item, menu_function):
        self.menu_item.append(menu_item)
        self.menu_function = menu_function.append(menu_function)

    def print_menu():
        os.system("clear")

        print(self.menu_title)

        counter = 0
        for menu_item in self.menu_items:
            counter += 1
            print("   {}  {}".format(counter, menu_item))

        print(self.menu_footer)

        selection = raw_input("Please select an item: ")

        return self.menu_function[selection - 1]




