def execute(cmd, x, y, registers):
    if cmd == 'snd':
        print('Played {}'.format(registers[x]))
        registers['last_played'] = registers[x]
    elif cmd == 'set':
        registers[x] = y
    elif cmd == 'add':
        registers[x] += y
    elif cmd == 'mul':
        registers[x] *= y
    elif cmd == 'mod':
        registers[x] %= y
    elif cmd == 'rcv' and registers['last_played'] > 0:
        registers[x] = registers['last_played']
        print('Recovered {}'.format(registers['last_played']))

    return registers
