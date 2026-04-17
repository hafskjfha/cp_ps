points = [tuple(map(int, input().split())) for _ in range(int(input()))]

def shoelace_area(poly):
    area = 0
    n=len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        area += (x1 * y2) - (x2 * y1)
    return abs(area) / 2

area = shoelace_area(points)
print(f"{area:.1f}")
