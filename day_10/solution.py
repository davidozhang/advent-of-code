#!/usr/bin/python
from itertools import groupby
def main():
	_input = '1321131112'
	_temp = ''
	for _ in xrange(50):	# 40 for part 1
		for i, j in groupby(_input):
			_temp += str(len(list(j))) + i
		_input = _temp
		_temp = ''
	print len(_input)
if __name__ == '__main__':
	main()