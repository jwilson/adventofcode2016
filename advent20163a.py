triangles = """
"""
valid = []
for triangle in triangles.splitlines():
    sides = sorted(map(int, filter(None, triangle.split(' '))))
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a + b > c:
        valid.append(sides)
print len(valid)
