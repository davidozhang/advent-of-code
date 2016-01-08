#!/usr/bin/python

def main():
	total = 0
	with open('input.txt') as data:
		_input = data.read()
		for i in _input.split():
			l, w, h = map(int, i.split('x'))
			# part 1
			# total += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
			# part 2
			total += min(2*l+2*h, 2*w+2*l, 2*w+2*h) + l*w*h
	print total	

if __name__ == '__main__':
	main()
