from Player import Player
from Board import Board
from Dice import Dice
b = Board(board_width=5, board_height=5)
player1 = Player(name="Player", board=b)
d = Dice()
while True:
    c = d.roll()
    print(c)
    if not player1.move(c):
        print(player1)
    else:
        print(player1)
        break