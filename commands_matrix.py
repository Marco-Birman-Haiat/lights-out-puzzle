class CommandsMatrix():
    def __init__(self, size: int) -> None:
        self.data = [[0 for i in range(size**2)] for j in range(size**2)]
        self.size = size
        self.populate_commands_matrix()

    def populate_commands_matrix(self):
        for row_index in range(self.size**2):
            for col_index in range(self.size**2):
                if row_index == col_index:
                    self.data[row_index][col_index] = 1
                if (self.is_line_adjacent(row_index, col_index, self.size)
                    or self.is_col_adjacent(row_index, col_index, self.size)):
                    self.data[row_index][col_index] = 1

    def is_line_adjacent(self, row_index, col_index, side):
        sides = self.is_in_side(row_index, side)
        if sides and sides[1] == 'l':
            return col_index - row_index == 1
        elif sides and sides[1] == 'r':
            return row_index - col_index == 1
        else:
            return abs(col_index - row_index) == 1

    def is_col_adjacent(self, i, j, side):
        sides = self.is_in_side(i, side)
        if sides and sides[1] == 't':
            return j - side == i
        elif sides and sides[1] == 'b':
            return j + side == i
        else:
            return j - side == i or j + side == i

    def is_in_side(self, i, side):
        top = (0 < i < side - 1, 't')
        left = (i % side == 0, 'l')
        right = (i % side == side - 1, 'r')
        bottom = (side**2 - side < i < side**2 - 1, 'b')

        sides = [top, left, right, bottom]
        sides = list(filter(lambda x: x[0], sides))

        return sides[0] if sides else False
