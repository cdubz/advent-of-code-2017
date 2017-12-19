"""
--- Part Two ---
As you congratulate yourself for a job well done, you notice that the
documentation has been on the back of the tablet this entire time. While you
actually got most of the instructions correct, there are a few key differences.
This assembly code isn't about sound at all - it's meant to be run twice at the
same time.

Each running copy of the program has its own set of registers and follows the
code independently - in fact, the programs don't even necessarily run at the
same speed. To coordinate, they use the send (snd) and receive (rcv)
instructions:

snd X sends the value of X to the other program. These values wait in a queue
until that program is ready to receive them. Each program has its own message
queue, so a program can never receive a message it sent.

rcv X receives the next value and stores it in register X. If no values are in
the queue, the program waits for a value to be sent to it. Programs do not
continue to the next instruction until they have received a value. Values are
received in the order they are sent.

Each program also has its own program ID (one 0 and the other 1); the register
p should begin with this value.

For example:

snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d

Both programs begin by sending three values to the other. Program 0 sends 1, 2,
0; program 1 sends 1, 2, 1. Then, each program receives a value (both 1) and
stores it in a, receives another value (both 2) and stores it in b, and then
each receives the program ID of the other program (program 0 receives 1; program
1 receives 0) and stores it in c. Each program now sees a different value in its
own copy of register c.

Finally, both programs try to rcv a fourth time, but no data is waiting for
either of them, and they reach a deadlock. When this happens, both programs
terminate.

It should be noted that it would be equally valid for the programs to run at
different speeds; for example, program 0 might have sent all three values and
then stopped at the first rcv before program 1 executed even its first
instruction.

Once both of your programs have terminated (regardless of what caused them to
do so), how many times did program 1 send a value?
"""
duet = [line.rstrip() for line in open('input.txt').readlines()]

registers = {0: {'p': 0}, 1: {'p': 1}}
queue = {0: [], 1: []}
state = {0: 'running', 1: 'running'}
sends = {0: 0, 1: 0}
i = {0: 0, 1: 0}
while True:
    cmds = {0: duet[i[0]][0:3], 1: duet[i[1]][0:3]}
    x = {0: duet[i[0]][4:5], 1: duet[i[1]][4:5]}
    y = {0: '', 1: ''}
    if len(duet[i[0]]) > 5:
        y[0] = duet[i[0]][6:len(duet[i[0]])]
    if len(duet[i[1]]) > 5:
        y[1] = duet[i[1]][6:len(duet[i[1]])]

    if state[0] == 'receiving' and state[1] == 'receiving':
        print('Deadlocked')
        print(sends)
        exit(0)

    for j, cmd in cmds.items():
        if x[j].isalpha() and x[j] not in registers[j]:
            registers[j][x[j]] = 0

        if cmd == 'snd':
            if j == 0:
                queue[1].insert(0, registers[j][x[j]])
            else:
                queue[0].insert(0, registers[j][x[j]])
            sends[j] += 1
        elif cmd == 'set':
            if y[j].isalpha():
                registers[j][x[j]] = registers[j][y[j]]
            else:
                registers[j][x[j]] = int(y[j])
        elif cmd == 'add':
            if y[j].isalpha():
                registers[j][x[j]] += registers[j][y[j]]
            else:
                registers[j][x[j]] += int(y[j])
        elif cmd == 'mul':
            if y[j].isalpha():
                registers[j][x[j]] *= registers[j][y[j]]
            else:
                registers[j][x[j]] *= int(y[j])
        elif cmd == 'mod':
            if y[j].isalpha():
                registers[j][x[j]] %= registers[j][y[j]]
            else:
                registers[j][x[j]] %= int(y[j])
        elif cmd == 'rcv':
            state[j] = 'receiving'
            if len(queue[j]) > 0:
                registers[j][x[j]] = queue[j].pop()
                state[j] = 'running'
        elif cmd == 'jgz':
            if (x[j].isalpha() and registers[j][x[j]] > 0) or (
                    x[j].isdigit() and int(x[j]) > 0):
                if y[j].isalpha():
                    i[j] += registers[j][y[j]] - 1
                else:
                    i[j] += int(y[j]) - 1

        if state[j] == 'running':
            i[j] += 1
