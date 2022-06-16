import numpy as np
import random as rand
import matplotlib.pyplot as plt
from matplotlib import animation
import math
import matplotlib.patches as patches

class MazeCreator:
    def __init__(self,size: int):

        self.h_walls = np.array([True] * size*(size-1))
        self.h_walls = np.reshape(self.h_walls, (size-1,size))
        
        self.v_walls = np.array([True] * size*(size-1))
        self.v_walls = np.reshape(self.v_walls, (size,size-1))

        self.all_walls = [self.h_walls,self.v_walls]
        
        self.history = [[np.copy(self.all_walls[0]),np.copy(self.all_walls[1])]] 
        
        cells = np.array([False]* size**2)
        cells = np.reshape(cells, (size,size))

        start = rand.choice(range(size**2))
        row = int(start % size)
        col = int((start-row)/size)
        cells[row,col] = True
        cell_walls = [(0,-1,0),(0,0,0),(1,0,-1),(1,0,0)]
        list = set()
        for wall in cell_walls:
            if row+wall[1]>=0 and col+wall[2]>=0:
                list.add((0+wall[0],row+wall[1],col+wall[2]))

        while len(list)>0:
            n_wall = rand.sample(list,1)
            n_wall = n_wall[0]
            if cells[n_wall[1],n_wall[2]]==False:
                row,col = n_wall[1],n_wall[2]
                cells[row,col] = True
                self.all_walls[n_wall[0]][n_wall[1],n_wall[2]] = False
                self.history.append([np.copy(self.all_walls[0]),np.copy(self.all_walls[1])])
                for  wall in cell_walls:
                    if row+wall[1]>=0 and col+wall[2]>=0:
                        list.add((0+wall[0],row+wall[1],col+wall[2])) 
            elif n_wall[0]==0 and n_wall[1]+1 < size and cells[n_wall[1]+1,n_wall[2]]==False:
                row,col = n_wall[1]+1,n_wall[2]
                cells[row,col] = True
                self.all_walls[n_wall[0]][n_wall[1],n_wall[2]] = False
                self.history.append([np.copy(self.all_walls[0]),np.copy(self.all_walls[1])])
                for  wall in cell_walls:
                    if row+wall[1]>=0 and col+wall[2]>=0:
                        list.add((0+wall[0],row+wall[1],col+wall[2]))
            elif n_wall[0]==1 and n_wall[2]+1 < size and cells[n_wall[1],n_wall[2]+1]==False:
                row,col = n_wall[1],n_wall[2]+1
                cells[row,col] = True
                self.all_walls[n_wall[0]][n_wall[1],n_wall[2]] = False
                self.history.append([np.copy(self.all_walls[0]),np.copy(self.all_walls[1])])
                for  wall in cell_walls:
                    if row+wall[1]>=0 and col+wall[2]>=0:
                        list.add((0+wall[0],row+wall[1],col+wall[2])) 
            list.remove(n_wall)

        
        
        
        """
        maze = np.array([False]* size**2)
        self.maze = np.reshape(maze,(size,size))

        
        self.history = [np.copy(self.maze)]

        #create random maze using randomized prim algorithm
        
        start = rand.choice(range(size**2))
        list = set()
        col = int(start % size)
        row = int((start -col)/size)
        self.maze[row,col] = True
        self.history.append(np.copy(self.maze))
        if col > 0 and not self.maze[row,col-1]:
            list.add(row*size+col-1)
        if col < size-1 and not self.maze[row,col+1]:
            list.add(row*size+col+1)
        if row < size-1 and not self.maze[row+1,col]:
            list.add((row+1)*size+col)
        if row > 0 and not self.maze[row-1,col]:
            list.add((row-1)*size+col)
        while len(list)>0:
            cell = rand.sample(list,1)
            cell = cell[0]
            list.remove(cell)
            count = 0
            col = int(cell % size)
            row = int((cell - col)/size)
            if col > 0 and self.maze[row,col-1]:
                count+=1
            if col < size-1 and self.maze[row,col+1]:
                count+=1
            if row < size-1 and self.maze[row+1,col]:
                count+=1
            if row > 0 and self.maze[row-1,col]:
                count+=1
            if count==1:
                self.maze[row,col] = True
                self.history.append(np.copy(self.maze))
                if col > 0 and not self.maze[row,col-1]:
                    list.add(row*size+col-1)
                if col < size-1 and not self.maze[row,col+1]:
                    list.add(row*size+col+1)
                if row < size-1 and not self.maze[row+1,col]:
                    list.add((row+1)*size+col)
                if row > 0 and not self.maze[row-1,col]:
                    list.add((row-1)*size+col)
        """
        
    def get_history(self):
        return self.history

    

    
#main
#choose size of maze (maze is square size*size)
size = 40
    
m =  MazeCreator(size)
history = m.get_history()



fig = plt.figure(figsize = (7.2,7.2))


ax = fig.add_subplot(111)

plt.show(block=False)
ax.axis([0,size,0,size])

pch = []
WALL_SIZE = 0.1
grid= []
for row in range(size-1):
    for col in range(size-1):
       ax.add_patch(patches.Rectangle((col+1-WALL_SIZE/2,row+1-WALL_SIZE/2), WALL_SIZE, WALL_SIZE, edgecolor = None, fc='g'))

#vertical walls
for row in range(size-1,-1,-1):
    for col in range(size-1):
        pch.append(patches.Rectangle((col+1-WALL_SIZE/2,row+WALL_SIZE/2), WALL_SIZE, 1-WALL_SIZE, edgecolor = None, fc='g'))

#horizontal walls
for row in range(size,1,-1):
    for col in range(size):
        pch.append(patches.Rectangle((col+WALL_SIZE/2,row-1-WALL_SIZE/2), 1-WALL_SIZE, WALL_SIZE, edgecolor = None, fc='g'))

#inside
#for row in range(size-1,-1,-1):
#    for col in range(size):
#        pch.append(patches.Rectangle((col+WALL_SIZE/2,row+WALL_SIZE/2), 1-WALL_SIZE, 1-WALL_SIZE, edgecolor = None, fc='g'))


def init():
    for patch in pch:
        ax.add_patch(patch)
    #for g in grid:
    #    ax.add_patch(g)
    return pch

changed = []

def animate(i):
  
    walls = history[i % len(history)]
    #vertical walls
    count= 0
    for row in range(size):
        for col in range(size-1):          
            if not walls[1][row,col]:
                pch[count].set_facecolor('w')
            else:
                pch[count].set_facecolor('g')
            count+=1
    #horizontal walls
    for row in range(size-1):
        for col in range(size):          
            if not walls[0][row,col]:
                pch[count].set_facecolor('w')
            else:
                pch[count].set_facecolor('g')
            count+=1
    #inside
    #for row in range(size):
    #    for col in range(size):          
    #        if maze[row,col]:
    #            pch[count].set_facecolor('w')
    #        else:
    #            pch[count].set_facecolor('g')
    #        count+=1
    else:
        return pch
    return pch

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(history), interval=4,repeat = False, blit=True)

anim.save('prim_maze_creator.gif')
plt.show()



