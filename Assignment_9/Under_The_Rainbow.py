import math
import sys
sys.setrecursionlimit(2000)
distance = []
cache = {}


def main():
    count = int(input())
    global distance
    distance = []
    global cache
    cache = {}
    x = 0
    while x < count + 1:
        distance.append(int(input()))
        x += 1
    penalty(count, 0)
    print(cache[0])


def penalty(hotels: int, loc: int):
    global distance
    global cache
    if loc == hotels:
        cache[loc] = 0
        return 0
    if loc in cache:
        return cache[loc]
    i = loc
    minimum = math.inf
    k = i + 1
    while k <= hotels:
        minimum = min((((400 - (distance[k] - distance[i]))*(400 - (distance[k] - distance[i]))) + penalty(hotels, k)), minimum)
        k += 1
    cache[i] = minimum
    return minimum


if __name__ == "__main__":
    main()