#!/usr/bin/python

import os, sys

# ---allow input to function in 2 & 3
if hasattr(__builtins__, "raw_input"):
    input = raw_input

class Menus():
    """Menu class

    Each Menus class instance stores a list of line item descriptions
    and a corresponding function object that the menu item should run
    if it is selected. menu_first_function should be set to the first
    function to be run.
    """
    master_menus = []
    menu_first_function = None

    def __init__(self, menu_title, menu_footer=None):
        self.menu_title = menu_title
        self.menu_footer = menu_footer
        self.menu_items = []
        self.menu_functions = []
        self.menu_type = []

        Menus.master_menus.append(self)

    def add_item(self, menu_item, menu_function, menu_type="menu"):
        """this method will add a single line item to an individual menu.
        menu_item: will be printed for the user to see
        menu_function: the function to be run should the menu item be selected
        menu_type: specifies the type of function, such as another menu or a custom function
        """
        self.menu_items.append(menu_item)
        self.menu_functions.append(menu_function)
        self.menu_type.append(menu_type)

    def print_menu(self):
        while True:
            os.system("clear")

            print(self.menu_title)

            counter = 0
            for menu_item in self.menu_items:
                counter += 1
                print("   {}  {}".format(counter, menu_item))

            if self.menu_footer:
                print(self.menu_footer)

            try:
                selection = int(input("Please select an item: "))

            except ValueError:
                input("\nPlease enter a selection, [1 - {0}]".format(counter+1) )
            else:
                return self.menu_functions[selection - 1], self.menu_type[selection - 1]

def save_menus():
    pass

def load_menus():
    pass

def my_menu():
    """Setup an example menu.  All menu class instances must be created first,
        then menu items added second.  Each menu item should include the function
        object (no parentheses) that is called when the menu item is selected.
        """
    main_menu = Menus("Main Menu")
    sub1_menu = Menus("Sub Menu 1")
    sub1_a_menu = Menus("Sub Menu 1.a")
    sub1_b_menu = Menus("Sub Menu 1.b")
    sub2_menu = Menus("Sub Menu 2")
    sub2_a_menu = Menus("Sub Menu 2.a")

    Menus.menu_first_function = main_menu.print_menu

    main_menu.add_item("Open Sub Menu 1", sub1_menu.print_menu)
    main_menu.add_item("Open Sub Menu 2", sub2_menu.print_menu)
    main_menu.add_item("Exit", sys.exit)

    sub1_menu.add_item("Open Sub Menu 1.a", sub1_a_menu.print_menu)
    sub1_menu.add_item("Open Sub Menu 1.b", sub1_b_menu.print_menu)
    sub1_menu.add_item("Test Function", test_function, "function")
    sub1_menu.add_item("Back", main_menu.print_menu)

    sub1_a_menu.add_item("Back", sub1_menu.print_menu)
    sub1_b_menu.add_item("Back", sub1_menu.print_menu)

    sub2_menu.add_item("Open Sub Menu 2.a", sub1_a_menu.print_menu)
    sub2_menu.add_item("Back", main_menu.print_menu)

    sub2_a_menu.add_item("Back", sub2_menu)

    return

def test_function():
    print("This is a test function.")
    x = input("Press enter to continue...")

### Program start

if __name__ == "__main__":

    my_menu()

    current_menu = Menus.menu_first_function

    while True:
        try:
            choice, type = current_menu()
        except TypeError:
            print("Menu handling error. Probably forgot to set type='function',"
                "please check your menu setup.")
            print("Function: {0}".format(str(current_menu)))
            sys.exit()

        if type == "menu":
            current_menu = choice
        else:
            choice()



