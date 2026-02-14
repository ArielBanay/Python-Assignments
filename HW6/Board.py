from Cell import Cell
class Board:

    def __init__(self, board_width=5, board_height=5, snakes_ladders= {'L':{3:9, 5:11, 6:24},'S':{20:4, 16:2, 18:10}}):
        if type(board_width) != int:
            raise TypeError(f'{board_width} is not int.')
        elif type(board_height) != int:
            raise TypeError(f'{board_height} is not int.')
        elif type(snakes_ladders) != dict:
            raise TypeError(f'{snakes_ladders} is not dict.')
        elif board_width < 5:
            raise ValueError(f'{board_width} supposed to be >=5.')
        elif board_height < board_width:
            raise ValueError(f'{board_height} supposed to be at least {board_width}.')
        self.__size = board_width * board_height
        if self.__check_SL(snakes_ladders):
            raise ValueError(f'{snakes_ladders} is invalid dict.')
        self.__grid = None
        for i in range(1, self.__size + 1):
            self.__add_cell(i)
        for types in snakes_ladders:
            for k in snakes_ladders[types]:
                temp = self.__get_cell(k)
                temp.cell_type = types
                leap = self.__get_cell(snakes_ladders[types][k])
                temp.update_leap(leap)
        self.__crnt = self.__grid
        self.height = board_height
        self.width = board_width

    def __get_cell(self,x): #private method
        cell = self.get_grid()
        while cell.position<x:
            cell = cell.next
        return cell

    def __add_cell(self,x): #private method
        new_cell = Cell(x)
        if not self.__grid:
            self.__grid = new_cell
        else:
            curnt = self.__grid
            while curnt.next:
                curnt = curnt.next
            curnt.update_next(new_cell) 

    def __check_SL(self,x): #Checks whether SNAKE_LADDERS is a valid dictionary, private method
        s = set()
        if x=={}:
            return True
        for i in ["S","L"]:
            if i not in x.keys():
                return True
            elif x[i]=={}:
                return True
            for k,v in x[i].items():
                if type(k)!=int or type(v)!=int:
                    return True
                elif k > len(self) or v > len(self):
                    return True
                elif k in s or v in s:
                    return True
                s.add(k)
                s.add(v)

    def __iter__(self):
        self.__crnt = self.__grid
        return self

    def __next__(self):
        if self.__crnt is None:
            raise StopIteration
        temp = self.__crnt
        self.__crnt = self.__crnt.next
        return temp

    def __repr__(self):
        board_repr = ""
        ladder_snake_positions = {}  # Dictionary to map ladders and snakes to their destinations

        # Collect ladder and snake positions
        for cell in self:
            if cell.cell_type in {"L", "S"}:
                ladder_snake_positions[cell.position] = (
                    cell.leap.position,
                    cell.cell_type,
                )

        for row in range(self.height):
            row_repr = ""
            for col in range(self.width):
                cell_num = row * self.width + col + 1
                if cell_num in ladder_snake_positions:
                    target, cell_type = ladder_snake_positions[cell_num]
                    if cell_type == "L":
                        row_repr += f"[L{cell_num:02d}->{target:02d}]"
                    elif cell_type == "S":
                        row_repr += f"[S{cell_num:02d}->{target:02d}]"
                else:
                    row_repr += f"[{cell_num:02d}]"
            board_repr = row_repr + "\n" + board_repr  # Reverse row order to mimic game style
        return board_repr

    def get_grid(self):
        return self.__grid

    def __len__(self):
        return self.__size

