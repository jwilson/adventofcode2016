# """The first floor contains a strontium generator, a strontium-compatible microchip, a plutonium generator, and a plutonium-compatible microchip.
# The second floor contains a thulium generator, a ruthenium generator, a ruthenium-compatible microchip, a curium generator, and a curium-compatible microchip.
# The third floor contains a thulium-compatible microchip.
# The fourth floor contains nothing relevant."""


current_floor = None

floors = [
	[0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
	[0,  0,  0,  0,  0, -4,  0,  0,  0,  0],
	[0,  0,  0,  0,  4,  0,  8, -8, 16,-16],
	[1, -1,  2, -2,  0,  0,  0,  0,  0,  0]
]
floors.reverse()


def sum_of_pair(floor, pair):
	the_pair = floor[pair * 2:(pair * 2) + 2]
	return sum(the_pair), the_pair


def use_elevator(d, f):
	n = len(floors) - 1 \
		if floors.index(f) + d >= len(floors) \
		else floors.index(f) + d
	n = 0 if n < 0 else n
	return floors[n]


def irradiate_chips(floor):
	for pair in range(0, len(floor) / 2):
		the_sum, the_pair = sum_of_pair(floor, pair)
		print the_sum, the_pair


def play():
	moves = 0
	current_floor = floors[0]
	while not winning():
		current_floor = use_elevator(1, current_floor)
		irradiate_chips(current_floor)
		break


def winning():
	win = True
	for floor in floors:
		win = True if sum(floor) == 0 and win != False else False
	return win


play()
