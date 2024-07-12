import os
from characters.player import Player
from utils.enemy_loader import load_enemies, get_enemy_by_name, get_enemy_by_challenge_rating
from utils.item_loader import load_items, get_item_by_name


def main():
    # Load enemies from JSON
    current_dir = os.path.dirname(__file__)
    enemies_json_path = os.path.join(current_dir, 'enemies.json')
    items_json_path = os.path.join(current_dir, 'items.json')

    enemies = load_enemies(enemies_json_path)
    items = load_items(items_json_path)

    # Display all loaded enemies
    print("Loaded Enemies:")
    for enemy in enemies:
        print(enemy)

    # Get a specific enemy by name
    goblin = get_enemy_by_name(enemies, "Goblin")
    if goblin:
        print(f"\nSpecific Enemy - Goblin: {goblin}")
    else:
        print("\nGoblin not found.")

    # Get enemies by challenge rating
    print("\nEnter a challenge rating: ")
    challenge_rating_input = input()
    matching_enemies = get_enemy_by_challenge_rating(enemies, challenge_rating_input)

    # Print all enemies with the matching challenge rating
    print("\nEnemies by challenge rating:")
    if matching_enemies:
        for enemy in matching_enemies:
            print(enemy)
    else:
        print("No enemies found for challenge rating:", challenge_rating_input)

    # Display all loaded items
    print("\nLoaded Items:")
    for item in items:
        print(item)

    # Get a specific item by name
    sword_of_strength = get_item_by_name(items, "Sword of Strength")
    if sword_of_strength:
        print(f"\nSpecific Item - Sword of Strength: {sword_of_strength}")
    else:
        print("\nSword of Strength not found.")

    # Create a player with initial attributes and stats
    player_attributes = {
        "strength": 10,
        "dexterity": 10,
        "constitution": 10,
        "intelligence": 10,
        "wisdom": 10,
        "charisma": 10
    }
    player_base_stats = {
        "health": 100,
        "attack": 10,
        "armor_class": 10,
        "speed": 10
    }

    player = Player(name="Hero", attributes=player_attributes, base_stats=player_base_stats)
    print("\nCreated Player:")
    print(player)

    # Equip an item and display player's stats
    if sword_of_strength:
        player.equip_item(sword_of_strength)
        print("\nPlayer after equipping Sword of Strength:")
        print(player)

    # Unequip the item and display player's stats
    if sword_of_strength:
        player.unequip_item("Sword of Strength")
        print("\nPlayer after unequipping Sword of Strength:")
        print(player)


if __name__ == "__main__":
    main()
