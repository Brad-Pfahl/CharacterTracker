import random
import re


class DiceRoller:
    @staticmethod
    def roll_dice(dice_type):
        match = re.match(r"(\d*)d(\d+)([+-]?\d+)?", dice_type)
        if not match:
            raise ValueError(f"Invalid dice type {dice_type}")

        num_dice = int(match.group(1)) if match.group(1) else 1
        dice_value = int(match.group(2))
        modifier = int(match.group(3)) if match.group(3) else 0

        total = sum(random.randint(1, dice_value) for _ in range(num_dice)) + modifier
        print(f"Rolling {dice_type}: {total}")
        return total

    @staticmethod
    def silent_roll_dice(dice_type):
        match = re.match(r"(\d*)d(\d+)([+-]?\d+)?", dice_type)
        if not match:
            raise ValueError(f"Invalid dice type {dice_type}")

        num_dice = int(match.group(1)) if match.group(1) else 1
        dice_value = int(match.group(2))
        modifier = int(match.group(3)) if match.group(3) else 0

        total = sum(random.randint(1, dice_value) for _ in range(num_dice)) + modifier
        return total

    @staticmethod
    def roll(dice_type):
        dice_sides = {
            "d100": 100,
            "d20": 20,
            "d12": 12,
            "d10": 10,
            "d8": 8,
            "d6": 6,
            "d4": 4,
            "d2": 2
        }

        if dice_type not in dice_sides:
            raise ValueError(f"Invalid dice type {dice_type}")

        result = random.randint(1, dice_sides[dice_type])
        print(f"Rolling {dice_type}: {result}")
        return result

    @staticmethod
    def silent_roll(dice_type):
        dice_sides = {
            "d100": 100,
            "d20": 20,
            "d12": 12,
            "d10": 10,
            "d8": 8,
            "d6": 6,
            "d4": 4,
            "d2": 2
        }

        if dice_type not in dice_sides:
            raise ValueError(f"Invalid dice type {dice_type}")

        result = random.randint(1, dice_sides[dice_type])
        return result
