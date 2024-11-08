from window import *
from maze import *

def main():

    win = Window(800,600)

    x = (win.width - (20 * 38)) / 2

    y = (win.height - (20 * 28)) /2

    maze = Maze(x,y,28,38,20,20,win)

    maze.solve()

    win.wait_for_close()


main()