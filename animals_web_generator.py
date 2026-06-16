import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')


def print_animals_data(list_animals):
    for animal in list_animals:
        print(f"Name: {animal["name"]}")
        print(f"Diet: {animal["characteristics"]["diet"]}")
        print(f"Location: {animal["locations"][0]}")
        animal_type = animal["characteristics"].get("type", None)
        if animal_type:
            print(f"Type: {animal_type}")
        print("")


