input = """""".splitlines()
import string
columns = []
for col in range(0,8):
	column = {}
	for letter in string.ascii_lowercase:
		column[letter] = 0
	columns.append(column)
for line in input:
	col = 0
	for c in line:
		columns[col][c] += 1
		col += 1
for column in columns:
	print sorted(column.items(), key=lambda (k, v): (-v, k), reverse=True)[0]