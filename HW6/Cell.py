from CellUpdateError import CellUpdateError


class Cell():
    def __init__(self, position, cell_type="R"):
        if type(position)!=int:
            raise TypeError(f"{position} is not int.")
        elif position<=0:
            raise ValueError(f"position = {position} is smaller than 0.")
        elif type(cell_type)!=str:
            raise TypeError(f"{cell_type} is not str.")
        elif cell_type not in ["R","L","S"]:
            raise ValueError(f"{cell_type} is not in ['R','L','S'].")
        self.position = position
        self.cell_type = cell_type
        self.next = None
        self.leap = None

    def update_next(self, next_cell):
        if self.next is not None:
            raise CellUpdateError(f'A value already exists in this field. It cannot be reset.')
        elif not isinstance(next_cell,Cell):
            raise CellUpdateError(f'"next_cell" is not instance of cell.')
        elif self.position != next_cell.position-1:
            raise ValueError(f"{next_cell} is not the next one.")
        self.next = next_cell

    def update_leap(self, leap):
        if self.leap is not None:
            raise CellUpdateError(f'A value already exists in this field. It cannot be reset.')
        elif self.cell_type == "R":
            raise CellUpdateError(f'The current cell is "R" type.')
        elif not isinstance(leap,Cell):
            raise CellUpdateError(f'leap is not instance of cell.')
        elif self.cell_type == "L" and leap.position < self.position:
            raise ValueError(f'leap position supposed to be greater than {self.position}.')
        elif self.cell_type == "S" and leap.position > self.position:
            raise ValueError(f'leap position supposed to be smaller than {self.position}.')
        elif leap.cell_type!= "R":
            raise CellUpdateError(f'leap is not "R" type.')
        elif self.cell_type == "L" and leap.position > self.position:
            self.leap = leap
        elif self.cell_type == "S" and leap.position < self.position:
            self.leap = leap

    def __repr__(self):
        if self.cell_type == "R":
            return f'{self.position}:{self.cell_type}->'
        else:
            return f'{self.position}:{self.cell_type}->{self.leap.position}'


