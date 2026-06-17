import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_animals_data(list_animals):
    output = ""
    for animal in list_animals:
        output += '<li class="cards__item">'
        output += f"Name: {animal['name']}<br/>\n"
        output += f"Diet: {animal["characteristics"]["diet"]}<br/>\n"
        output += f"Location: {animal["locations"][0]}<br/>\n"
        animal_type = animal["characteristics"].get("type", None)
        if animal_type:
            output += f"Type: {animal_type}<br/>\n"
        output += "</li >"
        output += "\n"
    return output


def replace_text_html(html_file, new_text):
    with open(html_file, "r") as handle:
        html_text = handle.read()
    html_text = html_text.replace("__REPLACE_ANIMALS_INFO__", new_text)
    with open("new.html", "w") as handle:
        handle.write(html_text)


animals_data = load_data('animals_data.json')

text_pagina = get_animals_data(animals_data)

replace_text_html("animals_template.html", text_pagina)
