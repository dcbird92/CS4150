import math
import sys
'''
PU's galactic diameter d(1<=d<=10^6) and star count k(1<=k<=106)
There are exactly k more lines (# of stars)
Each line contains x(0<=x<=109) and y(0<=y<=10^9) *No two lines are identical
Star position and d guarantee that any stars that are greater than
d distance apart are not in the same PU, meaning all the stars in that galaxy
do not need to be checked with that star
'''

class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def compare(self, star_check):
        return self.x == star_check.x and self.y == star_check.y


def star_distance(s1,s2, distance):
    return math.pow((int(s1.x) - int(s2.x)), 2) + math.pow((int(s1.y) - int(s2.y)), 2) <= math.pow(distance,2)


def subList(s_list, distance):
    pos = 0
    newList = []
    while pos < len(s_list):
        if star_distance(s_list[pos], s_list[pos+1], distance):
            newList.append(s_list[pos])
        pos += 2
    if len(newList) == 0:
        return None
    return newList


def findMajority(s_list, distance):
    if len(s_list) == 1:
        return s_list[0]
    sub_list = s_list.copy()
    while len(sub_list) > 1:
        if len(sub_list) % 2 == 1:
            y = sub_list.pop()
        else:
            y = None
        temp_list = subList(sub_list, distance)
        if temp_list is None:
            if y is not None:
                count = 1
                for stars in s_list:
                    if star_distance(y, stars, distance):
                        count += 1
                if count > len(s_list)/2:
                    return y
                else:
                    return None
            else:
                return None
        sub_list = temp_list
    return sub_list[0]


if __name__ == '__main__':
    galaxy = input()
    diameter, star_count = galaxy.split(" ")
    diameter = int(diameter)
    star_count = int(star_count)
    star_lst = []
    count = 0
    for stars in sys.stdin:
        x_val, y_val = stars.split(" ")
        nstar = Star(x_val,y_val)
        star_lst.append(nstar)
        count += 1
        if count == star_count:
            break
    majority = findMajority(star_lst, diameter)
    if majority is None:
        print("NO")
    else:
        count = 0
        for stars in star_lst:
            if star_distance(majority, stars, diameter):
                count += 1
        if count > len(star_lst)/2:
            print(count)
        else:
            print("NO")
