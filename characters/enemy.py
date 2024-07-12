from utils.dice_rolls import DiceRoller


class Enemy:
    def __init__(self, name, base_attributes, base_stats, challenge_rating):
        self.name = name
        self.base_attributes = base_attributes
        self.base_stats = base_stats
        self.challenge_rating = challenge_rating

    @property
    def health(self):
        return DiceRoller.silent_roll_dice(self.base_stats["health"])

    @property
    def attack(self):
        return DiceRoller.silent_roll_dice(self.base_stats["attack"])

    @property
    def damage(self):
        return DiceRoller.silent_roll_dice(self.base_stats["damage"])

    def __repr__(self):
        return (f"Enemy(name={self.name}, "
                f"base_attributes={self.base_attributes}, "
                f"base_stats={self.base_stats}, "
                f"health={self.health}, "
                f"attack={self.attack}, "
                f"damage={self.damage}, "
                f"challenge_rating={self.challenge_rating})")
