#!/usr/bin/python
import re

def parser(s):
    pattern = r'(.*) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'
    search_result = re.match(pattern, s)
    return search_result.groups()

def main():
    time = 2503
    winner = None
    _max = 0
    with open('input.txt') as data:
        _input = data.read()
        for i in _input.split('\n'):
            if not i:
                continue
            p = parser(i)
            distance = int(p[1])*int(p[2])*(time/(int(p[2])+int(p[3])))
            distance += int(p[1])*int(p[2]) if time%(int(p[2])+int(p[3])) > int(p[2]) else 0
            if distance > _max:
                _max = distance
                winner = p[0]
    print _max

if __name__ == '__main__':
    main()