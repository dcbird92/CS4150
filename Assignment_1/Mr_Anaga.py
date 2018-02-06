import sys
import random
import string
import time


def randomNumber(xcount, xsize):
    wordcount = 0
    while wordcount < xcount:
        newword = ''
        wordsize = 0
        while wordsize < xsize:
            newword += ''.join(random.choice(string.ascii_lowercase))
            wordsize += 1
        wordcount += 1
        random_words.append(newword)
    # print(random_words)


def sorting():
    x_list = []
    rejected = []
    inputs = 0
    for x_line in random_words:
    # for x_line in sys.stdin:
        word = sorted(x_line.rstrip())
        if word not in x_list:
            x_list.append(word)
            rejected.append(word)
        elif word in rejected:
            rejected.remove(word)
        inputs += 1
        if inputs == count:
            break
    # print(len(rejected))
    # print('NORMAL LIST: ', x_list)
    # print('REJECTED LIST: ', rejected)




if __name__ == '__main__':
    # numbers = input()
    # count, size = numbers.split(" ")
    count = 2000
    size = 4
    loops = 0
    random_words = []
    while loops < 18:
        randomNumber(count, size)
        start = time.time()
        sorting()
        end = time.time()
        print('Count:', count, ' Size: ', size, ' Time: ',end - start)
        loops += 1
        size *= 2







