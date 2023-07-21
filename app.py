from game import Game

print("Wellcome to Marco's lights out\n")

command = input("If you want to enter a game, just type the side of the grid:\n")

game = Game(int(command))

game.start()
