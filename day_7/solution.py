#!/usr/bin/python
import types
import re

expressions = {}
cached = {}
def evaluate_expression(expression):
    tokens = expression.split()
    if tokens.count('AND') == 1:
        result = evaluate_operand(tokens[0]) & evaluate_operand(tokens[2])
    elif tokens.count('OR') == 1:
        result = evaluate_operand(tokens[0]) | evaluate_operand(tokens[2])
    elif tokens.count('LSHIFT') == 1:
        result = evaluate_operand(tokens[0]) << evaluate_operand(tokens[2])
    elif tokens.count('RSHIFT') == 1:
        result = evaluate_operand(tokens[0]) >> evaluate_operand(tokens[2])
    elif tokens.count('NOT') == 1:
        result = ~evaluate_operand(tokens[1])
    else:
        result = evaluate_operand(tokens[0])
    return result + 0x10000 if result < 0 else result

def evaluate_operand(operand):
    try:
        return int(operand)
    except:
        if operand in cached:
            return cached[operand]
        else:
            value = evaluate_expression(expressions[operand])
            cached[operand] = value
            return value

def main():
    with open('input.txt') as data:
        _input = data.read()
        for i in _input.split('\n'):
            if not i:
                continue
            p = i.split(' -> ')
            expressions[p[1]] = p[0]
    # part 1
    print evaluate_expression('a')

if __name__ == '__main__':
    main()