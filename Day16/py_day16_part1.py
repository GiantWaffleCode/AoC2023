#   Advent of Code 2023
#      GiantWaffle
#   Challenge 16 of 25
#      Part 1 of 2
# -----------------------

from dataclasses import dataclass

use_real_data = True
data = []

with open('Day16\data_day16.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

# example = [
#     '.|...\\....',
#     '|.-.\\.....',
#     '.....|-...',
#     '........|.',
#     '..........',
#     '.........\\',
#     '..../.\\\\..',
#     '.-.-/..|..',
#     '.|....-|.\\',
#     '..//.|....'
# ]

example = [
    '\\........-.........\\................................|...',
    '......-/.............|-.../.....|...........././..\\.....',
    '-.........................|.....\\...................|.\\.',
    '.......-........../.......\\.........|..../........-.-|..',
]



if use_real_data:
    test_input = data
else:
    test_input = example

# for line in test_input:
#     print(line)


eng_grid = []
grid_height = len(test_input)
grid_width = len(test_input[0])


for y in range(grid_height):
    blank_str = '.'*grid_width
    eng_grid.append(blank_str)


def energize_cell(cords): # cords = [x,y]
    line = eng_grid[cords[1]]
    line = line[:cords[0]] + '#' + line[cords[0]+1:]
    eng_grid[cords[1]] = line


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
                if self.cords[0] < len(eng_grid[0])-1:
                    self.cords[0] += 1
                else:
                    beams.remove(self)
            case 'S':
                if self.cords[1] < len(eng_grid)-1:
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
                
    def energize(self):
        energize_cell(self.cords)

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

def print_grid():
    print(f'Engergized Grid')
    for line in eng_grid:
        print(line)


cycles = 4000

#init beam
starting_beam = Beam([0,0],'E')
starting_beam.energize()


beams = []
beams.append(starting_beam)

for cycle in range(cycles):
    #print(f'Cycle Count: {cycle+1}')
    for num, beam in enumerate(beams):
        cell = get_cell(beam.cords) # get symbol were on
        #print(f'Beam {num+1}: {beam}')
        #print(f'Cell : {cell}')
        beam_dir = choose_dir(beam, cell) #do something based off symbol
        #print(beam_dir)
        beam.move() #move beam
        beam.check_hist() #check to see if beam has been here before
        beam.add_to_hist() # add location and dir to history
        #print(f'Moved to: {beam.cords}')
        beam.energize() #energize cell we moved to
        #print(cell)

    if len(beams) == 0:
        print(f'Final Cycle: {cycle}')
        break
    #print_grid()

    # if len(eng_history) >= 10:
    #     eng_history.pop(0)
    # eng_history.append(current_eng)
    # if len(eng_history) == 10:
    #     if len(set(eng_history)) == 1:
    #         break


        

# print(f'Cords: {get_cell(starting_beam.cords)}')

# print(starting_beam.cords, starting_beam.dir)
#print_grid()

current_eng = calc_grid_energy(eng_grid)

print(f'Part 1 Answer: {current_eng}')