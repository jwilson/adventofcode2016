import md5
import string
input = 'uqwqemis'
input_to_hash = input
i = 0
found_eight = False
code = {}
while not found_eight:
	m = md5.new()
	m.update(input_to_hash)
	hash = m.hexdigest()
	if hash[:5] == '00000' and hash[5] not in ['a','b','c','d','e']:
		if int(hash[5]) < 8:
			if int(hash[5]) not in code.keys():
				code[int(hash[5])] = hash[6]
				print hash[5], hash[6]
			if len(code.keys()) == 8:
				found_eight = True
	i += 1
	input_to_hash = input + str(i)
print code