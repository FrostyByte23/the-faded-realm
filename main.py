import pygame
from game import Game
from frontend import Frontend

def main():
    game = Game()
    frontend = Frontend(game)
    frontend.run()

if __name__ == "__main__":
    main()