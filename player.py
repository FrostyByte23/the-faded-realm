import random
class Player:

    def __init__(self):
        self.name = None
        self.race = None

        #Health
        self.max_health = 10
        self.health = self.max_health

        #Combat
        self.dodge = 2
        self.attack = 2
        self.defense = 0
        self.armor = None
        self.weapon = None

        #Progression
        self.level = 1
        self.xp = 0

        #Collectables
        self.gold = 50
        self.inventory = []

        #Status
        self.alive = True

        #Stats
        self.strength = 0
        self.dexterity = 0
        self.intelligence = 0
        self.magical_power = 0
        self.luck = 0

    def add_gold(self, gold):
        self.gold += gold

    def lose_gold(self,gold):
        self.gold -= gold
        if self.gold < 0:
            self.gold = 0

    def buy(self, price):
        if self.gold >= price:
            self.gold -= price
            return True
        return False

    def give_item(self, item):
        self.inventory.append(item)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False

    def heal(self, healing_amount):
        self.health += healing_amount
        if self.health > self.max_health:
            self.health = self.max_health

    def check(self, roll_type, amount):
        stats = {
            "str": self.strength,
            "dex": self.dexterity,
            "int": self.intelligence,
            "mp": self.magical_power,
            "lck": self.luck
        }

        if roll_type not in stats:
            raise ValueError(f"Invalid roll type: {roll_type}")

        roll = random.randint(1,20) + stats[roll_type]
        return roll >= amount

    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Race: {self.race.name}")
        print(f"Max Health: {self.max_health}")
        print(f"Health: {self.health}")
        print(f"Str: {self.strength}")
        print(f"Dex: {self.dexterity}")
        print(f"Int: {self.intelligence}")
        print(f"MP: {self.magical_power}")
        print(f"LCK: {self.luck}")
        print(f"Dodge: {self.dodge}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Armor: {self.armor}")
        print(f"Weapon: {self.weapon}")
        print(f"Level: {self.level}")
        print(f"XP: {self.xp}")
        print(f"Gold: {self.gold}")
        print(f"Inventory: {self.inventory}")
        input("Press Enter to continue...")
