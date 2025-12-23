from player import Player
class Enemy:
    def __init__(self, name, damage, health, experience=3, value=5, desc="", entrance=""):
        self.name = name
        self.damage = damage
        self.health = health
        self.experience = experience
        self.value = value
        self.desc = desc
        self.entrance = entrance
