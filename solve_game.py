from commands_matrix import CommandsMatrix

class GameSolver():
    solution = []
    solver_matrix = []
    def __init__(self, size: int) -> None:
        self.commands_matrix = CommandsMatrix(size).data
        # self.board_state = 

    def get_solution(self, board):
        self.append_board_to_commands(board)
        self.down_pivet_norm()
        self.update_solution_from_normalized_solver()
        return self.solution

    def append_board_to_commands(self, board):
        self.solver_matrix = list(map(lambda r, l: r + [l], self.commands_matrix, board))

    def down_pivet_norm(self):
        for i, row in enumerate(self.solver_matrix):
            pivet = self.find_pivet_in_row(i, row)
            self.delete_down(pivet)
        # return self.solver_matrix

    def update_solution_from_normalized_solver(self):
        tags = list(range(1, len(self.commands_matrix) + 1))
        self.solution = list(map(lambda x: x[-1], self.solver_matrix))
        ## usar variaveis para descrever o que esta acontecendo ou trocar in place?
        self.solution = list(map(lambda x, y: x * y , self.solution, tags))
        self.solution =  [button for button in self.solution if button]

    def find_pivet_in_row(self, row_index, row):
        if not self.solver_matrix[row_index][row_index]:
            self.swap_to_pivet(row_index)
        return (row_index, row_index)

    def delete_down(self, pivet):
        pivet_col = pivet[1]
        for i, row in enumerate(self.solver_matrix):
            if row[pivet_col] and pivet_col != i:
                self.solver_matrix[i] = list(map(lambda s, p: s ^ p, self.solver_matrix[i], self.solver_matrix[pivet_col]))
        # return self.solver_matrix

    def swap_to_pivet(self, row_index):
        for r in range(row_index + 1, len(self.solver_matrix)):
            if self.solver_matrix[r][row_index]:
                self.solver_matrix[row_index], self.solver_matrix[r] = self.solver_matrix[r], self.solver_matrix[row_index]
                break
