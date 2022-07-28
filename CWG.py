import time
import matplotlib.pyplot as plt
import random


empty_check = []

class cell:
    def __init__(self, y, x):
        self.x = x
        self.y = y

def Empty_Grid( x, y):
    grid = []

    for r in range(0, y):
        grid.append([None for c in range(0, x)])

    return grid

def Check_Neighbor_Cells(grid, x,y):
    neighbor_count = 0
    
    # bottom Row
    if grid[y+1][x-1] == None:
        empty_check.append((x-1,y+1))
    else:
        neighbor_count += 1
    if grid[y+1][x] == None:
        empty_check.append((x,y+1))
    else:
        neighbor_count += 1
    if grid[y+1][x+1] == None:
        empty_check.append((x+1,y+1))
    else:
        neighbor_count += 1

    #middle row
    if grid[y][x-1] == None:
        empty_check.append((x-1,y))
    else:
        neighbor_count += 1
    if grid[y][x+1] == None:
        empty_check.append((x+1,y))
    else:
        neighbor_count += 1
    
    #top row
    if grid[y-1][x-1] == None:
        empty_check.append((x-1,y-1))
    else:
        neighbor_count += 1
    if grid[y-1][x] == None:
        empty_check.append((x,y-1))
    else:
        neighbor_count += 1
    if grid[y-1][x+1] == None:
        empty_check.append((x+1,y-1))
    else:
        neighbor_count += 1

    return neighbor_count

def Empty_Neighbor_Check(grid, x,y):
    neighbor_count = 0
    #Don't crash at edge
    if x+1 >= len(grid):
        return 0
    elif y+1 >= len(grid):
        return 0
    else:
        pass
    if x-1 < 0:
        return 0
    elif y-1 < 0:
        return 0
    else:
        pass
    # bottom Row
    if grid[y+1][x-1] == None:
        pass
    else:
        neighbor_count += 1
    if grid[y+1][x] == None:
        pass
    else:
        neighbor_count += 1
    if grid[y+1][x+1] == None:
        pass
    else:
        neighbor_count += 1

    #middle row
    if grid[y][x-1] == None:
        pass
    else:
        neighbor_count += 1
    if grid[y][x+1] == None:
        pass
    else:
        neighbor_count += 1
    
    #top row
    if grid[y-1][x-1] == None:
        pass
    else:
        neighbor_count += 1
    if grid[y-1][x] == None:
        pass
    else:
        neighbor_count += 1
    if grid[y-1][x+1] == None:
        pass
    else:
        neighbor_count += 1

    return neighbor_count

def Increment_Game(current_generation,next_generation,empty_check):
    for y in range(len(current_generation)):
        for x in range(len(current_generation[y])):
            if current_generation[y][x] == None:
                pass
            else:
                live_cell = current_generation[y][x]
                i = live_cell.x
                j = live_cell.y
                neighbor_count = Check_Neighbor_Cells(current_generation,i,j)
                Life_Rules(neighbor_count,next_generation,x,y)

                while len(empty_check) != 0:
                    coordinates = empty_check.pop()
                    p = coordinates[0] #x
                    l = coordinates[1] #y
                    empty_neighbor_count = Empty_Neighbor_Check(current_generation,p,l)
                    if empty_neighbor_count == 3:
                        next_generation[l][p] = cell(l,p)
                    else:
                        pass 
    return next_generation

def Automate_Game(x,y,tics):
    current_generation = Empty_Grid(x,y)
    next_generation = Empty_Grid(x,y)
    current_generation = Random_Grid_Assignment(current_generation)
    
    #make an autopopulate function to go here | make choices
    """
    current_generation[1][3] = cell(1,3)
    current_generation[1][4] = cell(1,4)
    current_generation[1][5] = cell(1,5)
    current_generation[1][9] = cell(1,9)
    current_generation[1][10] = cell(1,10)
    current_generation[1][11] =cell(1,11)

    current_generation[3][1] = cell(3,1)
    current_generation[3][6] =cell(3,6)
    current_generation[3][8] =cell(3,8)
    current_generation[3][13] =cell(3,13)
    current_generation[4][1] = cell(4,1)
    current_generation[4][6] =cell(4,6)
    current_generation[4][8] =cell(4,8)
    current_generation[4][13] =cell(4,13)
    current_generation[5][1] = cell(5,1)
    current_generation[5][6] =cell(5,6)
    current_generation[5][8] =cell(5,8)
    current_generation[5][13] =cell(5,13)

    current_generation[6][3] = cell(6,3)
    current_generation[6][4] = cell(6,4)
    current_generation[6][5] = cell(6,5)
    current_generation[6][9] = cell(6,9)
    current_generation[6][10] =cell(6,10)
    current_generation[6][11] =cell(6,11)

    current_generation[8][3] = cell(8,3)
    current_generation[8][4] = cell(8,4)
    current_generation[8][5] = cell(8,5)
    current_generation[8][9] = cell(8,9)
    current_generation[8][10] =cell(8,10)
    current_generation[8][11] =cell(8,11)

    current_generation[9][1] = cell(9,1)
    current_generation[9][6] =cell(9,6)
    current_generation[9][8] =cell(9,8)
    current_generation[9][13] =cell(9,13)
    current_generation[10][1] = cell(10,1)
    current_generation[10][6] =cell(10,6)
    current_generation[10][8] =cell(10,8)
    current_generation[10][13] =cell(10,13)
    current_generation[11][1] = cell(11,1)
    current_generation[11][6] =cell(11,6)
    current_generation[11][8] =cell(11,8)
    current_generation[11][13] =cell(11,13)

    current_generation[13][3] = cell(13,3)
    current_generation[13][4] = cell(13,4)
    current_generation[13][5] = cell(13,5)
    current_generation[13][9] = cell(13,9)
    current_generation[13][10] =cell(13,10)
    current_generation[13][11] =cell(13,11)
    """
    #display the first frame
    b = Object2Number(current_generation)
    plt.imshow(b, interpolation='none')
    plt.draw()
    plt.pause(0.0001)
    plt.clf()

    #increment the game for however long specified
    while tics > 0:
        a = Increment_Game(current_generation,next_generation,empty_check)
        
        #continue displaying the rest of the changes
        b = Object2Number(a)
        plt.imshow(b, interpolation='none')
        plt.draw()
        plt.pause(0.000001)
        plt.clf()
        
        current_generation = next_generation
        next_generation = Empty_Grid(x,y)
        time.sleep(0.0000001)
        tics -= 1

def Object2Number(grid):
    number_grid = Empty_Grid(len(grid),len(grid))
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == None:
                number_grid[y][x] = 0
            else:
                number_grid[y][x] = 1
    return number_grid

def Number2Object(grid):
    object_grid = Empty_Grid(len(grid),len(grid))
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                object_grid[y][x] = None
            else:
                object_grid[y][x] = cell(y,x)
    return object_grid
    
def Random_Grid_Assignment(grid):
    # outputs a number grid
    number_grid = Object2Number(grid)
    #creates a list to make odds of 1 or 0 into a percentage
    odds = [1] * 5 + [0] * 20 

    
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if x == 0 or x ==1 :
                pass
            elif y == 0 or y == 1:
                pass
            elif x == (len(grid)-1) or x == (len(grid)-2):
                pass
            elif y == (len(grid)-1) or y == (len(grid)-2):
                pass
            else:
                number_grid[y][x] = random.choice(odds)
    return Number2Object(number_grid)

def Life_Rules(neighbor_count, next_generation,x,y):
    if neighbor_count == 2:
        next_generation[y][x] = cell(y,x)
    elif neighbor_count == 3:
        next_generation[y][x] = cell(y,x)
    elif neighbor_count > 3 |  neighbor_count < 2:
        next_generation[y][x] = None

#Automate_Game(100,100,1000)

def main():
    x = int(input("How big of a square do you want?\n"))
    t = int(input("How long should it last?\n"))
    Automate_Game(x,x,t)
main()