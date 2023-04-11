import tkinter as tk

CELL_SIZE = 25
BOARD_WIDTH = 10
BOARD_HEIGHT = 20

BOARD = [[0 for w in range(BOARD_WIDTH)] for h in range(BOARD_HEIGHT)]
BOARD[5][5] = 1

for i in BOARD:
    print(i)


class Cell():
    def __init__(self, w_ind, h_ind):
        self.x1 = w_ind * CELL_SIZE
        self.y1 = h_ind * CELL_SIZE
        self.x2 = (w_ind + 1)* CELL_SIZE
        self.y2 = (h_ind + 1)* CELL_SIZE
        self.color = "#CCCCCC"
        self.border = "#FFFFFF"
    
    def set_color(self, color):
        self.color = color

class Board():
    def __init__(self):
        self.cells = self.create_board(BOARD)
    
    def create_board(self, board):
        cells = []
        for h in range(BOARD_HEIGHT):
            cells_line = []
            for w in range(BOARD_WIDTH):
                cell_num = board[h][w]
                cell = Cell(w, h)
                if cell_num == 1:
                    cell.set_color("#FF0000")
                else:
                    pass
                cells_line.append(cell)
            cells.append(cells_line)
        return cells

    def get_cell(self, x, y):
        return self.cells[y][x]

class Canvas(tk.Canvas):
    def __init__(self, master, board):
        canvas_width = CELL_SIZE * BOARD_WIDTH
        canvas_height = CELL_SIZE * BOARD_HEIGHT
        super().__init__(master, width=canvas_width, height=canvas_height, bg="white")

        self.board = board

        self.render()  
    
    def render(self):
        for h in range(BOARD_HEIGHT):
            for w in range(BOARD_WIDTH):
                cell = self.board.get_cell(w, h)
                print(cell.color)
                self.create_rectangle(cell.x1, cell.y1, cell.x2, cell.y2, 
                                      fill=cell.color, outline=cell.border)
        


class Game():
    def __init__(self, master):
        self.board = Board()
        self.canvas = Canvas(master, self.board)
        self.canvas.place(x=25, y=25)

class EventHandler():
    def __init__(self, game):
        self.runnig = False
        self.block = None
        self.game = game
#定期実行機能の追加

    def start_game(self):
        self.end_game()
        self.running = True
    
    def end_game(self):
        self.running = False 


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("400x600")
        self.title("game")

        game = Game(self)

        EventHandler(game)

def main():
    app = Application()
    app.mainloop()

if __name__ == "__main__":
    main()

