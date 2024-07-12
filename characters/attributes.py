import random


class Attributes:
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self._strength = strength
        self._dexterity = dexterity
        self._constitution = constitution
        self._intelligence = intelligence
        self._wisdom = wisdom
        self._charisma = charisma

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        if value < 0:
            raise ValueError("Strength cannot be negative")
        self._strength = value

    @property
    def dexterity(self):
        return self._dexterity

    @dexterity.setter
    def dexterity(self, value):
        if value < 0:
            raise ValueError("Dexterity cannot be negative")
        self._dexterity = value

    @property
    def constitution(self):
        return self._constitution

    @constitution.setter
    def constitution(self, value):
        if value < 0:
            raise ValueError("Constitution cannot be negative")
        self._constitution = value

    @property
    def intelligence(self):
        return self._intelligence

    @intelligence.setter
    def intelligence(self, value):
        if value < 0:
            raise ValueError("Intelligence cannot be negative")
        self._intelligence = value

    @property
    def wisdom(self):
        return self._wisdom

    @wisdom.setter
    def wisdom(self, value):
        if value < 0:
            raise ValueError("Wisdom cannot be negative")
        self._wisdom = value

    @property
    def charisma(self):
        return self._charisma

    @charisma.setter
    def charisma(self, value):
        if value < 0:
            raise ValueError("Charisma cannot be negative")
        self.charisma = value

    def __str__(self):
        return (f"Strength: {self.strength}, Dexterity: {self.dexterity}, Constitution: {self.constitution}, "
                f"Intelligence: {self.intelligence}, Wisdom: {self.wisdom}, Charisma: {self.charisma}")

    def __repr__(self):
        return (f"Attributes(strength={self.strength}, dexterity={self.dexterity}, constitution={self.constitution}, "
                f"intelligence={self.intelligence}, wisdom={self.wisdom}, charisma={self.charisma}")
