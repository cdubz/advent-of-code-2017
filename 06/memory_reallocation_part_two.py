"""
--- Part Two ---

Out of curiosity, the debugger would also like to know the size of the loop:
starting from a state that has already been seen, how many block redistribution
cycles must be performed before that same state is seen again?

In the example above, 2 4 1 2 is seen again after four cycles, and so the answer
in that example would be 4.

How many cycles are in the infinite loop that arises from the configuration in
your puzzle input?
"""
bank = {k: int(v) for k, v in enumerate(open('input.txt').read().split())}
seen = []
reset = False
while bank.values() not in seen:
    seen.append(bank.values())
    key = max(bank, key=bank.get)
    value = bank[key]
    bank[key] = 0

    while value > 0:
        value -= 1
        key += 1
        try:
            bank[key] += 1
        except KeyError:
            key = 0
            bank[key] += 1

    if not reset and bank.values() in seen:
        seen = []
        reset = True

print(len(seen))
