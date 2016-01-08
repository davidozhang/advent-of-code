#!/usr/bin/python

def main():
	with open('input.txt') as data:
		_input = data.read()
		# part 1
		# print _input.count('(') - _input.count(')')
		# part 2
		count, result = 0, 0
		for i, j in enumerate(_input):
			if j == '(':
				count += 1
			elif j == ')':
				count -= 1
			if count < 0:
                                result = i
                                break
		print result + 1
if __name__ == '__main__':
	main()
