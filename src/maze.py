from window import *
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range (self.num_cols):
            col_list = []
            for j in range (self.num_rows):
                col_list.append(Cell(Point(1,1),Point(1,1),self.win))
            self._cells.append(col_list)
        for i in range (self.num_cols):
            for j in range (self.num_rows):
                self._draw_cell(i,j)
        self._break_entrance_and_exit(i,j)
    
    def _draw_cell(self, i, j):
        self._cells[i][j].x1 = self.x1 + (i * self.cell_size_x)
        self._cells[i][j].x2 = self.x1 + ((i+1) * self.cell_size_x)
        self._cells[i][j].y1 = self.y1 + (j * self.cell_size_y)
        self._cells[i][j].y2 = self.y1 + ((j+1) * self.cell_size_x)
        self._cells[i][j].draw()
        self._animate()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self,i,j):
        self._cells[0][0].has_left_wall = False
        self._cells[i][j].has_right_wall = False
        self._draw_cell(0,0)
        self._draw_cell(i,j)

    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
        while True:
            test_list = []
            if i-1 >= 0 and not self._cells[i-1][j].visited:
                test_list.append((i-1,j,"left"))
            if j-1 >= 0 and not self._cells[i][j-1].visited:
                test_list.append((i,j-1,"top"))
            if i+1 < self.num_cols and not self._cells[i+1][j].visited:
                test_list.append((i+1,j,"right"))
            if j+1 < self.num_rows and not self._cells[i][j+1].visited:
                test_list.append((i,j+1,"bottom"))

            if len(test_list) == 0:
                self._draw_cell(i,j)
                return
            
            rand = random.randint(0,len(test_list)-1)

            match test_list[rand][2]:
                case "top":
                    self._cells[i][j].has_top_wall = False
                    self._cells[test_list[rand][0]][test_list[rand][1]].has_bottom_wall = False

                case "right":
                    self._cells[i][j].has_right_wall = False
                    self._cells[test_list[rand][0]][test_list[rand][1]].has_left_wall = False

                case "bottom":
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[test_list[rand][0]][test_list[rand][1]].has_top_wall = False

                case "left":
                    self._cells[i][j].has_left_wall = False
                    self._cells[test_list[rand][0]][test_list[rand][1]].has_right_wall = False

            self._break_walls_r(test_list[rand][0],test_list[rand][1])

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False


    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self,i,j):
        self._animate()

        self._cells[i][j].visited = True

        if i == self.num_cols-1 and j == self.num_rows-1:
            return True
        
        if i != 0 and j !=0 and not self._cells[i][j].has_left_wall and not self._cells[i-1][j].visited:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            pathfound = self._solve_r(i-1,j)
            if pathfound:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j],True)

        if not self._cells[i][j].has_top_wall and not self._cells[i][j-1].visited:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            pathfound = self._solve_r(i,j-1)
            if pathfound:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1],True)

        if not self._cells[i][j].has_right_wall and not self._cells[i+1][j].visited:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            pathfound = self._solve_r(i+1,j)
            if pathfound:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j],True)

        if not self._cells[i][j].has_bottom_wall and not self._cells[i][j+1].visited:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            pathfound = self._solve_r(i,j+1)
            if pathfound:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1],True)
    
        return False