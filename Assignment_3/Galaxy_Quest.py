import math
import sys


class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def compare(self, star_check):
        return self.x == star_check.x and self.y == star_check.y


def star_distance(s1,s2, distance):
    return math.pow((int(s1.x) - int(s2.x)), 2) + math.pow((int(s1.y) - int(s2.y)), 2) <= math.pow(distance,2)


def findMajority(star_list,distance):
    if len(star_list) == 0:
        return None
    if len(star_list) == 1:
        return star_list[0]
    else:
        mid = len(star_list)/2
        a_list = star_list[:int(mid)]
        b_list = star_list[int(mid):len(star_list)]
        left = findMajority(a_list,distance)
        right = findMajority(b_list,distance)
        if left is None and right is None:
            return None

        elif right is None:
            left_count = 0
            for stars in star_list:
                if star_distance(left,stars,distance):
                    left_count += 1
            if left_count > len(star_list)/2:
                return left
            else: return None

        elif left is None:
            right_count = 0
            for stars in star_list:
                if star_distance(right,stars,distance):
                    right_count += 1
            if right_count > len(star_list)/2:
                return right
            else: return None

        else:
            x_count = 0
            for stars in star_list:
                if star_distance(left,stars,distance):
                    x_count += 1
            if x_count > len(star_list)/2:
                return left
            k_count = 0
            for stars in star_list:
                if star_distance(right, stars, distance):
                    k_count += 1
            if k_count > len(star_list)/2:
                return right
            return None


if __name__ == '__main__':
    galaxy = input()
    diameter, star_count = galaxy.split(" ")
    diameter = int(diameter)
    star_count = int(star_count)
    star_lst = []
    count = 0
    for stars in sys.stdin:
        x_val, y_val = stars.split(" ")
        newstar = Star(x_val,y_val)
        star_lst.append(newstar)
        count += 1
        if count == star_count:
            break
    major = findMajority(star_lst,diameter)
    if major is None:
        print("NO")
    else:
        count = 0
        for stars in star_lst:
            if star_distance(major,stars,diameter):
                count += 1

        print(count)