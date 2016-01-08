#!/usr/bin/python

import hashlib

def main():
	_input = 'yzbqklnj'
	counter = 0
	while True:
		counter += 1
		m = hashlib.md5()
		m.update(_input+str(counter))
		# if m.hexdigest()[:5].count('0') == 5:
			# break
		if m.hexdigest()[:6].count('0') == 6:
			break
	print counter

if __name__ == '__main__':
	main()
