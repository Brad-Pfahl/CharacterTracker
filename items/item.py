from utils.dice_rolls import DiceRoller


class Item:
    def __init__(self, name, effects):
        self.name = name
        self.effects = effects

    def __repr__(self):
        return f"Item(name={self.name}, effects={self.effects})"
