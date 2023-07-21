import math
from commands_matrix import CommandsMatrix


class Board:
    def __init__(self, size: int) -> None:
        self.lights = [1 for _ in range(size**2)]
        self.commands_matrix = CommandsMatrix(size).data
        self.side = size

    def apply_move(self, move: int) -> None:
        self.lights = list(map(lambda x, y: x ^ y, self.lights, self.commands_matrix[move-1]))

    def __len__(self):
        return len(self.lights)
    
    def __str__(self) -> str:
        print_array = []
        for l in self.lights:
            print_array.append(f' {l} |')
            self.side -= 1
            if not self.side:
                print_array.append('\n')
                self.side = math.sqrt(len(self.lights))
        return ''.join(print_array)


if __name__ == '__main__':
    print('testing board object')
    board = Board(3)
    print(board)