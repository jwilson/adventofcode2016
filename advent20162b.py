digits = []
actual_current = [(-2,0)]
directions = {'L': -1, 'R': 1, 'U': 1, 'D': -1}
for digit in digits:
	for d in digit:
		x, y = actual_current.pop()
		if x + y == 1 or x + y == -1:
			if d == 'L' or d == 'R':
				actual_current.append((x + directions[d], y))
			elif d == 'D' or d == 'U':
				actual_current.append((x, y + directions[d]))
			else:
				actual_current.append((x, y))
		elif x == -2:
			if d == 'R':
				actual_current.append((x + 1, y))
			else:
				actual_current.append((x, y))
		elif x == 2:
			if d == 'L':
				actual_current.append((x - 1, y))
			else:
				actual_current.append((x, y))
		elif y == -2:
			if d == 'U':
				actual_current.append((x, y + 1))
			else:
				actual_current.append((x, y))
		elif y == 2:
			if d == 'D':
				actual_current.append((x, y - 1))
			else:
				actual_current.append((x, y))
		else:
			if d == 'D' and y > -1 or d == 'U' and y < 1:
				actual_current.append((x, y + directions[d]))
			elif d == 'L' and x > -1 or d == 'R' and x < 1:
				actual_current.append((x + directions[d], y))
			else:
				actual_current.append((x, y))
	print actual_current
