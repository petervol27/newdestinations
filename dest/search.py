def search_destination(destinations):
    print("search for destination")
    destinations_found = []
    selection = input("enter 0 to search by name or 1 to search by score:")
    try:
        if selection == "0":
            search_term = input("enter name/letter to search by: ")
            for destination in destinations:
                if (
                    destination["name"].lower().startswith(search_term)
                    or search_term in destination["name"].lower()
                ):
                    destinations_found.append(destination)
        elif selection == "1":
            search_term = int(
                input("enter score to find destinations with score or higher: ")
            )
            for destination in destinations:
                if destination["score"] >= search_term:
                    destinations_found.append(destination)
        else:
            print("invalid input should be 0 or 1")
        if destinations_found:
            for destination in destinations_found:
                print(
                    f"{destination['name']} found! and has a score of {destination['score']}"
                )
        else:
            print("no destinations found!")
    except Exception as ex:
        print(ex)
