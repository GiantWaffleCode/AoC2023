#   Advent of Code 2023
#      GiantWaffle
#   Challenge 10 of 25
#      Part 1 of 2
# -----------------------

from tkinter import *

use_real_data = True

data = []

with open('Day10\data_day10.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = [
    '.....',
    '.F-7.',
    '.|.|.',
    '.L-J.',
    '.....'
]

if use_real_data:
    test_input = data
else:
    test_input = example


class Node:
    def __init__(self, x, y, direction, fill):
        self.x = x
        self.y = y
        self.direction = direction
        self.fill = fill
        self.visited = False

        self.conn_fwd = Node
        self.conn_bwd = Node

        self.drawPipe()

    def drawHorLine(self, canvas, x, y, fill):
        canvas.create_line(7*x+2, 7*y+3, 7*x+9, 7*y+3)
        canvas.create_line(7*x+2, 7*y+7, 7*x+9, 7*y+7)
        if fill:
            canvas.create_line(7*x+2, 7*y+4, 7*x+9, 7*y+4, fill=fill)
            canvas.create_line(7*x+2, 7*y+5, 7*x+9, 7*y+5, fill=fill)
            canvas.create_line(7*x+2, 7*y+6, 7*x+9, 7*y+6, fill=fill)

    def drawVertLine(self, canvas, x, y, fill):
        canvas.create_line(7*x+3, 7*y+2, 7*x+3, 7*y+9)
        canvas.create_line(7*x+7, 7*y+2, 7*x+7, 7*y+9)
        if fill:
            canvas.create_line(7*x+4, 7*y+2, 7*x+4, 7*y+9, fill=fill)
            canvas.create_line(7*x+5, 7*y+2, 7*x+5, 7*y+9, fill=fill)
            canvas.create_line(7*x+6, 7*y+2, 7*x+6, 7*y+9, fill=fill)

    def drawNELine(self, canvas, x, y, fill):
        canvas.create_line(7*x+3, 7*y+2, 7*x+3, 7*y+8)
        canvas.create_line(7*x+3, 7*y+7, 7*x+9, 7*y+7)
        canvas.create_line(7*x+7, 7*y+2, 7*x+7, 7*y+4)
        canvas.create_line(7*x+7, 7*y+3, 7*x+9, 7*y+3)
        if fill:
            canvas.create_line(7*x+4, 7*y+4, 7*x+9, 7*y+4, fill=fill)
            canvas.create_line(7*x+4, 7*y+5, 7*x+9, 7*y+5, fill=fill)
            canvas.create_line(7*x+4, 7*y+6, 7*x+9, 7*y+6, fill=fill)
            canvas.create_line(7*x+4, 7*y+2, 7*x+7, 7*y+2, fill=fill)
            canvas.create_line(7*x+4, 7*y+3, 7*x+7, 7*y+3, fill=fill)

    def drawSELine(self, canvas, x, y, fill):
        canvas.create_line(7*x+3, 7*y+3, 7*x+9, 7*y+3)
        canvas.create_line(7*x+3, 7*y+3, 7*x+3, 7*y+9)
        canvas.create_line(7*x+7, 7*y+7, 7*x+9, 7*y+7)
        canvas.create_line(7*x+7, 7*y+7, 7*x+7, 7*y+9)
        if fill:
            canvas.create_line(7*x+4, 7*y+4, 7*x+9, 7*y+4, fill=fill)
            canvas.create_line(7*x+4, 7*y+5, 7*x+9, 7*y+5, fill=fill)
            canvas.create_line(7*x+4, 7*y+6, 7*x+9, 7*y+6, fill=fill)
            canvas.create_line(7*x+4, 7*y+7, 7*x+7, 7*y+7, fill=fill)
            canvas.create_line(7*x+4, 7*y+8, 7*x+7, 7*y+8, fill=fill)

    def drawNWLine(self, canvas, x, y, fill):
        canvas.create_line(7*x+2, 7*y+3, 7*x+4, 7*y+3)
        canvas.create_line(7*x+3, 7*y+2, 7*x+3, 7*y+4)
        canvas.create_line(7*x+7, 7*y+2, 7*x+7, 7*y+7)
        canvas.create_line(7*x+2, 7*y+7, 7*x+8, 7*y+7)
        if fill:
            canvas.create_line(7*x+2, 7*y+4, 7*x+7, 7*y+4, fill=fill)
            canvas.create_line(7*x+2, 7*y+5, 7*x+7, 7*y+5, fill=fill)
            canvas.create_line(7*x+2, 7*y+6, 7*x+7, 7*y+6, fill=fill)
            canvas.create_line(7*x+4, 7*y+2, 7*x+7, 7*y+2, fill=fill)
            canvas.create_line(7*x+4, 7*y+3, 7*x+7, 7*y+3, fill=fill)

    def drawSWLine(self, canvas, x, y, fill):
        canvas.create_line(7*x+2, 7*y+3, 7*x+7, 7*y+3)
        canvas.create_line(7*x+7, 7*y+3, 7*x+7, 7*y+9)
        canvas.create_line(7*x+2, 7*y+7, 7*x+4, 7*y+7)
        canvas.create_line(7*x+3, 7*y+7, 7*x+3, 7*y+9)
        if fill:
            canvas.create_line(7*x+2, 7*y+4, 7*x+7, 7*y+4, fill=fill)
            canvas.create_line(7*x+2, 7*y+5, 7*x+7, 7*y+5, fill=fill)
            canvas.create_line(7*x+2, 7*y+6, 7*x+7, 7*y+6, fill=fill)
            canvas.create_line(7*x+4, 7*y+7, 7*x+7, 7*y+7, fill=fill)
            canvas.create_line(7*x+4, 7*y+8, 7*x+7, 7*y+8, fill=fill)


    def drawPipe(self):
        match self.direction:
            case '|':
                self.drawVertLine(my_canvas, self.x, self.y, self.fill)
            case '-':
                self.drawHorLine(my_canvas, self.x, self.y, self.fill)
            case 'L':
                self.drawNELine(my_canvas, self.x, self.y, self.fill)
            case 'J':
                self.drawNWLine(my_canvas, self.x, self.y, self.fill)
            case '7':
                self.drawSWLine(my_canvas, self.x, self.y, self.fill)
            case 'F':
                self.drawSELine(my_canvas, self.x, self.y, self.fill)

    def fillPipe(self, color):
        self.fill = color
        self.drawPipe()


root = Tk()
root.title('Day 10')
root.geometry('1080x1080')

canvas_size = [len(test_input[0]),len(test_input)]

my_canvas = Canvas(root,
    width=canvas_size[0]*7,
    height=canvas_size[1]*7,
    bg='grey')

my_canvas.pack(pady=20)

nodes = []
starting_location = []


for y, line in enumerate(test_input):
    node_line = []
    for x, cell in enumerate(line):
        if cell == 'S':
            starting_location = [x, y]
            node_line.append(Node(x, y, '|', False))
        elif cell != '.':
            node_line.append(Node(x, y, cell, False))
        else:
            node_line.append(Node(x,y, '.', False))
    nodes.append(node_line)


#print(f'{starting_location=}')
starting_node = nodes[starting_location[1]][starting_location[0]]
#print(starting_node.x, starting_node.y)
starting_node.fillPipe('red')

#mouse

#Look direction
#see if above cell has connecting direction
#if so move to that cell and fill it in
#repeat till starting cell

print(f'Starting Cell -> X:{starting_location[0]}, Y:{starting_location[1]}')
current_cell = nodes[starting_node.y][starting_node.x]
current_cell.visited = True
print(f'Current Cell -> X:{current_cell.x}, Y:{current_cell.y}')

at_start = False
steps = 0

while not ((current_cell.x == starting_location[0]) and (current_cell.y == starting_location[1]+1)):
#while not next_cell.visited:
#while count+1 <= 150:
    #print('Entered While Loop')
    #print(f'Current Cell -> X:{current_cell.x}, Y:{current_cell.y}')

    steps += 1
    #print(count)

    #Look North
    if (current_cell.y-1 > 0) and (current_cell.direction in ['|', 'J', 'L']):
        #print('Looking North')
        cell_north = nodes[current_cell.y-1][ current_cell.x]
        #print(f'Cell North Cords -> X:{cell_north.x}, Y:{cell_north.y}')
        if (cell_north.direction in ('|', 'F', '7')) and not cell_north.visited:
            #print('Found Cell')
            current_cell = cell_north
            current_cell.fillPipe('green')
            current_cell.visited = True
            continue
    #Look West
    if (current_cell.x-1 > 0) and (current_cell.direction in ['-', 'J', '7']):
        #print('Looking West')
        cell_west = nodes[current_cell.y][current_cell.x-1]
        if cell_west.direction in ('-', 'F', 'L') and not cell_west.visited:
            #print('Found Cell')
            current_cell = cell_west
            current_cell.fillPipe('green')
            current_cell.visited = True
            continue

    #Look South
    if (current_cell.y+1 < len(nodes)) and (current_cell.direction in ['|', 'F', '7']):
        #print('Looking South')
        cell_south = nodes[current_cell.y+1][current_cell.x]
        if cell_south.direction in ('|', 'L', 'J') and not cell_south.visited:
            #print('Found Cell')
            current_cell = cell_south
            current_cell.fillPipe('green')
            current_cell.visited = True
            continue

    #Look East
    if (current_cell.x+1 < len(nodes[0])) and (current_cell.direction in ['-', 'L', 'F']):
        #print('Looking East')
        cell_east = nodes[current_cell.y][current_cell.x+1]
        if cell_east.direction in ('-', '7', 'J') and not cell_east.visited:
            #print('Found Cell')
            current_cell = cell_east
            current_cell.fillPipe('green')
            current_cell.visited = True
            continue

print(f'Part 1 Answer: {(steps+1)/2}')


root.mainloop()


