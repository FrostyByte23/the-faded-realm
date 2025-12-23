class Race:
    name = "unknown"

    def passive(self, player):
        pass

    def on_attack(self,player,target):
        pass

    def on_turn(self, player):
        pass

    def on_battle_end(self,player):
        pass

class Human(Race):
    name = "Human"

    def passive(self, player):
        pass

    def on_attack(self,player,target):
        pass

    def on_turn(self, player):
        pass

    def on_battle_end(self,player):
        pass

class Elf(Race):
    name = "Elf"

    def passive(self,player):
        player.attack += 2
        player.dodge += 5
        player.defense -= 2

    def on_attack(self,player,target):
        pass

    def on_turn(self,player):
        pass

    def on_battle_end(self,player):
        pass

class Dwarf(Race):
    name = "Dwarf"

    def passive(self,player):
        player.defense += 3
        player.max_health += 10
        player.health = player.max_health
        player.magical_power -= 999

    def on_attack(self,player,target):
        pass

    def on_turn(self,player):
        pass

    def on_battle_end(self,player):
        pass
