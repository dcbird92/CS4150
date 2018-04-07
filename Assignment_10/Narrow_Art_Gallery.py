values = []
N = 0
cache = []


def max_value(r: int, uncloseable_room: int, k: int):
    global values
    global N
    global cache
    imax = 0
    if r >= N:
        return imax
    if k == 0:
        imax = values[r][0] + values[r][1] + max_value(r+1, -1, k)
        return imax
    if k < 0:
        return imax
    if cache[r][uncloseable_room + 1][k - 1] != 0:
        return cache[r][uncloseable_room + 1][k - 1]
    if k < N - r:
        if uncloseable_room == -1:
            imax = max((values[r][0]+max_value(r+1, 0, k-1)), (values[r][1]+max_value(r+1, 1, k-1)),
                       (values[r][0]+values[r][1] + max_value(r+1, -1, k)))
            cache[r][0][k - 1] = imax
        elif uncloseable_room == 0:
            imax = max((values[r][0] + max_value(r+1, 0, k-1)), (values[r][0] + values[r][1] + max_value(r+1, -1, k)))
            cache[r][1][k - 1] = imax
        else:  # uncloseable_room == 1
            imax = max((values[r][1] + max_value(r+1, 1, k-1)), (values[r][0] + values[r][1] + max_value(r+1, -1, k)))
            cache[r][2][k - 1] = imax
    elif k == N - r:
        if uncloseable_room == -1:
            imax = max((values[r][0] + max_value(r+1, 0, k-1)), (values[r][1] + max_value(r+1, 1, k-1)))
            cache[r][0][k - 1] = imax
        elif uncloseable_room == 0:
            imax = values[r][0] + max_value(r+1, 0, k-1)
            cache[r][1][k - 1] = imax
        else:
            imax = values[r][1] + max_value(r+1, 1, k-1)
            cache[r][2][k - 1] = imax
    return imax


def main():
    rows, closed = map(int, input().split(" "))
    global values
    global N
    global cache
    # create the gallery table 2 x rows
    values = [[0 for x in range(2)] for y in range(rows + 1)]
    cache = [[[0 for x in range(closed)] for y in range(3)]for m in range(rows)]
    N = rows
    i = 0
    while i < rows:
        values[i][0], values[i][1] = map(int, input().split(" "))
        i += 1
    print(max_value(0, -1, closed))
    return


if __name__ == "__main__":
    main()