#!/usr/bin/python

def main():
	vowels = set(['a','e','i','o','u'])
	nice_count = 0
	with open('input.txt') as data:
		_input = data.read()
		for i in _input.split():
			vowel_count, twice, not_contain = 0, False, False
			for a in i:
				if a in vowels:
					vowel_count += 1
			for b in xrange(len(i)-1):
				if i[b] == i[b+1]:
					twice = True
					break
			if 'ab' not in i and 'cd' not in i and 'pq' not in i and 'xy' not in i:
				not_contain = True
			if vowel_count >= 3 and twice and not_contain:
				nice_count += 1
	print nice_count
if __name__ == '__main__':
	main()
