from pprint import pprint
mission = """--- Part Two ---
Watching over your shoulder as you work, one of The Historians asks if you took the effects of resonant harmonics into your calculations.

Whoops!

After updating your model, it turns out that an antinode occurs at any grid position exactly in line with at least two antennas of the same frequency, regardless of distance. This means that some of the new antinodes will occur at the position of each antenna (unless that antenna is the only one of its frequency).

So, these three T-frequency antennas now create many antinodes:

T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
..........
In fact, the three T-frequency antennas are all exactly in line with two antennas, so they are all also antinodes! This brings the total number of antinodes in the above example to 9.

The original example now has 34 antinodes, including the antinodes that appear on every antenna:

##....#....#
.#.#....0...
..#.#0....#.
..##...0....
....0....#..
.#...#A....#
...#..#.....
#....#.#....
..#.....A...
....#....A..
.#........#.
...#......##
Calculate the impact of the signal using this updated model. How many unique locations within the bounds of the map contain an antinode?"""

input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

input = open('input.txt').read()


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # overide add operator for self + Pos or self + tuple
    def __add__(self, other):
        if isinstance(other, Pos):
            return Pos(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple):
            return Pos(self.x + other[0], self.y + other[1])
        else:
            raise NotImplementedError('Addition not implemented for Pos and {}'.format(type(args)))

    def __sub__(self, other):
        return Pos(self.x - other.x, self.y - other.y)
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return '{},{}'.format(self.x, self.y)

    def __repr__(self):
        return self.__str__()


letters = set(list(input))
letters.remove('.')
letters.remove('\n')

the_map = input.split('\n')
the_map = [list(row) for row in the_map]


antennas = {key: [] for key in letters}

for antenna_type in letters:

    # find all antennas of this type
    for y in range(len(the_map)):
        for x in range(len(the_map[y])):
            if the_map[y][x] == antenna_type:
                antennas[antenna_type].append(Pos(x, y))


def oob(pos):
    return pos.x < 0 or pos.y < 0 or pos.x >= len(the_map[0]) or pos.y >= len(the_map)
    

freq_points = set()

for [key, positions] in antennas.items():
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            p1 = positions[i]
            p2 = positions[j]

            a = p1 - p2
            b = p2 - p1

            freq_pos = p1
            while not oob(freq_pos):
                freq_points.add(freq_pos)
                freq_pos = freq_pos + a

            freq_pos = p2
            while not oob(freq_pos):
                freq_points.add(freq_pos)
                freq_pos = freq_pos + b

print(len(freq_points))