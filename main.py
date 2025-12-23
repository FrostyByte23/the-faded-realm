import pygame
from game import Game
from player import Player
from race import Human, Elf, Dwarf
from registry import RACE_REGISTRY
player = Player()
game = Game()

print("Welcome! Would you like to continue a game or start a new one?")
#Starting
#Start Loop
while True:
    opening_save = input("[Continue or Start] ").lower()
    if opening_save == "start":
        print("Starting...")
        break
    elif opening_save == "continue":
        print("Not available yet :/")
        pass
    else:
        print("Invalid choice. Please try again.")
        pass
#Race Loop
while True:
    choice = game.input_dialogue("Which race would you like?", [
        "Human",
        "Elf",
        "Dwarf"
    ])
    if choice in RACE_REGISTRY:
        player.race = RACE_REGISTRY[choice]()
        player.race.passive(player)
        print("You chose " + player.race.name + "!")
        break
    else:
        print("Invalid choice. Please try again.")
        pass
#Story Start
print("[Shimmerdrift Village, The Faded Realm, 1073]")
#Shimmerdrift Main Loop
while True:
    print("What would you like to do?")
    shimmer_choice = game.input_dialogue("What would you like to do?", [
        "Go to the shop,",
        "Go to the bar,",
        "View stats"
    ])
    if shimmer_choice == "1":
        #Shop loop
        if not player.name:
            print("Shopkeeper:")
            input_name = input("    Welcome! What should I call you? ").title()
            player.name = input_name
            game.dialogue("Shopkeeper:", [
                f"Welcome {player.name}!",
        ])
        while True:
            shop_choice = game.input_dialogue("What would you like to do?", ["Buy", "Sell", "Leave"])
            if shop_choice == "3":
                game.dialogue("Shopkeeper", [
                    "Goodbye,"
                    "Come back soon!"
                ])
                break

    if shimmer_choice == "3":
        player.display_stats()