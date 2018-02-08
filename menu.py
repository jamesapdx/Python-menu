#!/usr/bin/python

import os, sys
import printformats as pf

# ---allow input() to function in 2 & 3
if hasattr(__builtins__, "raw_input"):
    input = raw_input

class Menus():
    """Menu class

    Each Menus class instance stores a list of line item descriptions
    and a corresponding function object that the menu item should run
    if it is selected. menus_first_function should be set to the first
    function to be run.
    """
    master_menus = []
    menus_first_function = None
    menus_note = None

    def __init__(self, title=None, title_formatting="{GREEN_FG}", footer=None, footer_formatting="{GREEN_FG}"):

        self.menu_title = title
        self.menu_title_formatting = title_formatting.format(**pf.print_formats)

        self.menu_footer = footer
        self.menu_footer_formatting = footer_formatting.format(**pf.print_formats)

        self.line_items_text = []
        self.line_items_function = []
        self.line_items_active = []
        self.line_items_type = []
        self.line_items_indent = []
        self.line_items_formatting = []
        self.line_items_been_used = []
        self.line_items_mark_as_done = []

        Menus.master_menus.append(self)
        if not Menus.menus_first_function:
            Menus.menus_first_function = self.print_menu

    def add_line_item(self, item_text, item_function, item_type="menu", item_indent=4, item_formatting="{DEFAULT}",
                 item_mark_as_done="{SPACE}"):
        """this method will add a single line item to an individual menu.
        menu_item: will be printed for the user to see
        menu_function: the function to be run should the menu item be selected
        menu_items_type: specifies the type of function, such as another menu or a custom function
        """
        self.line_items_text.append(item_text)
        self.line_items_function.append(item_function)
        self.line_items_type.append(item_type)
        self.line_items_active.append(True)

        self.line_items_indent.append(item_indent)
        self.line_items_formatting.append(item_formatting)
        self.line_items_been_used.append(False)
        self.line_items_mark_as_done.append(item_mark_as_done)

    def modify_line_item(self, item_number, item_text=None, item_function=None, item_type=None, item_indent=None,
                    item_formatting=None, item_mark_as_done=None):
        if item_text is not None:
            self.line_items_text[item_number] = item_text
        if item_function is not None:
            self.line_items_function[item_number] = item_function
        if item_type is not None:
            self.line_items_type[item_number] = item_type
        if item_indent is not None:
            self.line_items_indent[item_number] = item_indent
        if item_formatting is not None:
            self.line_items_formatting[item_number] = item_formatting
        if item_mark_as_done is not None:
            self.line_items_mark_as_done[item_number] = item_mark_as_done

    def disable_line_item(self, item_number):
        self.line_items_active[item_number] = False

    def delete_line_item(self, item_number):
        pass


    def print_menu(self):
        while True:
            os.system("clear")

            title_format = self.menu_title_formatting.format(**pf.print_formats)
            title_line = 30 * "{LINE}".format(**pf.print_formats)  #FIX
            print("{0}{1} {2} {1}{RESET}".format(
                                        title_format,
                                        title_line,
                                        self.menu_title,
                                        **pf.print_formats
                                        ))

            for counter in range(len(self.line_items_text)):
                this_line_indent = self.line_items_indent[counter] * "{SPACE}".format(**pf.print_formats)
                if self.line_items_active[counter] is True:
                    this_line_format = self.line_items_formatting[counter].format(**pf.print_formats)
                else:
                    this_line_format = "{LIGHTGREY_FG}".format(**pf.print_formats)
                #FIX too confusing, figure out a better way
                this_mark_as_done = self.line_items_mark_as_done[counter].format(**pf.print_formats)
                this_line_text = self.line_items_text[counter]

                print("{0}{1} {2} {3}{4}{RESET}".format(
                                        this_line_indent,
                                        counter + 1, #FIX format fixed width
                                        this_mark_as_done,
                                        this_line_format,
                                        this_line_text,
                                        **pf.print_formats
                                        ))

            if Menus.menus_note:
                print("   {0}".format(Menus.menus_note, **pf.print_formats))

            if self.menu_footer:
                print(self.menu_footer)

            try:
                selection = int(input("Please select an item: "))

            except ValueError:
                input("\nPlease enter a selection, [1 - {0}]".format(counter+1) )
            else:
                return self.line_items_function[selection - 1], self.line_items_type[selection - 1]

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

    Menus.menus_first_function = main_menu.print_menu

    main_menu.add_line_item("Open Sub Menu 1", sub1_menu.print_menu)
    main_menu.add_line_item("Open Sub Menu 2", sub2_menu.print_menu)
    main_menu.add_line_item("Exit", sys.exit)

    sub1_menu.add_line_item("Open Sub Menu 1.a", sub1_a_menu.print_menu)
    sub1_menu.add_line_item("Open Sub Menu 1.b", sub1_b_menu.print_menu)
    sub1_menu.add_line_item("Test Function", test_function, "function")
    sub1_menu.add_line_item("Back", main_menu.print_menu)

    sub1_a_menu.add_line_item("Back", sub1_menu.print_menu)
    sub1_b_menu.add_line_item("Back", sub1_menu.print_menu)

    sub2_menu.add_line_item("Open Sub Menu 2.a", sub1_a_menu.print_menu)
    sub2_menu.add_line_item("Back", main_menu.print_menu)

    sub2_a_menu.add_line_item("Back", sub2_menu)

    return

def test_function():
    print("This is a test function.")
    x = input("Press enter to continue...")

### Program start

if __name__ == "__main__":

    my_menu()

    current_menu = Menus.menus_first_function

    choice, type = current_menu()
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
