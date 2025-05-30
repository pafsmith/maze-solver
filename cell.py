from window import Line, Point


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win
        self.__visited = False

    def draw(self, x1, y1, x2, y2):
        if self.__win is None:
            return
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line, "black")
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line, "black")
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line, "black")
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line, "black")
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        if self.__win is None:
            return

        if undo:
            color = "gray"
        else:
            color = "red"

        center_x_self = (self.__x1 + self.__x2) / 2
        center_y_self = (self.__y1 + self.__y2) / 2

        center_x_to_cell = (to_cell.__x1 + to_cell.__x2) / 2
        center_y_to_cell = (to_cell.__y1 + to_cell.__y2) / 2

        line = Line(Point(center_x_self, center_y_self), Point(center_x_to_cell, center_y_to_cell))

        self.__win.draw_line(line, color)