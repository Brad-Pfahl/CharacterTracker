import json
from items.item import Item


def load_items(filename):
    with open(filename, 'r') as file:
        items_data = json.load(file)  # Properly load the JSON data into a dictionary

    items = []
    for item_data in items_data["items"]:
        item = Item(
            name=item_data["name"],
            effects=item_data["effects"]
        )
        items.append(item)
    return items


def get_item_by_name(items, name):
    for item in items:
        if item.name == name:
            return item
    return None
