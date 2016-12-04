input = """""".splitlines()
import operator
import string
valid_sum = 0
for line in input:
    parts = line.split('-')
    checksum = parts[len(parts)-1]
    new_line = []
    letter_count = {}
    potential_checksum = ''
    for part in parts[:len(parts)-1]:
        new_line += part
    unique_letters = set(new_line)
    for letter in unique_letters:
        letter_count[letter] = new_line.count(letter)
    sorted_line = sorted(letter_count.items(), key=lambda (k, v): (-v, k))
    for l in sorted_line[:5]:
        potential_checksum += l[0]
    if potential_checksum == checksum[4:-1]:
        valid_sum += int(checksum[:-7])
        valid_checksum_rotation = int(checksum[:-7]) % 26
        new_string = ''
        for char in line[:-11]:
            if char != '-':
                position = string.ascii_lowercase.index(char) + valid_checksum_rotation - 26
                new_string += string.ascii_lowercase[position]
            else:
                new_string += ' '
        if 'northpole object storage' in new_string:
            print new_string, int(checksum[:-7])
print valid_sum
