#!/usr/bin/python
from itertools import permutations

def main():
	cities = set()
	distances = {}
	sums = []
	with open('input.txt') as data:
		_input = data.read()
		for i in _input.split('\n'):
			if not i:
				continue
			left, right = i.split(' = ')
			first, second = left.split(' to ')
			distances[(first, second)] = int(right)
			distances[(second, first)] = int(right)
			cities.update([first, second])
	for j in permutations(list(cities)):
		_sum = 0
		for k in xrange(len(j)-1):
			_sum += distances[(j[k], j[k+1])]
		sums.append(_sum)
	# part 1
	# print min(sums)
	# part 2
	print max(sums)

if __name__ == '__main__':
	main()