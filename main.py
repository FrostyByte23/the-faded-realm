import pygame
from world import World
from game import Game
from frontend import Frontend

def main():
    world = World()
    game = Game()
    frontend = Frontend(game)
    frontend.run()

if __name__ == "__main__":
    main()