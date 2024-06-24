import json

FILE_NAME = "destinations.json"


def check_directory():
    try:
        with open(FILE_NAME, "r") as file:
            destinations = json.load(file)
            return destinations
    except:
        with open(FILE_NAME, "w") as file:
            destinations = []
            return destinations


def save_json(destinations):
    with open(FILE_NAME, "w") as file:
        json.dump(destinations, file)
