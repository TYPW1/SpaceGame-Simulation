class BoardCell:
    """Represents a cell on the board with special properties."""
    def __init__(self, name, special_effect=None):
        self.name = name
        self.special_effect = special_effect

# Define a simple circular board with some special cells
def create_board(size=20):
    board = []
    for i in range(size):
        if i % 5 == 0:
            board.append(BoardCell("Asteroid Field"))
        elif i % 7 == 0:
            board.append(BoardCell("Space Station"))
        else:
            board.append(BoardCell("Normal Space"))
    return board

# Create a sample board
board = create_board()
board[:5]  # Display the first 5 cells as a sample
