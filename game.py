from solve_game import GameSolver
from board import Board

class Game:
    solution = 0
    finished = False
    automatic_mode = False

    def __init__(self, size) -> None:
        self.size = size
        self.board = Board(size)

    def start(self):
        self.greet()
        print(self.board)

        while not self.finished:
            if self.solution:
                if input('Activate automatic Mode?') == 'y':
                    self.activate_automatic_mode()
                    break
            self.game_round()
            self.finished = self.is_game_finished()
        
        self.finish()
        
    def game_round(self):
        if self.solution:
            self.get_and_show_solution()
        else:
            self.ask_about_solution()    
        move = self.get_next_move()
        self.board.apply_move(move)
        print(self.board)

    def activate_automatic_mode(self):
        for move in self.solution:
            self.get_and_show_solution()
            input(f'press any key to iterate with move {move}')
            self.board.apply_move(move)
            print(self.board)
    
    def ask_about_solution(self):
        if input('Want to see the solution? (y):') == 'y':
            self.get_and_show_solution()
    
    def get_and_show_solution(self):
        solver = GameSolver(self.size)
        self.solution = solver.get_solution(self.board.lights)
        print(self.solution)

    def is_game_finished(self):
        return not any(self.board.lights)

    def get_next_move(self) -> int:
        next_move = input(f'input a number from 1 to {len(self.board)}: ')
        return int(next_move)        

    def greet(self):
        print(f'game initialized with a board of size {self.size}')

    def finish(self):
        print('Congratulations!!! Geniouss')