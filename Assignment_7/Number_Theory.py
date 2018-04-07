import sys


def gcd(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a


def exp(x: int, y: int, n: int):
    if y == 0:
        return 1
    z = exp(x, y//2, n)
    if y % 2 == 0:
        return (z * z) % n
    else:
        return (((z * z) % n) * x) % n


def inverse(a: int, n: int):
    x, y, d = ee(a, n)
    if d != 1:
        return "none"
    return x % n


def is_prime(p: int):
    if exp(2, p-1, p) != 1:
        return "no"
    elif exp(3, p-1, p) != 1:
        return "no"
    elif exp(5, p-1, p) != 1:
        return "no"
    return "yes"


def key(p: int, q: int):
    n = p*q
    phi = (p-1)*(q-1)
    e = 2
    while gcd(phi, e) != 1:
        e += 1
    d = inverse(e, phi)
    print(n, e, d)


def ee(a: int, b: int):
    if b == 0:
        return 1, 0, a
    x, y, d = ee(b, a % b)
    j = a//b
    return y, (x - (j*y)), d


def main():
    for line in sys.stdin:
        to_do = line.split(" ")
        if "gcd" in to_do[0]:
            print(gcd(int(to_do[1]), int(to_do[2])))
        elif "exp" in to_do[0]:
            print(exp(int(to_do[1]), int(to_do[2]), int(to_do[3])))
        elif "inverse" in to_do[0]:
            print(inverse(int(to_do[1]), int(to_do[2])))
        elif "isprime" in to_do[0]:
            print(is_prime(int(to_do[1])))
        elif "key" in to_do[0]:
            key(int(to_do[1]), int(to_do[2]))


if __name__ == "__main__":
    main()
