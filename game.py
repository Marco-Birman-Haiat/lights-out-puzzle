import math
from commands_matrix import create_commands_matrix
from utils import binary_digit_sum
from solve_game import solve_game

def print_board(lights):
    side = math.sqrt(len(lights))
    for l in lights:
        print(f' {l} |', end=' ')
        side -= 1
        if not side:
            print(' ')
            side = math.sqrt(len(lights))


def is_game_finished(lights):
    return not any(lights)


def game_matrix_operation(lights, move):
    side = int(math.sqrt(len(lights)))
    effects_matrix = create_commands_matrix(side)
    new_lights = map(lambda x, y: binary_digit_sum(x, y), lights, effects_matrix[move - 1])
    return list(new_lights)

def apply_move(lights, move):
    new_lights = game_matrix_operation(lights, move)
    return new_lights

def automatic_mode(lights, solution):
    for move in solution:
        input(f'press any key to iterate with move {move}')
        lights = apply_move(lights, move)
        print_board(lights)
      
    return lights

def game_init():
    print('Wellcome to Marcos lights out \n')
    size = int(input("I'll generate a game for you, choose a size: "))

    lights_array = [1 for _ in range(size**2)]
    print('\n Here is the starting board:\n')
    print_board(lights_array)

    solution = 0
    while not is_game_finished(lights_array):
        if not solution:
          if input('want the solution? (y/n):') == 'y':
            solution = solve_game(lights_array)
            print(f'The solution is: {solution}')
                
        else:
            solution = solve_game(lights_array)
            print(f'The solution is: {solution}')
            if input('automatic mode? (y/n):') == 'y':
                lights_array = automatic_mode(lights_array, solution)
                break

        move = input(f'\ndigite um movimento, de 1 a {len(lights_array)}: ')
        lights_array = apply_move(lights_array, int(move))
        print_board(lights_array)
            
    
    print('Congratulations!!! Geniouss')
    return


game_init()