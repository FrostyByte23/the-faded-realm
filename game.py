from player import Player
from world import World

class Game:
    def __init__(self):
        self.player = Player()
        self.world = World()
        self.flags = {}
        self.variables = {}

    def move_player(self, dx, dy):
        """
        Move the player in the game world
        
        Args:
            dx (int): Change in x-coordinate
            dy (int): Change in y-coordinate
            
        Returns:
            tuple: The new position (x, y)
        """
        return self.world.move_player(dx, dy)

    def get_player_stats(self):
        """Return player stats as a dictionary for the frontend"""
        return {
            'name': self.player.name,
            'race': self.player.race.name if hasattr(self.player, 'race') else 'Unknown',
            'health': self.player.health,
            'max_health': self.player.max_health,
            'level': self.player.level,
            'xp': self.player.xp,
            'gold': self.player.gold,
            'inventory': [str(item) for item in self.player.inventory],
            'position': self.world.current_location
        }