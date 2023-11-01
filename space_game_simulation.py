import random

# Define the roles in the game
roles = ["Captain", "Mechanic", "Scientist", "Medic"]

# Game board setup
board_size = 20  # Number of cells in the circular board
special_cells = {"Asteroid Field": [3, 7, 12], "Space Station": [5, 10, 15]}  # Example positions

# Ship status
ship_health = 10  # Starting health of the ship
ship_position = 0  # Starting position

# Define the basic structure of the deck
hazard_cards = [
    {"name": "Air Leak", "effect": "lose_1_hp", "counter": ["Mechanic", "Scientist"]},
    {"name": "Cosmic Radiation", "effect": "discard_card", "counter": ["Scientist"]},
    # Add other hazard cards here
]

beneficial_cards = [
    {"name": "Engine Boost", "effect": "move_extra_space"},
    {"name": "Quick Fix", "effect": "restore_1_hp"},
    # Add other beneficial cards here
]






# Function to draw a hazard card
def draw_hazard_card():
    return random.choice(hazard_cards)

# Function to check if a player can counter the hazard
def can_counter_hazard(card, player_role):
    return player_role in card.get("counter", [])

# Function to move the ship
def move_ship():
    global ship_position
    ship_position = (ship_position + 1) % board_size
    print(f"Ship moved to position {ship_position}")

# Function to draw a card from the deck
def draw_card():
    deck = hazard_cards + beneficial_cards  # Combine both types of cards for simplicity
    return random.choice(deck)

# Function to apply the effect of the card
def apply_card_effect(card):
    global ship_health
    effect = card["effect"]

    if effect == "lose_1_hp":
        ship_health -= 1
        print(f"Effect: Ship loses 1 HP. Current health: {ship_health}")
    elif effect == "discard_card":
        # Placeholder for discarding a card
        print("Effect: Players discard a card (not yet implemented)")
    elif effect == "move_extra_space":
        move_ship()
        print("Effect: Ship moves an extra space")
    elif effect == "restore_1_hp":
        ship_health = min(ship_health + 1, 10)  # Assuming 10 is the max health
        print(f"Effect: Ship restores 1 HP. Current health: {ship_health}")
    # Add other effects as needed

# Function to simulate a turn with the correct order
def simulate_turn(player_roles):
    global ship_health
    print("\nStarting a new turn...")

    # Captain always draws a hazard card
    hazard_drawn = draw_hazard_card()
    print(f"Captain draws a hazard card: {hazard_drawn['name']}")

    # Other players attempt to resolve the hazard
    hazard_resolved = False
    for role in player_roles[1:]:  # Skip the captain
        if can_counter_hazard(hazard_drawn, role):
            print(f"{role} counters the hazard: {hazard_drawn['name']}")
            hazard_resolved = True
            break

    # Apply hazard effect if not resolved
    if not hazard_resolved:
        apply_card_effect(hazard_drawn)

    # Move the ship at the end of the turn
    move_ship()

# Main function to start the game simulation
def main():
    player_roles = ["Captain", "Mechanic", "Scientist", "Medic"]
    print("Starting the game with ship health:", ship_health)
    for _ in range(5):  # Simulate 5 turns for demonstration
        simulate_turn(player_roles)
        if ship_health <= 0:
            print("Game over: Ship destroyed.")
            break

# Entry point of the script
if __name__ == "__main__":
    main()
