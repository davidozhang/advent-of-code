#!/usr/bin/python

def main():
	with open('input.txt') as f:
		compare = set([
			'children:3',
			'cats:7',
			'samoyeds:2',
			'pomeranians:3',
			'akitas:0',
			'vizslas:0',
			'goldfish:5',
			'trees:3',
			'cars:2',
			'perfumes:1'
		])
		data = f.read()
		for i in data.split('\n'):
			if not i:
				continue
			s = i.split()
			name = s[1][:-1]
			first = (s[2]+s[3])[:-1]
			second = (s[4]+s[5])[:-1]
			third = s[6]+s[7]
			if len(set([first, second, third]).intersection(compare)) == 3:
				print name
				break

if __name__ == '__main__':
	main()