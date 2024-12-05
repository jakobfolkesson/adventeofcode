mission = """--- Day 4: Ceres Search ---
"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:


..X...
.SAMX.
.A..A.
XMAS.S
.X....
The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
Take a look at the little Elf's word search. How many times does XMAS appear?"""


input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

desireUp = """
d
ch
bgl
afkp
ejo
in
m
"""

desireDown = """
a
eb
ifc
mjgd
nkh
ol
p
"""

input = open('input.txt').read()

input = input.split('\n')
input = [list(i) for i in input]

# create letter class with x, y, and next
class Letter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def next(self):
        raise NotImplementedError('next method not implemented')
    
    def __str__(self):
        return self.get()

    def is_done(self):
        return self.x >= len(input) or self.y >= len(input[0]) or self.x < 0 or self.y < 0

    def get(self):
        return input[self.x][self.y]

# create subclas vertical letter
class VerticalLetter(Letter):
    def next(self):
        self.x += 1

class HorizontalLetter(Letter):
    def next(self):
        self.y += 1

class DiagonalUpLetter(Letter):
    def next(self):
        self.x += 1
        self.y += 1

class DiagonalDownLetter(Letter):
    def next(self):
        self.x -= 1
        self.y += 1

horisontals = [HorizontalLetter(i, 0) for i in range(len(input))]
verticals = [VerticalLetter(0, i) for i in range(len(input[0]))]

diagonalsUp = [DiagonalUpLetter(i, 0) for i in range(len(input))] 
diagonalsUp += [DiagonalUpLetter(0, i) for i in range(1, len(input[0]))] 

diagonalsDown = [DiagonalDownLetter(len(input)-1, i) for i in range(len(input))]
diagonalsDown += [DiagonalDownLetter(i, 0) for i in range(len(input[0])-1)] 

letters = horisontals + verticals + diagonalsUp + diagonalsDown


all_lines = []
for letter in letters:
    line = []
    while not letter.is_done():
        line.append(letter.get())
        letter.next()
    all_lines.append(''.join(line))

# backwaards
all_lines = all_lines + [line[::-1] for line in all_lines]

xmax_count = 0
for line in all_lines:
    xmax_count += line.count('XMAS')
print(xmax_count)
