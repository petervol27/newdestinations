def destinations_list(destinations):
    for destination in destinations:
        print(
            f"{destination['name']} is {destination['desc']} with a score of {destination['score']}/10 ★"
        )


def add_destination(destinations):
    try:
        destination_name = input("enter destination name: ").capitalize()
        destination_description = input("enter destination description: ")
        destination_score = int(
            input("enter destination score: (must be number between 1 and 10) ")
        )
        for check in range(0, 11):
            if destination_score == check:
                destinations.append(
                    {
                        "name": destination_name,
                        "desc": destination_description,
                        "score": destination_score,
                    }
                )
                print(f"{destination_name} added succesfully!!")

    except Exception as ex:
        print(ex, "score needs to be a number between 1-10!!!")


def edit_destination(destinations):
    check_exists = False
    selection = input("enter destination to edit: ").lower()
    what_to_edit = input(
        "enter 0 to edit name, 1 to edit description or 2 to edit score: "
    )
    if what_to_edit == "0":
        for destination in destinations:
            if selection == destination["name"].lower():
                check_exists = True
                new_name = input("enter new name for destination: ")
                destination["name"] = new_name.capitalize()
                print(f"{selection} has been changed to {new_name}")
        if not check_exists:
            print(f"{selection} does not exists")

    elif what_to_edit == "1":
        for destination in destinations:
            if selection == destination["name"].lower():
                check_exists = True
                new_description = input("enter new description: ")
                destination["desc"] = new_description
                print(f"{selection} description has been changed to {new_description}")
        if not check_exists:
            print(f"{selection} does not exists")
    elif what_to_edit == "2":
        for destination in destinations:
            if selection == destination["name"].lower():
                try:
                    check_exists = True
                    new_score = int(input("enter new score: "))
                    for check in range(1, 11):
                        if new_score == check:
                            destination["score"] = new_score
                            print(
                                f"{selection} score has been changed to {new_score}/10★"
                            )
                            break
                        elif check == 10:
                            print(
                                "not in range of numbers, enter number between 1 and 10!!"
                            )
                except Exception as ex:
                    print(ex, "score must be a number!!!")
        if not check_exists:
            print(f"{selection} does not exists")
    else:
        print("invalid input!!!")


def remove_destination(destinations):
    check_exists = False
    selection = input("enter destination name to remove: ").lower()
    for destination in destinations:
        if selection == destination["name"].lower():
            check_exists = True
            destinations.remove(destination)
            print(selection, "has been removed!")
    if not check_exists:
        print(f"{selection} does not exist!")
