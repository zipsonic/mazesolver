from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.__root = Tk()
        self.__root.geometry(f"{width}x{height}")
        self.__root.title("MazeSolver")
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
        )

class Cell:
    def __init__(self,top_left,bottom_right,window):
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.x1 = top_left.x
        self.y1 = top_left.y
        self.x2 = bottom_right.x
        self.y2 = bottom_right.y
        self.window = window
        self.visited = False

    def draw(self):

        if self.has_top_wall:
            top_color = "black"
        else:
            top_color = "#d9d9d9"
        point1 = Point(self.x1,self.y1)
        point2 = Point(self.x2,self.y1)
        self.window.draw_line(Line(point1,point2),top_color)
            
        if self.has_right_wall:
            right_color = "black"
        else:
            right_color = "#d9d9d9"
        point1 = Point(self.x2,self.y1)
        point2 = Point(self.x2,self.y2)
        self.window.draw_line(Line(point1,point2),right_color)
            
        if self.has_bottom_wall:
            bottom_color = "black"
        else:
            bottom_color = "#d9d9d9"
        point1 = Point(self.x1,self.y2)
        point2 = Point(self.x2,self.y2)
        self.window.draw_line(Line(point1,point2),bottom_color)
            
        if self.has_left_wall:
            left_color = "black"
        else:
            left_color = "#d9d9d9"
        point1 = Point(self.x1,self.y1)
        point2 = Point(self.x1,self.y2)
        self.window.draw_line(Line(point1,point2),left_color)

    def get_center(self,axis):
        if axis == "x":
            return (self.x1+self.x2)/2
        else:
            return (self.y1+self.y2)/2

    def draw_move(self, to_cell, undo=False):
        
        if undo:
            color = "gray"
        else:
            color = "red"

        point1=Point(self.get_center("x"),self.get_center("y"))
        point2=Point(to_cell.get_center("x"),to_cell.get_center("y"))
        
        self.window.draw_line(Line(point1,point2),color)


