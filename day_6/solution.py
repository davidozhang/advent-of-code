#!/usr/bin/python
import re

def parser(s):
	pattern = r'(.*) (\d+),(\d+) (.*) (\d+),(\d+)'
        input_re = re.compile(pattern)
        search_result = re.match(pattern, s)
        return search_result.groups()

def main():
	_dict = {(i,j): 0 for i in xrange(0,1000) for j in xrange(0,1000)}
	with open('input.txt') as data:
		_input = data.read()
		for i in _input.split('\n'):
			if i:
				# 0: command, 1-2: first coord, 4-5: second coord
				p = parser(i)
				cmd, x_start, y_start, x_end, y_end = p[0], int(p[1]), int(p[2]), int(p[4]), int(p[5])
				for i in xrange(x_start, x_end+1):
					for j in xrange(y_start, y_end+1):
						if cmd == 'turn on':
							# part 1
							# _dict[(i,j)] = 1
							# part 2
							_dict[(i,j)] += 1
						elif cmd == 'toggle':
							# part 1
							# _dict[(i,j)] ^= 1
							# part 2
							_dict[(i,j)] += 2
						elif cmd == 'turn off':
							# part 1
							# _dict[(i,j)] = 0
							# part 2
							if _dict[(i,j)] > 0:
								_dict[(i,j)] -= 1
		# part 1
		# print _dict.values().count(1)
		# part 2
		print sum(_dict.values())

if __name__ == '__main__':
	main()
