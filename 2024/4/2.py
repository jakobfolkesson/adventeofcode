mission = """The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S
Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?
"""

input = """M.S
.A.
M.S"""

input = open('input.txt').read()
input = input.split('\n')
input = [list(i) for i in input]


_sum = 0
for x in range(len(input)):
    for y in range(len(input[x])):
        if input[x][y] == 'A' and x > 0 and y > 0 and x < len(input) - 1 and y < len(input[x]) - 1:
           a = [input[x-1][y-1], input[x+1][y+1]]
           b = [input[x-1][y+1], input[x+1][y-1]]
           if sorted(a) == sorted(b) == ['M', 'S']:
                _sum += 1

print(_sum)