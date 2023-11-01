class Card:
    """Represents a card in the game with a specific effect."""
    def __init__(self, name, effect, counter, text):
        self.name = name
        self.effect = effect
        self.counter = counter
        self.text = text

# Sample cards definition
def create_deck():
    deck = [
        Card("Air Leak", "Ship loses 1 HP", "Mechanic or Scientist", "A hissing sound warns of escaping oxygen."),
        Card("Cosmic Radiation", "All players discard a card", "Scientist", "Dangerous radiation permeates the ship."),
        Card("Engine Malfunction", "Ship doesn't move this turn", "Mechanic", "The engines sputter and stall."),
        # ... Add more cards as needed
    ]
    return deck

# Create a sample deck
deck = create_deck()
deck[:3]  # Display the first 3 cards as a sample
