from Cell import Cell
from Board import Board
from Dice import Dice

class Player:
    def __init__(self, name, board):
        if not isinstance(board,Board):
            raise TypeError(f'{board} type is not Board.')
        elif type(name)!=str:
            raise TypeError(f'{name} rype is not Str.')
        elif len(name)==0:
            raise ValueError(f'{name} must contain at least 1 char.')
        elif not name.isalpha():
            raise ValueError(f'{name} contain invalid char.')
        self.__name = name
        self._position = None #cell type
        self.__board = board
        self._num_turns = 0

    def move(self, roll):
        if type(roll)!=int:
            raise TypeError(f'{roll} type is not int.')
        elif roll>6 or roll<1:
            raise ValueError(f'{roll} should be in range 1-6.')
        self._num_turns += 1
        if self._position is None: # first turn
            self._position = self.__board.get_grid()
            for i in range(roll-1):
                if self._position.next:
                    self._position = self._position.next
                else:
                    break
        else: # regular turn
            for i in range(roll):
                if self._position.next:
                    self._position = self._position.next
                else:
                    break
        if self._position.cell_type in ["L", "S"]:
            self._position = self._position.leap
        elif self._position.position == len(self.__board):
            return True
        return False

    def __repr__(self):
        return f'Player(name={self.__name}, position={self._position})'
