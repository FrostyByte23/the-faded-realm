import pygame
class Frontend:
    def __init__(self, game):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("The Faded Realm")
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