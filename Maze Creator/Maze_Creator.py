import numpy as np
import random as rand
import matplotlib.pyplot as plt
from matplotlib import animation
import math
import matplotlib.patches as patches

class MazeCreator:
    def __init__(self,size: int):

        
        
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

        
    def get_history(self):
        return self.history

    

    
#main
#choose size of maze (maze is square size*size)
size = 20
    
m =  MazeCreator(size)
history = m.get_history()



fig = plt.figure(figsize = (10.2,7.2))

ax = fig.add_subplot(111)

plt.show(block=False)
ax.axis([0,size,0,size])

pch = []
for row in range(size):
    for col in range(size):
        pch.append(patches.Rectangle((row, col), 1, 1, color='g'))


def init():
    for patch in pch:
        ax.add_patch(patch)
    return pch

def animate(i):
    maze = history[i % len(history)]
    for row in range(size):
        for col in range(size):
            if maze[row,col]:
                pch[row*size+col].set_color('w')
            else:
                pch[row*size+col].set_color('g')
    return pch

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(history), interval=0.5,repeat = False, blit=True)

#anim.save('a_star.gif')
plt.show()



