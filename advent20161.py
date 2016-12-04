turns = ''
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
        dis = int(turn[1:])
        (xp, yp), (xf, yf) = point, facing
        if turn[0] == 'R':
            yf, xf = rotate(yf, xf)
        else:
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
