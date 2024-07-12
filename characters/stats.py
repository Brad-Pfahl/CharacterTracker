
class Stats:
    def __init__(self, health=0, attack=0, armor_class=10, speed=0, damage=0):
        self.health = health
        self.attack = attack
        self.armor_class = armor_class
        self.speed = speed
        self.damage = damage

    def __repr__(self):
        return f"Stats(health={self.health}, attack={self.attack}, armor_class={self.armor_class}, speed={self.speed}, damage={self.damage})"
