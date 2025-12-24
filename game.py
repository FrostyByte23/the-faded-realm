from player import Player

class Game:
    def __init__(self):
        self.player = Player()
        self.flags = {}
        self.variables = {}
        self.current_location = (0, 0)  # Example position tracking

    def move_player(self, dx, dy):
        """Move the player by (dx, dy) in the game world"""
        self.current_location = (self.current_location[0] + dx, self.current_location[1] + dy)
        # Add any movement-related logic here

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
            'inventory': [str(item) for item in self.player.inventory]
        }