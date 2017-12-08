"""
--- Part Two ---

To be safe, the CPU also needs to know the highest value held in any register
during this process so that it can decide how much memory to allocate to these
operations. For example, in the above instructions, the highest value ever held
was 10 (in register c after the third instruction was evaluated).
"""
import re

registers = {}
max_register_value = 0
with open('input.txt') as f:
    for line in f:
        result = re.search('(?P<register>[a-z]+) (?P<op>inc|dec) (?P<amt>-?\d+) '
                           'if (?P<cond_register>[a-z]+) (?P<cond>.+) '
                           '(?P<cond_amt>-?\d+)', line.strip())

        register = result.group('register')
        op = result.group('op')
        amt = int(result.group('amt'))
        cond_register = result.group('cond_register')
        cond = result.group('cond')
        cond_amt = int(result.group('cond_amt'))

        if register not in registers:
            registers[register] = 0
        if cond_register not in registers:
            registers[cond_register] = 0

        if eval('{} {} {}'.format(registers[cond_register], cond, cond_amt)):
            if op == 'inc':
                registers[register] += amt
            elif op == 'dec':
                registers[register] -= amt

        if registers[register] > max_register_value:
            max_register_value = registers[register]

print(max_register_value)
