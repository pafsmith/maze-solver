from cell import Cell
import random
import time


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
        seed=None,
    ):
        self.__cells = []
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__seed = seed
        if seed is not None:
            random.seed(seed)

       
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0) 

    def __create_cells(self):
        for i in range(self.__num_cols):
            col_cells = []
            for j in range(self.__num_rows):
                col_cells.append(Cell(self.__win))
            self.__cells.append(col_cells)
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        if self.__win is None:
            return
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.01)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)
    
    def __break_walls_r(self, i, j):
        self.__cells[i][j]._Cell__visited = True
        while True:
            to_visit = []
           
            if i > 0 and not self.__cells[i - 1][j]._Cell__visited:
                to_visit.append((i - 1, j))
        
            if i < self.__num_cols - 1 and not self.__cells[i + 1][j]._Cell__visited:
                to_visit.append((i + 1, j))
        
            if j > 0 and not self.__cells[i][j - 1]._Cell__visited:
                to_visit.append((i, j - 1))
           
            if j < self.__num_rows - 1 and not self.__cells[i][j + 1]._Cell__visited:
                to_visit.append((i, j + 1))

            if not to_visit:
                self.__draw_cell(i, j)
                return

            direction = random.choice(to_visit)
            next_i, next_j = direction

            if next_i == i - 1:  
                self.__cells[i][j].has_left_wall = False
                self.__cells[i - 1][j].has_right_wall = False
            elif next_i == i + 1:  
                self.__cells[i][j].has_right_wall = False
                self.__cells[i + 1][j].has_left_wall = False
            elif next_j == j - 1:  
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j - 1].has_bottom_wall = False
            elif next_j == j + 1:  
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j + 1].has_top_wall = False
            
            self.__draw_cell(i,j) 
            self.__break_walls_r(next_i, next_j)

        
