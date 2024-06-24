from storage.saveload import save_json, check_directory
from dest.actions import (
    add_destination,
    edit_destination,
    remove_destination,
    destinations_list,
)
from dest.search import search_destination


def destination_menu():
    destinations = check_directory()
    print("Welcome to our destinations!!!")
    while True:
        print("1 - List the destinations")
        print("2 - Add destination")
        print("3 - Edit destination")
        print("4 - Remove destination")
        print("5 - Search for destination")
        print("6 - Exit Program")
        selection = input("enter digit to select action: ")
        if selection == "6":
            save_json(destinations)
            print("Thanks for using our services!")
            break
        elif selection == "1":
            destinations_list(destinations)
        elif selection == "2":
            add_destination(destinations)
        elif selection == "3":
            edit_destination(destinations)
        elif selection == "4":
            remove_destination(destinations)
        elif selection == "5":
            search_destination(destinations)
        else:
            print("invalid input!!! should be a digit from 1 to 6!")
