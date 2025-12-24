
class World:
    def __init__(self):
        self.current_location = (0, 0)  # Tracks the player's position in the game world

    def move_player(self, dx, dy):
        """
        Move the player by (dx, dy) in the game world
        
        Args:
            dx (int): Change in x-coordinate
            dy (int): Change in y-coordinate
            
        Returns:
            tuple: The new position (x, y)
        """
        self.current_location = (self.current_location[0] + dx, self.current_location[1] + dy)
        return self.current_location

