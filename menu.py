#!/usr/bin/python

import os, sys
if hasattr(__builtins__, "raw_input"):
    input = raw_input

class Menus():
    """each class instance stores a list of line item descriptions
        and a list of corresponding functions that the items should run
        """
    def __init__(self, menu_title, menu_type="menu", menu_footer=None):
        self.menu_title = menu_title
        self.menu_type = menu_type
        self.menu_footer = menu_footer
        self.menu_items = []
        self.menu_functions = []

    def add_item(self, menu_item, menu_function):
        self.menu_items.append(menu_item)
        self.menu_functions.append(menu_function)

    def print_menu(self):
        while True:
            os.system("clear")

            print(self.menu_title)

            counter = 0
            for menu_item in self.menu_items:
                counter += 1
                print("   {}  {}".format(counter, menu_item))

            print(self.menu_footer)

            selection = int(input("Please select an item: "))

            return self.menu_functions[selection - 1], self.menu_type


def init():
    """Setup the menus here.  All menu class instances must be created first,
        then menu items added second.  Each menu item should include the function
        object (no parentheses) that is called when the menu item is selected.
        """
    main_menu = Menus("Main Menu")
    sub1_menu = Menus("Sub Menu 1")
    sub1_a_menu = Menus("Sub Menu 1.a")
    sub1_b_menu = Menus("Sub Menu 1.b")
    sub2_menu = Menus("Sub Menu 2")
    sub2_a_menu = Menus("Sub Menu 2.a")

    main_menu.add_item("Open Sub Menu 1", sub1_menu.print_menu)
    main_menu.add_item("Open Sub Menu 2", sub2_menu.print_menu)
    main_menu.add_item("Exit", sys.exit)

    sub1_menu.add_item("Open Sub Menu 1.a", sub1_a_menu.print_menu)
    sub1_menu.add_item("Open Sub Menu 1.b", sub1_b_menu.print_menu)
    sub1_menu.add_item("Test Function", test_function)
    sub1_menu.add_item("Back", main_menu.print_menu)

    sub1_a_menu.add_item("Back", sub1_menu.print_menu)
    sub1_b_menu.add_item("Back", sub1_menu.print_menu)

    sub2_menu.add_item("Open Sub Menu 2.a", sub1_a_menu.print_menu)
    sub2_menu.add_item("Back", main_menu.print_menu)

    sub2_a_menu.add_item("Back", sub2_menu)

    return main_menu.print_menu

def test_function():
    print("This is a test function.")
    x = input("Press enter to continue...")

### Program start

current_menu = init()

while True:
    choice, type = current_menu()
    if type == "menu":
        current_menu = choice
    else:
        choice()



