#!/usr/bin/python
from itertools import groupby

not_allowed = set(['i', 'o', 'l'])
def increment(s):
    ascii = [ord(i) for i in s]
    for i in xrange(len(ascii)-1, -1, -1):
        if ascii[i] == 122:
            ascii[i] = 97
        else:
            ascii[i] += 1
            break
    return ''.join(map(chr, ascii))

def check(s):
    three_straight, pairs = False, 0
    for j in s:
        if j in not_allowed:
            return False
    ascii = [ord(i) for i in s]
    for i in xrange(len(ascii)-2):
        if ascii[i]+1 == ascii[i+1] and ascii[i+1]+1 == ascii[i+2]:
            three_straight = True
            break
    prev = None
    for k in xrange(len(s)-1):
        if s[k] == s[k+1] and s[k] != prev:
            pairs += 1
            prev = s[k]
    return three_straight and pairs >= 2

def main():
    # part 1
    # password = 'cqjxjnds'
    # part 2
    password = 'cqjxyaaa'
    while not check(password):
        password = increment(password)
        print password
    print password

if __name__ == '__main__':
    main()