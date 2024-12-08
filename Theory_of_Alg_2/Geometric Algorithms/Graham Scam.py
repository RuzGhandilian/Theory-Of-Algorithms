def orientation(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])


def distance(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


def convex_hull(points):
    if len(points) < 3:
        return points
    points = sorted(points, key=lambda p: (p[1], p[0]))
    p0 = points[0]
    sorted_points = sorted(points[1:], key=lambda p: (orientation(p0, p, (p0[0] + 1, p0[1])), -distance(p0, p)))
    hull = [p0, sorted_points[0]]
    for p in sorted_points[1:]:
        while len(hull) > 1 and orientation(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    return hull


points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
hull = convex_hull(points)
print(hull)
