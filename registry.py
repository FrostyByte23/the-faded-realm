from item import Weapon, Potion
from enemy import Enemy
from race import Human, Elf, Dwarf
# ITEMS
def iron_sword():
    return Weapon(
        name="Iron Sword",
        damage=3,
        rarity="common",
        desc="Strong & sturdy, use wisely.",
        value=10
    )


#ENEMYS
def skeleton():
    return Enemy(
        name="Skeleton",
        damage=5,
        desc="Fragile, little glass cannon.",
        value=5,
        entrance = "Skeleton shoves in.",
        experience = 5,
        health = 2,
    )

#RACES
RACE_REGISTRY = {
    "3": Dwarf,
    "2": Elf,
    "1": Human
}

ITEM_REGISTRY = {
    "iron_sword": iron_sword
}

ENEMY_REGISTRY = {
    "skeleton": skeleton
}

