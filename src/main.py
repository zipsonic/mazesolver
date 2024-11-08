from window import *
from maze import *

def main():
    win = Window(800,600)

    maze = Maze(10,10,14,19,40,40,win)

    maze.solve()

    win.wait_for_close()


main()