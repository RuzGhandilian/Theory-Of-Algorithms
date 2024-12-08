# Jarvis March
def orientation(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])


def convex_hull(points):
    if len(points) < 3:
        return points
    hull = []
    leftmost = min(range(len(points)), key=lambda i: points[i][0])
    p = leftmost
    while True:
        hull.append(points[p])
        q = (p + 1) % len(points)
        for i in range(len(points)):
            if orientation(points[p], points[i], points[q]) < 0:
                q = i
        p = q
        if p == leftmost:
            break
    return hull


points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
hull = convex_hull(points)
print(hull)
