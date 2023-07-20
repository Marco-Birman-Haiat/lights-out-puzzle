def create_commands_matrix(side: int):
	matrix = [[0 for i in range(side**2)] for j in range(side**2)]

	for i in range(side**2):
		for j in range(side**2):
			if i == j:
				matrix[i][j] = 1
			if is_line_ad(i, j, side) or is_col_ad(i, j, side):
				matrix[i][j] = 1
	
	return matrix


def is_line_ad(i, j, side):
	sides = is_in_side(i, side)
	if sides and sides[1] == 'l':
		return j - i == 1
	elif sides and sides[1] == 'r':
		return i - j == 1
	else:
		return abs(j - i) == 1


def is_col_ad(i, j, side):
	sides = is_in_side(i, side)
	if sides and sides[1] == 't':
		return j - side == i
	elif sides and sides[1] == 'b':
		return j + side == i
	else:
		return j - side == i or j + side == i


def is_in_side(i, side):
	top = (0 < i < side - 1, 't')
	left = (i % side == 0, 'l')
	right = (i % side == side - 1, 'r')
	bottom = (side**2 - side < i < side**2 - 1, 'b')

	sides = [top, left, right, bottom]
	sides = list(filter(lambda x: x[0], sides))

	return sides[0] if sides else False


if __name__ == '__main__':
	[print(row) for row in create_commands_matrix(3)]
