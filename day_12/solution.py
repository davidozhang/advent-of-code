#!/usr/bin/python

def main():
	_sum = 0
	with open('input.txt') as data:
		_input = data.read()
		accum = ''
		i = 0
		while i < len(_input):
			if _input[i] == '-' or _input[i].isdigit():
				accum += _input[i]
			else:
				if accum != '':
					_sum += int(accum)
					accum = ''
			i += 1
	print _sum

if __name__ == '__main__':
	main()