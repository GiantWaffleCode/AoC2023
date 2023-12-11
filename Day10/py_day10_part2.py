#   Advent of Code 2023
#      GiantWaffle
#   Challenge 10 of 25
#      Part 2 of 2
# -----------------------

from tkinter import *
from PIL import ImageGrab, Image
import os.path

use_real_data = True

data = []

with open('Day10\data_day10.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = [
    '.....',
    '.F-7.',
    '.|S|.',
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
        self.inside = False

        self.conn_fwd = Node
        self.conn_bwd = Node

        self.drawPipe()

    def drawHorLine(self, canvas, x, y):
        canvas.create_line(7*x+2, 7*y+3, 7*x+9, 7*y+3)

    def drawVertLine(self, canvas, x, y):
        canvas.create_line(7*x+3, 7*y+2, 7*x+3, 7*y+9)

    def drawNELine(self, canvas, x, y):
        canvas.create_line(7*x+3, 7*y+3, 7*x+9, 7*y+3)
        canvas.create_line(7*x+3, 7*y+2, 7*x+3, 7*y+4)

    def drawSELine(self, canvas, x, y):
        canvas.create_line(7*x+3, 7*y+3, 7*x+9, 7*y+3)
        canvas.create_line(7*x+3, 7*y+3, 7*x+3, 7*y+9)

    def drawNWLine(self, canvas, x, y):
        canvas.create_line(7*x+2, 7*y+3, 7*x+4, 7*y+3)
        canvas.create_line(7*x+3, 7*y+2, 7*x+3, 7*y+4)

    def drawSWLine(self, canvas, x, y):
        canvas.create_line(7*x+2, 7*y+3, 7*x+4, 7*y+3)
        canvas.create_line(7*x+3, 7*y+3, 7*x+3, 7*y+9)

    def drawBlank(self, canvas, x, y, fill):
        canvas.create_line(7*x+2, 7*y+2, 7*x+9, 7*y+2, fill=fill)
        canvas.create_line(7*x+2, 7*y+3, 7*x+9, 7*y+3, fill=fill)
        canvas.create_line(7*x+2, 7*y+4, 7*x+9, 7*y+4, fill=fill)
        canvas.create_line(7*x+2, 7*y+5, 7*x+9, 7*y+5, fill=fill)
        canvas.create_line(7*x+2, 7*y+6, 7*x+9, 7*y+6, fill=fill)
        canvas.create_line(7*x+2, 7*y+7, 7*x+9, 7*y+7, fill=fill)
        canvas.create_line(7*x+2, 7*y+8, 7*x+9, 7*y+8, fill=fill)
        canvas.create_line(7*x+5, 7*y+5, 7*x+6, 7*y+6, fill='red')


    def drawPipe(self):
        match self.direction:
            case '|':
                self.drawVertLine(my_canvas, self.x, self.y)
            case '-':
                self.drawHorLine(my_canvas, self.x, self.y)
            case 'L':
                self.drawNELine(my_canvas, self.x, self.y)
            case 'J':
                self.drawNWLine(my_canvas, self.x, self.y)
            case '7':
                self.drawSWLine(my_canvas, self.x, self.y)
            case 'F':
                self.drawSELine(my_canvas, self.x, self.y)

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

def get_color(image, cord):
    return image.getpixel((cord[0], cord[1]))

def getter(widget):
    x=root.winfo_rootx()+widget.winfo_x()
    y=root.winfo_rooty()+widget.winfo_y()
    x1=x+widget.winfo_width()
    y1=y+widget.winfo_height()
    image = ImageGrab.grab().crop((x+2,y+2,x1-2,y1-2))
    image.show()
    image.save('Day10/pipes.png')

if os.path.exists('Day10/pipes.png'):
    pipes = Image.open(r"Day10/pipes.png")
    pixel_map = pipes.load()
else:
    screenshot = root.after(2000, lambda: getter(my_canvas))


#go line by line
#if cell is visited already exclude it
#if cell has not been visited
#raycast from center to edge in all 4 directions
#if black pixels 

#generate blank map
for node_line in nodes:
    for cell in node_line:
        if not cell.visited:
            cell.drawBlank(my_canvas, cell.x, cell.y, 'grey')
        
def raycastOut(x, y):
    total = [0,0,0,0] #[U D L R]
    px_cord = [7*x+3, 7*y+3]
    width, height = pipes.size

    for up in range(0, px_cord[1]):
        if pixel_map[px_cord[0], up] == (0, 0, 0):
            total[0] += 1

    for down in range(px_cord[1], height):
        if pixel_map[px_cord[0], down] == (0, 0, 0):
            total[1] += 1

    for left in range(0, px_cord[0]):
        if pixel_map[left, px_cord[1]] == (0, 0, 0):
            total[2] += 1

    for right in range(px_cord[0], width):
        if pixel_map[right, px_cord[1]] == (0, 0, 0):
            total[3] += 1

    return total


def raycastOutDiag(x, y):
    total = [0,0,0,0] #[NW NE SW SE]
    px_cord = [7*x+3, 7*y+3]
    width, height = pipes.size
    print(width, height)

    if px_cord[0] > px_cord[1]:
        dist_nw = px_cord[1]
    else:
        dist_nw = px_cord[0]
    for nw in range(dist_nw):
        if pixel_map[px_cord[0]-nw, px_cord[1]-nw] == (0, 0, 0):
            total[0] += 1

    if width-px_cord[0] > px_cord[1]:
        dist_ne = px_cord[1]
    else:
        dist_ne = width-px_cord[0]
    for ne in range(dist_ne):
        if pixel_map[px_cord[0]+ne, px_cord[1]-ne] == (0, 0, 0):
            total[1] += 1

    if px_cord[0] > height-px_cord[1]:
        dist_sw = height-px_cord[1]
    else:
        dist_sw = px_cord[0]
    for sw in range(dist_sw):
        if pixel_map[px_cord[0]-sw, px_cord[1]+sw] == (0, 0, 0):
            total[2] += 1

    if width-px_cord[0] > height-px_cord[1]:
        dist_se = height-px_cord[1]
    else:
        dist_se = width-px_cord[0]
    for se in range(dist_se):
        if pixel_map[px_cord[0]+se, px_cord[1]+se] == (0, 0, 0):
            total[3] += 1      

    return total

def isRaycastOdd(raycast):
    isOdd = [False, False, False, False]

    if 0 in raycast:
        return False

    for i, cast in enumerate(raycast):
        if cast == 1:
            isOdd[i] = True
        elif cast % 2 != 0:
            isOdd[i] = True
        else:
            isOdd[i] = False
        
    return all(isOdd)


#raycast all non pipe cells
for y, node_line in enumerate(nodes):
    for x, cell in enumerate(node_line):
        if not cell.visited:
            raycast = raycastOut(x, y)
            print(f'Pixel: ({x},{y}) -> Raycast: {raycast}')
            if isRaycastOdd(raycast):
                print('Inside Cell Found')
                cell.inside = True

inside_count = 0

#generate inside map
for node_line in nodes:
    for cell in node_line:
        if cell.inside:
            cell.drawBlank(my_canvas, cell.x, cell.y, 'yellow')
            inside_count += 1

#pixel_color = root.after(3000, lambda: get_color(screenshot, [0,0]))
#root.after(3500, lambda: print(pixel_color))

print(f'Part 2 Answer: {inside_count}')

root.mainloop()




