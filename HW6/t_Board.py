from Board import Board
snakes_ladders = {
    'L': {5: 12, 3: 11, 6: 21},  # Ladders: position 3 -> 9, 5 -> 11, 6 -> 24
    'S': {19: 4, 20: 2, 18: 10}  # Snakes: position 20 -> 4, 16 -> 2, 18 -> 10
}
board_width = 5
board_height = 5

# Create the board
board = Board(board_width=board_width, board_height=board_height, snakes_ladders=snakes_ladders)
print("Game Board Representation:\n")
print(board)

# Iterate through the board cells and print details
print("\nDetailed Cell Information:\n")
for cell in board:
    print(f"Cell Position: {cell.position}")
    print(f"  Cell Type: {cell.cell_type}")
    if cell.leap:
        leap_type = "Ladder" if cell.cell_type == "L" else "Snake"
        print(f"  {leap_type} Leap: {cell.position} -> {cell.leap.position}")
    print("")


print("Iterating over Board...")
for i in board:
    print(i)

# Example: Interactively traversing the board
print("\nSimulating a Game Move with default board:\n")
board = Board()
current_cell = board.get_grid()
print(f"Starting at cell {current_cell.position}")

while current_cell.next and not current_cell.leap:
    current_cell = current_cell.next
    print(f"Moved to cell {current_cell.position}")

if current_cell.leap:
    leap_target = current_cell.leap.position
    cell_type = "Ladder" if current_cell.cell_type == "L" else "Snake"
    print(f"Landed on a {cell_type} at cell {current_cell.position}! Moving to cell {leap_target}.")
    current_cell = current_cell.leap

print(f"Final position we landed on: Cell {current_cell.position}")


try:
    failed_board = Board(5, 5, {"L": {5:3}, "S": {19: 4, 20: 2, 18: 10}})
except Exception as e:
    print(e)

try:
    failed_board = Board(5, 5, {"L": {5:20, 7:13}, "S": {19: 21, 20: 2, 18: 10}})
except Exception as e:
    print(e)

try:
    failed_board = Board(5, 5, {"L": {5:4}, "S": {19: 4, 20: 2, 18: 10}})
except Exception as e:
    print(e)