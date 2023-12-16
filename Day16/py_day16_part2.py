#   Advent of Code 2023
#      GiantWaffle
#   Challenge 16 of 25
#      Part 2 of 2
# -----------------------

from dataclasses import dataclass

use_real_data = True
data = []

with open('Day16\data_day16.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = [
    '.|...\\....',
    '|.-.\\.....',
    '.....|-...',
    '........|.',
    '..........',
    '.........\\',
    '..../.\\\\..',
    '.-.-/..|..',
    '.|....-|.\\',
    '..//.|....'
]


if use_real_data:
    test_input = data
else:
    test_input = example

# for line in test_input:
#     print(line)


grid_height = len(test_input)
grid_width = len(test_input[0])

def create_eng_grid():
    eng_grid = []
    for y in range(grid_height):
        blank_str = '.'*grid_width
        eng_grid.append(blank_str)
    return eng_grid


def energize_cell(grid, cords): # cords = [x,y]
    line = grid[cords[1]]
    line = line[:cords[0]] + '#' + line[cords[0]+1:]
    grid[cords[1]] = line

@dataclass
class Beam:
    cords: [int, int]
    dir: str
    hist = {}

    def move(self):
        match self.dir:
            case 'N':
                if self.cords[1] > 0:
                    self.cords[1] -= 1
                else:
                    beams.remove(self)
            case 'E':
                if self.cords[0] < grid_width-1:
                    self.cords[0] += 1
                else:
                    beams.remove(self)
            case 'S':
                if self.cords[1] < grid_height-1:
                    self.cords[1] += 1
                else:
                    beams.remove(self)
            case 'W':
                if self.cords[0] > 0:
                    self.cords[0] -= 1
                else:
                    beams.remove(self)

    def change_dir(self, new_dir):
        self.dir = new_dir

    def split(self, split_or):
        if self.dir == 'E' or self.dir == 'W':
            if split_or == '|':  # split beam
                self.dir = 'N'
                #print(f'Changed Direction to North')
                new_beam = Beam(self.cords.copy(), 'S')
                beams.append(new_beam)
        else:
            if split_or == '-':  # split beam
                self.dir = 'E'
                #print(f'Changed Direction to East')
                new_beam = Beam(self.cords.copy(), 'W')
                beams.append(new_beam)

    def deflect(self, mirror):
        match self.dir:
            case 'N':
                if mirror == '\\':
                    self.dir = 'W'
                else:
                    self.dir = 'E'
            case 'E':
                if mirror == '\\':
                    self.dir = 'S'
                else:
                    self.dir = 'N'
            case 'S':
                if mirror == '\\':
                    self.dir = 'E'
                else:
                    self.dir = 'W'
            case 'W':
                if mirror == '\\':
                    self.dir = 'N'
                else:
                    self.dir = 'S'
                
    def energize(self, grid):
        energize_cell(grid, self.cords)

    def add_to_hist(self):
        self.hist[(self.cords[0], self.cords[1], self.dir)] = 1

    def check_hist(self): #[[x,y], str : 'N']
        if (self.cords[0], self.cords[1], self.dir) in self.hist:
            if self in beams:
                beams.remove(self)


def get_cell(cords):
    return test_input[cords[1]][cords[0]]

def choose_dir(beam, cell):
    match cell:
        case '\\':
            beam.deflect('\\')
            return 'Deflect'
        case '/':
            beam.deflect('/')
            return 'Deflect'
        case '-':
            beam.split('-')
            return 'Split'
        case '|':
            beam.split('|')
            return 'Split'
        case '.':
            return 'Nothing'

def calc_grid_energy(grid):
    eng_count = 0
    for line in grid:
        eng_count += line.count('#')
    return eng_count

def print_grid(grid):
    print(f'Engergized Grid')
    for line in grid:
        print(line)

beams = []

def run_grid(starting_beam):
    global beams
    beams.append(starting_beam)
    eng_grid = create_eng_grid()
    beams[0].energize(eng_grid)
    Beam.hist = {}

    while len(beams) != 0:
        #print(f'Cycle Count: {cycle+1}')
        for num, beam in enumerate(beams):
            cell = get_cell(beam.cords) # get symbol were on
            beam_dir = choose_dir(beam, cell) #do something based off symbol
            beam.move() #move beam
            beam.check_hist() #check to see if beam has been here before
            beam.add_to_hist() # add location and dir to history
            beam.energize(eng_grid) #energize cell we moved to

    current_eng = calc_grid_energy(eng_grid)
    print_grid(eng_grid)
    return current_eng    

max_eng_val = 0

def fuck_you_chat(x, y, dir):
    global max_eng_val
    print('')
    print(f'X: {x} Y: {y}, DIR: {dir}')
    starting_beam = Beam([x,y], dir)
    eng_val = run_grid(starting_beam)
    max_eng_val = max(max_eng_val, eng_val)
    print(f'Energy: {eng_val}, Max Energy: {max_eng_val}')

for y in range(grid_height):
    for x in range(grid_width):
        if y == 0:
            fuck_you_chat(x, y, 'S')
        if y == grid_height-1:
            fuck_you_chat(x, y, 'N')
        if x == 0:
            fuck_you_chat(x, y, 'E')
        if x == grid_width-1:
            fuck_you_chat(x, y, 'W')


print(f'Part 1 Answer: {max_eng_val}')