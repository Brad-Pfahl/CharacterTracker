from characters.attributes import Attributes
from characters.stats import Stats
from items.item import Item


class Player:
    def __init__(self, name, attributes, base_stats):
        self.name = name
        self.attributes = Attributes(**attributes)
        self.base_stats = Stats(**base_stats)
        self.current_stats = Stats(**base_stats)
        self.inventory = []
        self.equipped_items = {}

        # Update current stats based on attributes
        self.update_stats()

    def update_stats(self):
        # Update health based on constitution
        self.current_stats.health = self.base_stats.health + self.attributes.constitution * 2

        # Update other stats based on attributes
        self.current_stats.attack = self.base_stats.attack + self.attributes.strength
        self.current_stats.armor_class = self.base_stats.armor_class + self.attributes.dexterity
        self.current_stats.speed = self.base_stats.speed + self.attributes.dexterity

    def equip_item(self, item):
        if not isinstance(item, Item):
            raise ValueError("Can only equip items of type Item")
        self.equipped_items[item.name] = item
        self.apply_item_effects(item)

    def unequip_item(self, item_name):
        if item_name in self.equipped_items:
            item = self.equipped_items.pop(item_name)
            self.remove_item_effects(item)

    def apply_item_effects(self, item):
        # Adjust stats based on item effects
        for effect, value in item.effects.items():
            if hasattr(self.current_stats, effect):
                setattr(self.current_stats, effect, getattr(self.current_stats, effect) + value)
            if hasattr(self.attributes, effect):
                setattr(self.attributes, effect, getattr(self.attributes, effect) + value)
        self.update_stats()  # Update current stats after applying item effects

    def remove_item_effects(self, item):
        # Revert stats based on item effects
        for effect, value in item.effects.items():
            if hasattr(self.current_stats, effect):
                setattr(self.current_stats, effect, getattr(self.current_stats, effect) - value)
            if hasattr(self.attributes, effect):
                setattr(self.attributes, effect, getattr(self.attributes, effect) - value)
        self.update_stats()  # Update current stats after removing item effects

    def add_to_inventory(self, item):
        if not isinstance(item, Item):
            raise ValueError("Can only add items of type Item")
        self.inventory.append(item)

    def remove_from_inventory(self, item_name):
        self.inventory = [item for item in self.inventory if item.name != item_name]

    def __repr__(self):
        return (f"Player(name={self.name}, attributes={self.attributes}, "
                f"current_stats={self.current_stats}, inventory={self.inventory}, "
                f"equipped_items={self.equipped_items})")
