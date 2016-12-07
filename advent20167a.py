input="""""".splitlines()
import re
correct = 0
for line in input:
	not_in_brackets = re.split('\[\w+\]', line)
	in_brackets = re.findall('\[\w+\]', line)
	keep_going = True
	for chunk in in_brackets:
		if len(chunk) > 5:
			for i in range(0, len(chunk)):
				if chunk[i:i+2][::-1] == chunk[i+2:i+4]:
					keep_going = False
	if not keep_going:
		continue
	for chunk in not_in_brackets:
		for i in range(0, len(chunk)):
			if chunk[i:i+2][::-1] == chunk[i+2:i+4] and chunk[i:i+2] != chunk[i+2:i+4]:
				correct += 1
				keep_going = False
				break
		if not keep_going:
			break
print correct