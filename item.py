class Item:
    def __init__(self, name, rarity = "common", desc = "", value=0):
        self.name = name
        self.desc = desc
        self.value = value
        self.rarity = rarity

class Weapon(Item):
    def __init__(self, name, damage, rarity = "common", desc="", value=0, effects=None):
        super().__init__(name, rarity, desc, value)
        self.damage = damage
        self.effects = effects or []

class Armor(Item):
    def __init__(self, name, defense, rarity="common", desc="", value=0, effects=None):
        super().__init__(name,rarity, desc, value)

class Potion(Item):
    def __init__(self, name, rarity="common", desc="", value=0, effects=None, potency=1):
        super().__init__(name, rarity, desc, value)
        self.effects = effects or []
        self.potency = potency

class Effect:
    def on_hit(self, attacker, target):
        pass

    def on_equip(self, player):
        pass

    def on_unequip(self,player):
        pass
