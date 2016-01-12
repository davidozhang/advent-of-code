#!/usr/bin/python

def main():
    _sum = 0
    with open('input.txt') as data:
        _input = data.read()
        for i in _input.split('\n'):
            if not i:
                continue
            chars = len(i)
            # part 1
            '''
            memory = 0
            j = 1
            while j < len(i) - 1:
                if ord(i[j]) == 92 and i[j+1] == 'x':
                    j += 4
                elif ord(i[j]) == 92:
                    j += 2
                else:
                    j += 1
                memory += 1
            _sum += chars - memory
            '''
            # part 2
            memory = 2
            j = 0
            while j < len(i):
                if i[j] == '"' or ord(i[j]) == 92:
                    memory += 1
                j += 1
                memory += 1
            _sum += memory - chars
    print _sum

if __name__ == '__main__':
    main()