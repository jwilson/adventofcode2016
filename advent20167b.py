input="""""".splitlines()
import re
correct = 0
for line in input:
	not_in_brackets = re.split('\[\w+\]', line)
	in_brackets = re.findall('\[\w+\]', line)
	keep_going = True
	for chunk in not_in_brackets:
		for i in range(0, len(chunk)):
			if i < len(chunk) - 2 and chunk[i] == chunk[i+2] and chunk[i] != chunk[i+1]:
				aba = '{}{}{}'.format(chunk[i], chunk[i+1], chunk[i+2])
				bab = '{}{}{}'.format(chunk[i+1], chunk[i], chunk[i+1])
				for inner_chunk in in_brackets:
					if bab in inner_chunk:
						print aba, bab, inner_chunk
						correct += 1
						keep_going = False
						break
			if not keep_going:
				break
		if not keep_going:
			break
print correct