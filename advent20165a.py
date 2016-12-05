import md5
input = 'uqwqemis'
input_to_hash = input
i = 0
found_eight = False
code = []
while not found_eight:
	m = md5.new()
	m.update(input_to_hash)
	hash = m.hexdigest()
	if hash[:5] == '00000':
		code += hash[5]
		print hash[5]
		if len(code) == 8:
			found_eight = True
	i += 1
	input_to_hash = input + str(i)