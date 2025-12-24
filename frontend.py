import pygame
import os

class Frontend:
    def __init__(self, game):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("The Faded Realm")
        
        # Set window icon
        try:
            # Try to load the icon from the game directory
            icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'icon.jpg')
            if os.path.exists(icon_path):
                icon = pygame.image.load(icon_path)
                pygame.display.set_icon(icon)
        except Exception as e:
            print(f"Could not load window icon: {e}")
        self.clock = pygame.time.Clock()
        self.game = game
        self.running = True

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.game.move_player(0,-1)
                elif event.key == pygame.K_DOWN:
                    self.game.move_player(0,1)
                elif event.key == pygame.K_LEFT:
                    self.game.move_player(-1,0)
                elif event.key == pygame.K_RIGHT:
                    self.game.move_player(1,0)

    def run(self):
        while self.running:
            self.handle_input()
            self.draw()
            self.clock.tick(60)