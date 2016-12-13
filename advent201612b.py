input = """""".splitlines()
import string
registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
keep_processing = True
i = 0
while keep_processing:
    instruction = filter(None, input[i].split(' '))
    command = instruction[0]
    value = instruction[1]
    if command == 'cpy':
        register = instruction[2]
        if value in string.ascii_lowercase:
            registers[register] = registers[value]
        else:
            registers[register] = int(value)
        i += 1
    elif command == 'inc':
        registers[value] += 1
        i += 1
    elif command == 'dec':
        registers[value] -= 1
        i += 1
    elif command == 'jnz':
        if value in string.ascii_lowercase:
            value_to_check = registers[value]
        else:
            value_to_check = int(value)
        print instruction, value_to_check
        if value_to_check > 0:
            i += int(instruction[2])
        else:
            i += 1
    if i >= len(input):
        keep_processing = False
print registers['a']
