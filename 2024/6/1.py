from pprint import pprint

mission = """--- Day 6: Guard Gallivant ---
The Historians use their fancy device again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... in the year 1518! It turns out that having direct access to history is very convenient for a group of historians.

You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single guard is patrolling this part of the lab.

Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?

You start by making a map (your puzzle input) of the situation. For example:

....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of the map). Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:

If there is something directly in front of you, turn right 90 degrees.
Otherwise, take a step forward.
Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed suit prototypes):

....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:

....#.....
........>#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Reaching another obstacle (a spool of several very long polymers), she turns right again and continues downward:

....#.....
.........#
..........
..#.......
.......#..
..........
.#......v.
........#.
#.........
......#...
This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):

....#.....
.........#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#v..
By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path. Including the guard's starting position, the positions visited by the guard before leaving the area are marked with an X:

....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..
In this example, the guard will visit 41 distinct positions on your map.

Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?
"""

input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

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
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return '{},{}'.format(self.x, self.y)

    def __repr__(self):
        return self.__str__()
    

    

DIR_ORDER = [Pos(0, -1), Pos(1, 0), Pos(0, 1), Pos(-1, 0)]

class Level:
    def __init__(self, mr_map):
        splitmap = mr_map.split('\n') 
        self.map = [list(dots) for dots in splitmap]

        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == '^':
                    self.pos = Pos(x, y)

        self.dir = 0

    def get(self, pos):
        return self.map[pos.y][pos.x]

    def out_of_bounds(self, pos):
        return pos.x < 0 or pos.y < 0 or pos.x >= len(self.map[0]) or pos.y >= len(self.map)
    
    def next(self):
        steps_walked = []
        out_of_bounds = False

        next_pos = self.pos + DIR_ORDER[self.dir]
        while (self.get(next_pos) != '#'):
            self.pos = next_pos
            next_pos = self.pos + DIR_ORDER[self.dir]
            steps_walked.append(self.pos) 
            if self.out_of_bounds(next_pos):
                out_of_bounds = True
                break
        
        self.dir = (self.dir + 1) % len(DIR_ORDER)
        return steps_walked, out_of_bounds

l = Level(input)

positions = [l.pos]
oob = False
while not oob:
    steps, oob = l.next()
    positions.extend(steps)

print(len(set(positions))) 

