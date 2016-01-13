#!/usr/bin/python
import re
from itertools import permutations

def parser(s):
    pattern = r'(.*) would (.*) (\d+) happiness units by sitting next to (.*).'
    search_result = re.match(pattern, s)
    return search_result.groups()

def main():
    attendees = set()
    _dict = {}
    _max = 0
    _sum = 0
    with open('input.txt') as data:
        _input = data.read()
        for i in _input.split('\n'):
            if not i:
                continue
            p = parser(i)
            attendees.update([p[0], p[3]])
            _dict[(p[0], p[3])] = int(p[2]) if p[1] == 'gain' else -int(p[2])
    # part 2
    for m in attendees:
        _dict[('me', m)] = 0
        _dict[(m, 'me')] = 0
    attendees.add('me')
    for j in permutations(list(attendees)):
        for a, b in zip(j, j[1:]):
            _sum += _dict[(a,b)] + _dict[(b,a)]
        _sum += _dict[(j[0], j[-1])] + _dict[(j[-1], j[0])]
        if _sum > _max:
            _max = _sum
        _sum = 0
    print _max

if __name__ == '__main__':
    main()