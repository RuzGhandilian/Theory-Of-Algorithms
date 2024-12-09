def LineInt(p1, q1, p2, q2):
    if (Orientation(p1[0], p1[1], q1[0], q1[1], p2[0], p2[1]) !=
            Orientation(p1[0], p1[1], q1[0], q1[1], q2[0],q2[1]) and
            Orientation(p2[0], p2[1], q2[0], q2[1], p1[0], p1[1]) !=
            Orientation(p2[0], p2[1], q2[0], q2[1], q1[0], q1[1])):
        return True
    else:
        return False


def Orientation(x1, y1, x2, y2, x3, y3):
    if ((y2 - y1) * (x3 - x2) - (y3 - y2) * (x2 - x1)) > 0:
        return 1
    elif ((y2 - y1) * (x3 - x2) - (y3 - y2) * (x2 - x1)) < 0:
        return -1
    else:
        return 0


p1 = (1, 0)
q1 = (3, 1)
p2 = (3, 2)
q2 = (4, 5)
print(LineInt(p1, q1, p2, q2))
