#!/usr/bin/python

def convert(s):
	return 1 if s=='#' else 0

def cycle(lst, offsets, width, height):
	changed = [[0 for i in xrange(width)] for j in xrange(height)]
	for i in xrange(height):
		for j in xrange(width):
			on = 0
			for k in offsets:
				if i+k[0]<0 or i+k[0]==height or j+k[1]<0 or j+k[1]==width:
					continue
				on += 1 if lst[i+k[0]][j+k[1]] == 1 else 0
			if (lst[i][j] == 0 and on == 3) or (lst[i][j] == 1 and on != 2 and on != 3):
				changed[i][j] = 1
			# part 2
			if i == 0 and (j == 0 or j == width-1):
				changed[i][j] = 0
			elif i == height-1 and (j == 0 or j == width-1):
				changed[i][j] = 0
	for i in xrange(height):
		for j in xrange(width):
			if changed[i][j] == 1:
				lst[i][j] ^= 1
	return lst

def main():
	offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
	with open('input.txt') as f:
		width, height = 100, 100
		l, l2 = [], []
		data = f.read()
		for i in data.split('\n'):
			if not i:
				continue
			l.append(map(convert, list(i)))
	for i in xrange(100):
		l2 = cycle(l, offsets, width, height)
		l, l2 = l2, l
	count = 0
	for i in xrange(height):
		count += sum(l[i])
	print count

if __name__ == '__main__':
	main()