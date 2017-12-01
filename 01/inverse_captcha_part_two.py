"""
--- Part Two ---

You notice a progress bar that jumps to 50% completion. Apparently, the door
isn't yet satisfied, but it did emit a star as encouragement. The instructions
change:

Now, instead of considering the next digit, it wants you to consider the digit
halfway around the circular list. That is, if your list contains 10 items, only
include a digit in your sum if the digit 10/2 = 5 steps forward matches it.
Fortunately, your list has an even number of elements.

For example:

- 1212 produces 6: the list contains 4 items, and all four digits match the
  digit 2 items ahead.
- 1221 produces 0, because every comparison is between a 1 and a 2.
- 123425 produces 4, because both 2s match each other, but no other digit has a
  match.
- 123123 produces 12.
- 12131415 produces 4.
"""
import sys

total = 0
length = len(sys.argv[1])
digits = list(sys.argv[1] + sys.argv[1][0:length/2])
for a, b in zip(digits[::1], digits[length/2::1]):
    if a == b:
        total += int(a)

print(total)
