from ADTs import MyQueue
from Board import Board
from Dice import Dice
from Player import Player


class Game:
    def __init__(self, board_width, board_height, snakes_ladders, game_players = ["Omri", "Tal"]):
        try:
            self.__board = Board(board_width,board_height,snakes_ladders)
            if len(game_players)<2:
                raise Exception
            self.__players = [Player(i,self.__board) for i in game_players]
        except:
            self.__board = Board()
            self.__players = [Player(i, self.__board) for i in ["Omri", "Tal"]]
        self.__dice = Dice()
        self.__winner = None
        self.__forbidden = {}

    def play_turn(self):
        for i in self.__players:
            if i.move(self.__dice.roll()):
                self.__winner = i
                print(f'The winner is {i}')
                break
            elif i._position in self.__forbidden.values():
                pts=[k for k,v in self.__forbidden.items() if v == i._position][0]
                pts.position = None #Returns the player to the beginning of the game
                self.__forbidden[i]=i._position
            self.__forbidden[i] = i._position
        print(self.__forbidden.keys())

    def run_game(self):
        while self.__winner is None:
            self.play_turn()
        return tuple[self.__winner,self.__winner._num_turns]

    def solve(self):
        f_c = self.__board.get_grid()
        p_dict = {}
        visit = set()
        q = MyQueue()
        q.enqueue((f_c,[f_c.position]))
        last = len(self.__board)
        while not q.is_empty() and last not in p_dict.keys():
            curnt,path = q.dequeue()
            if curnt in visit:
                continue
            visit.add(curnt)
            p_dict[curnt.position]=path

            if curnt.next is not None and curnt.next not in visit:
                q.enqueue((curnt.next, path + [curnt.next.position]))
            if curnt.leap is not None and curnt.leap not in visit:
                q.enqueue((curnt.leap, path + [curnt.leap.position]))
        return p_dict[last]

    def __repr__(self):
        return f"Game(players={self.__players},\nboard={self.__board}\n****winner={self.__winner if self.__winner else 'game is still going on….'}****)"


    

        
