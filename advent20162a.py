digits = """
"""
actual_current = [(0,0)]
directions = {'L': -1, 'R': 1, 'U': 1, 'D': -1}
for digit in digits.splitlines():
	for d in digit:
		x, y = actual_current.pop()
		if d == 'D' and y > -1 or d == 'U' and y < 1:
			actual_current.append((x, y + directions[d]))
		elif d == 'L' and x > -1 or d == 'R' and x < 1:
			actual_current.append((x + directions[d], y))
		else:
			actual_current.append((x, y))
	print actual_current
