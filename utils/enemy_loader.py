import json
from characters.enemy import Enemy


def load_enemies(filename):
    with open(filename, 'r') as file:
        enemies_data = json.load(file)

    enemies = []
    for enemy_data in enemies_data["enemies"]:
        enemy = Enemy(
            name=enemy_data["name"],
            base_attributes=enemy_data["base_attributes"],
            base_stats=enemy_data["base_stats"],
            challenge_rating=enemy_data["challenge_rating"]
        )
        enemies.append(enemy)
    return enemies


def get_enemy_by_name(enemies, name):
    for enemy in enemies:
        if enemy.name == name:
            return enemy
    return None


# Todo: fix this ->
def get_enemy_by_challenge_rating(enemies, challenge_rating):
    matching_enemies = []
    for enemy in enemies:
        if enemy.challenge_rating == challenge_rating:
            matching_enemies.append(enemy)
    return matching_enemies
