class Ship:
    """Represents the spaceship with health and position."""
    def __init__(self, initial_health=10, start_position=0):
        self.health = initial_health
        self.position = start_position

# Initialize the ship with default values
ship = Ship()

(ship.health, ship.position)  # Display the ship's initial health and position
#test coment