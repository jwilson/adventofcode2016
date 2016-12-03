turns = 'L2, L5, L5, R5, L2, L4, R1, R1, L4, R2, R1, L1, L4, R1, L4, L4, R5, R3, R1, L1, R1, L5, L1, R5, L4, R2, L5, L3, L3, R3, L3, R4, R4, L2, L5, R1, R2, L2, L1, R3, R4, L193, R3, L5, R45, L1, R4, R79, L5, L5, R5, R1, L4, R3, R3, L4, R185, L5, L3, L1, R5, L2, R1, R3, R2, L3, L4, L2, R2, L3, L2, L2, L3, L5, R3, R4, L5, R1, R2, L2, R4, R3, L4, L3, L1, R3, R2, R1, R1, L3, R4, L5, R2, R1, R3, L3, L2, L2, R2, R1, R2, R3, L3, L3, R4, L4, R4, R4, R4, L3, L1, L2, R5, R2, R2, R2, L4, L3, L4, R4, L5, L4, R2, L4, L4, R4, R1, R5, L2, L4, L5, L3, L2, L4, L4, R3, L3, L4, R1, L2, R3, L2, R1, R2, R5, L4, L2, L1, L3, R2, R3, L2, L1, L5, L2, L1, R4'
def go(cross_paths=False):
    path = []
    def rotate(af, bf):
        if af == 1 or af == -1:
            bf = af
            af = 0
        elif bf == 1 or bf == -1:
            b = bf
            bf = af
            af = b * (-1)
        return af, bf
    point, facing = (0,0), (0, 1)
    for turn in turns.split(', '):
        way, dis = turn[0], int(turn[1:])
        (xp, yp), (xf, yf) = point, facing
        if way == 'R':
            yf, xf = rotate(yf, xf)
        elif way == 'L':
            xf, yf = rotate(xf, yf)
        if cross_paths:
            for _ in range(0, dis):
                xp += xf
                yp += yf
                if (xp,yp) not in path:
                    path.append((xp,yp))
                else:
                    return (xp,yp)
        else:
            xp += dis * xf
            yp += dis * yf
        point, facing = (xp, yp), (xf, yf)
    return point
print go(True)
