class Player:
    """General class for a player in the game."""
    def __init__(self, role):
        self.role = role
        self.cards = []  # Cards held by the player

class Captain(Player):
    """Represents the Captain role with specific abilities."""
    def __init__(self):
        super().__init__("Captain")

class Mechanic(Player):
    """Represents the Mechanic role with specific abilities."""
    def __init__(self):
        super().__init__("Mechanic")

class Scientist(Player):
    """Represents the Scientist role with specific abilities."""
    def __init__(self):
        super().__init__("Scientist")

class Medic(Player):
    """Represents the Medic role with specific abilities."""
    def __init__(self):
        super().__init__("Medic")

# Example of creating one player of each role
captain = Captain()
mechanic = Mechanic()
scientist = Scientist()
medic = Medic()

(captain.role, mechanic.role, scientist.role, medic.role)  # Display roles of the created players
