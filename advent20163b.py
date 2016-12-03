triangles = """
""".splitlines()
valid = []
for i in range(3, len(triangles) + 3, 3):
    sides = triangles[i-3:i]
    a, b, c = [], [], []
    for side in sides:
        split_side = filter(None, side.split(' '))
        a.append(split_side[0])
        b.append(split_side[1])
        c.append(split_side[2])
    for t in [a, b, c]:
        triangle = sorted(map(int, t))
        if sum(triangle[:2]) > triangle[2]:
            valid.append(triangle)
print len(valid)
