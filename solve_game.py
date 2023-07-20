import math
from commands_matrix import create_commands_matrix
from utils import binary_digit_sum


def find_pivet_in_row(row_index, row):
    return (row_index, row_index)

def delet_down(pivet, matrix):
    pivet_col = pivet[1]
    for i, row in enumerate(matrix):
        if row[pivet_col] and pivet_col != i:
            matrix[i] = list(map(lambda s, p: binary_digit_sum(s, p), matrix[i], matrix[pivet_col]))
    return matrix

def swap_to_pivet(matrix, row_index):
    for r in range(row_index + 1, len(matrix)):
        if matrix[r][row_index]:
            matrix[row_index], matrix[r] = matrix[r], matrix[row_index]
            break
    return matrix

def down_pivet_norm(matrix):
    for i, row in enumerate(matrix):
        pivet = find_pivet_in_row(i, row)
        if not matrix[pivet[0]][pivet[0]]:
            matrix = swap_to_pivet(matrix, i)
        delet_down(pivet, matrix)
    return matrix

def reduce_matrix(matrix):
    matrix = down_pivet_norm(matrix)
    return matrix
    


def is_solved(matrix):
    for ri, r in enumerate(matrix):
        for ci, c in enumerate(r):
          if ri == ci and not matrix[ri][ci]:
              return False
          elif ci < len(matrix) - 1 and matrix[ri][ci]:
              return False
    return True

def solve_game(lights):
    side = int(math.sqrt(len(lights)))
    effects_matrix = create_commands_matrix(side)

    sm = list(map(lambda r, l: r + [l], effects_matrix, lights))
    
    reduced_matrix = reduce_matrix(sm)
    answer = list(map(lambda x: x[-1], reduced_matrix))
    tags = list(range(1, len(lights) + 1))
    tag_answer = list(map(lambda x, y: x * y , answer, tags))
    return [button for button in tag_answer if button]
    
    # [print(row) for row in sm]
  


if __name__ == '__main__':
    l = [1 for _ in range(9)]
    solve_game(l)