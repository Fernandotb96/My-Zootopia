import json


def load_data(file_path):
    """ Loads the animals data from the JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """ Serializes the animal's info into an HTML <li> block."""
    diet = animal["characteristics"]["diet"]
    location = animal["locations"][0]
    animal_type = animal["characteristics"].get("type", None)
    output = f"""<li class='cards__item'>
        <div class='card__title'>{animal['name']}</div> <br/>
        <p class='card__text'>
            <strong>Diet:</strong> {diet}<br/>
            <strong>Location:</strong> {location}<br/>
        """
    if animal_type:
        output += f"<strong>Type:</strong> {animal_type}<br/>\n"
    output += f"    </p>\n</li>\n"
    return output


def animals_to_html(list_animals):
    """Transform list of animals into a unique HTML string."""
    output = ""
    for animal in list_animals:
        output += serialize_animal(animal)
    return output


def replace_text_html(html_file, new_text):
    """Replace HTML text with new HTML animal's text."""
    with open(html_file, "r") as handle:
        html_text = handle.read()
    html_text = html_text.replace("__REPLACE_ANIMALS_INFO__", new_text)
    with open("new.html", "w") as handle:
        handle.write(html_text)


if __name__ == "__main__":
    animals_data = load_data('animals_data.json')
    animals_html_text = animals_to_html(animals_data)
    replace_text_html("animals_template.html", animals_html_text)
