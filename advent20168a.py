input = """""".splitlines()
def shift_list(row, offset):
    new_row = []
    for i in range(0, len(row)):
        new_row.append(0)
    for i in reversed(range(0, len(row))):
        new_row[i] = row[i-offset]
    return new_row
screen = []
for i in range(0, 6):
    row = []
    for i in range(0, 50):
        row.append(0)
    screen.append(row)
for line in input:
    instructions = line.split(' ')
    instruction = instructions[0]
    if instruction == 'rect':
        coords = instructions[1].split('x')
        for y in range(0, int(coords[1])):
            for x in range(0, int(coords[0])):
                screen[y][x] = 1
    elif instruction == 'rotate':
        method = instructions[1]
        direction = instructions[2].split('=')
        actual_direction = direction[0]
        actual_row_or_column = direction[1]
        amount = int(instructions[4])
        if method == 'row':
            row = screen[int(actual_row_or_column)]
            screen[int(actual_row_or_column)] = shift_list(row, amount)
        elif method == 'column':
            column = []
            actual_int = int(actual_row_or_column)
            for i in range(0, len(screen)):
                column.append(screen[i][actual_int])
            new_column = shift_list(column, amount)
            for i in range(0, len(screen)):
                screen[i][actual_int] = new_column[i]
num_lit = 0
for row in screen:
    num_lit += sum(row)
print num_lit
