def solution(v):
    minx = min(v, key=lambda x: x[0])[0]
    maxx = max(v, key=lambda x: x[0])[0]
    miny = min(v, key=lambda x: x[1])[1]
    maxy = max(v, key=lambda x: x[1])[1]

    comparison = [[minx, miny], [minx, maxy], [maxx, miny], [maxx, maxy]]
    for c in comparison:
        if c not in v:
            return c
print(solution([[1, 4], [3, 4], [3, 10]]))