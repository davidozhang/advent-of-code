#!/usr/bin/python

def main():
	santa = (0,0)
	robo = (0,0)
	houses = set([(0,0)])
	with open('input.txt') as data:
		_input = data.read()
		for i, j in enumerate(_input):
			if j == '>':
				if i%2 == 0:
					santa = (santa[0]+1, santa[1])
				else:
					robo = (robo[0]+1, robo[1])
			elif j == '<':
				if i%2 == 0:
					santa = (santa[0]-1, santa[1])
				else:
					robo = (robo[0]-1, robo[1])
			elif j == '^':
				if i%2 == 0:
					santa = (santa[0], santa[1]+1)
				else:
					robo = (robo[0], robo[1]+1)
			elif j == 'v':
				if i%2 == 0:
					santa = (santa[0], santa[1]-1)
				else:
					robo = (robo[0], robo[1]-1)
			if i%2 == 0:
				houses.add(santa)
			else:
				houses.add(robo)
	print len(houses)

if __name__ == '__main__':
	main()
