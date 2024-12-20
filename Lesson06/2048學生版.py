# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 18:53:53 2018

@author: Eric
"""

import tkinter as tk
import random

class Grid:
    def __init__(self, n):
        self.size = n
        self.cells = self.generate_empty_grid()
        """設定標誌，用來判斷是否壓縮、合併、移動"""
        self.compressed = False
        self.merged = False
        self.moved = False
    
    """生成空的棋盤"""
    def generate_empty_grid(self):
        #建立一個儲存整個二維串列
        emptyGrid = []
        """用二維巢狀迴圈建立二維串列"""
        for i in range():
            #建立一個儲存"列"的串列
            rowGrid = []
            for j in range():
                rowGrid.append()
                
            emptyGrid.append()
                
        return 
    
    """取得所有空的格子"""
    def retrieve_empty_cells(self):
        #建立一個儲存所有空格子的串列
        empty_cells = []
        """用二維朝狀迴圈掃過網格"""
        for i in range(self.size):
            for j in range(self.size):
                """如果該格子等於0,則在empty_cells新增"""
                if self.cells[i][j] == :
                    empty_cells.append((i, j))
                    
        return 
    
    """隨機選一個空的棋格生成數字2"""
    def random_cell(self):
        cell = random.choice()
        """把取到的元祖資料分別存入i和j"""
        i = 
        j = 
        self.cells[i][j] = 2
        
    """直接設定格子"""
    def set_cells(self, col , row , num):
        """直接設定格子的數值"""
        
    """清除標誌"""
    def clear_flags(self):
        self.compressed = False
        self.merged = False
        self.moved = False
        
    """向左壓縮"""
    def left_compress(self):
        self.compressed = False
        """重新生成一個空的二為串列網格，儲存至new_grid"""
        new_grid = self.generate_empty_grid()
        
        """用二維網格掃過網格"""
        for i in range(self.size):
            count = 0
            for j in range(self.size):
                """如果該格子的值不等於0，則進行壓縮"""
                if self.cells[i][j] != 0:
                    new_grid[i][count] = self.cells[i][j]
                    """如果count不等於j，則表示有進行過壓縮"""
                    if count != j:
                        self.compressed = True
                    """若成功進行壓縮，count值加一"""
                    count += 1
        """全部壓縮完後，將舊的網格取代成新的網格"""
        self.cells = new_grid
    
    """向上壓縮"""
    def up_compress(self):
        self.compressed = False
        """重新生成一個空的二為串列網格，儲存至new_grid"""
        new_grid = 
        
        """用二維網格掃過網格"""
        for i in range():
            count = 0
            for j in range():
                """如果該格子的值不等於0，則進行壓縮"""
                if :
                    new_grid[count][i] = 
                    """如果count不等於j，則表示有進行過壓縮"""
                    if :
                        self.compressed = 
                    """若成功進行壓縮，count值加一"""
                    count 
        """全部壓縮完後，將舊的網格取代成新的網格"""
        self.cells = 

    """向右壓縮"""
    def right_compress(self):
        self.compressed = False
        """重新生成一個空的二為串列網格，儲存至new_grid"""
        new_grid = 
        
        """用二維網格掃過網格"""
        for i in range():
            count = self.size -1
            for j in range(self.size -1,-1,-1):
                """如果該格子的值不等於0，則進行壓縮"""
                if :
                    new_grid[i][count] = 
                    """如果count不等於j，則表示有進行過壓縮"""
                    if :
                        self.compressed = 
                    """若成功進行壓縮，count值減一"""
                    count 
        """全部壓縮完後，將舊的網格取代成新的網格"""
        self.cells = 
        
    """向下壓縮"""
    def down_compress(self):
        self.compressed = False
        """重新生成一個空的二為串列網格，儲存至new_grid"""
        new_grid = 
        
        """用二維網格掃過網格"""
        for i in range():
            count = 
            for j in range():
                """如果該格子的值不等於0，則進行壓縮"""
                if :
                    new_grid[][] = self.cells[][]
                    """如果count不等於j，則表示有進行過壓縮"""
                    if :
                        self.compressed = 
                    """若成功進行壓縮，count值減一"""
                    count 
        """全部壓縮完後，將舊的網格取代成新的網格"""
        self.cells = 

    """向左合併"""
    def left_merge(self):
        self.merged = False
        """用二維網格掃過網格(須注意range範圍及串列索引值)"""
        for i in range(self.size):
            """由於cells[i][j+1]會超出索引值，因而此處range放size-1"""
            for j in range(self.size - 1):
                
                """如果數字相同，且不為0則合併"""
                if self.cells[i][j] == self.cells[i][j + 1] \
                and  self.cells[i][j] != 0:
                    """左方數字*2，右方數值等於0"""
                    self.cells[i][j] *= 2
                    self.cells[i][j + 1] = 0
                    self.merged = True
                    
    
    """向上合併"""             
    def up_merge(self):
        self.merged = False
        """用二維網格掃過網格(須注意range範圍及串列索引值)"""
        for i in range():
            for j in range():
                
                """如果數字相同，且不為0則合併"""
                if :
                    """上方數字*2，下方數值等於0"""
                    self.cells[j][i] 
                    self.cells[j+1][i] 
                    self.merged = True
                    
    """向右合併"""               
    def right_merge(self):
        self.merged = False
        """用二維網格掃過網格(須注意range範圍及串列索引值)"""
        for i in range():
            for j in range():
                
                """如果數字相同，且不為0則合併"""
                if :
                    """右方數字*2，左方數值等於0"""
                    self.cells[i][j]
                    self.cells[i][j - 1]
                    self.merged = True
                    
    """向下合併"""             
    def down_merge(self):
        self.merged = False
        """用二維網格掃過網格(須注意range範圍及串列索引值)"""
        for i in range():
            for j in range():
                
                """如果數字相同，且不為0則合併"""
                if :
                    """下方數字*2，上方數值等於0"""
                    self.cells[][]
                    self.cells[][] = 
                    self.merged = True
                    
        """找到2048這個數字"""
    def found_2048(self):
        """用二維網格掃過網格，如果有任一格數值等於2048回傳True，否則為False"""
        

    """有沒有空的格子"""
    def has_empty_cells(self):
        """用二維網格掃過網格，如果有任一格數值為0回傳True，否則為False"""
        

    """是否可以合併"""
    def can_merge(self):
        """用二維網格掃過網格"""
        for i in range():
            for j in range():
                """判斷水平方向是否有相鄰且相同的兩個數字，若有回傳True"""
                if :
                    return True
        """用二維網格掃過網格"""
        for j in range():
            for i in range():
                """判斷垂直方向是否有相鄰且相同的兩個數字，若有回傳True"""
                if :
                    return True
        """如果都找不到則回傳False"""
        return False
    

class GamePanel():
    
    """整體背景顏色"""
    BACKGROUND_COLOR = '#92877d'
    
    """空格子顏色"""
    EMPTY_CELL_COLOR = '#9e948a'
    
    """數字背景顏色"""
    CELL_BACKGROUND_COLOR_DICT = {
        '2': '#eee4da',
        '4': '#ede0c8',
        '8': '#f2b179',
        '16': '#f59563',
        '32': '#f67c5f',
        '64': '#f65e3b',
        '128': '#edcf72',
        '256': '#edcc61',
        '512': '#edc850',
        '1024': '#edc53f',
        '2048': '#edc22e',
        'default': '3c3a32'
    }
    
    """數字字體顏色 """
    CELL_COLOR_DICT = {
        '2': '#776e65',
        '4': '#776e65',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#f9f6f2',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
        'default': '#f9f6f2'
    }
    
    FONT = ('Verdana', 24, 'bold')
    UP_KEYS = ('w', 'W', 'Up')
    LEFT_KEYS = ('a', 'A', 'Left')
    DOWN_KEYS = ('s', 'S', 'Down')
    RIGHT_KEYS = ('d', 'D', 'Right')

    def __init__(self , grid):
        """將grid放入類別屬性內"""
        self.grid = grid
        self.size = grid.size
        """建立一個tkinter主視窗"""
        self.window = tk.Tk()
        """設定視窗標題"""
        self.window.title('2048')
        """設定遊戲背景"""
        self.background = tk.Frame(self.window, bg=self.BACKGROUND_COLOR)
        """建立空串列，用來儲存格子Label"""
        self.cell_labels = []
        
        """初始化文字"""
        """用二維巢狀迴圈建立二維串列"""
        for i in range(self.size):
            #建立一個儲存"列"的串列
            row_labels = []
            for j in range(self.size):
                """背景顏色為EMPTY_CELL_COLOR"""
                """font為剛剛設置的FONT"""
                label = tk.Label(self.background, text='',
                                 bg=self.EMPTY_CELL_COLOR,
                                 font=self.FONT,
                                 width=4, height=2)
                """設定label位置"""
                label.grid(row=i, column=j, padx=10, pady=10)
                """將新增好的Label放入row_labels內"""
                row_labels.append(label)
                """將新增好的row_labels放入cell_labels內"""
            self.cell_labels.append(row_labels)
        self.background.grid()

    """把格子和字上色"""
    def paint(self):
        """用兩個迴圈掃過網格"""
        for i in range(self.size):
            for j in range(self.size):
                
                 #如果那個格子數字是0
                if self.grid.cells[i][j] == 0:
                    """設定該格子的文字為空，背景為MPTY_CELL_COLOR"""
                    self.cell_labels[i][j].configure(
                         text='',
                         bg=GamePanel.EMPTY_CELL_COLOR)
                    
                #如果不是0，則依照字典顏色上色
                #bg->background(背景)
                #fg->foreground(前景)
                else:
                    """cell_text為該格子的數值，轉為字串型態"""
                    cell_text = str(self.grid.cells[i][j])
                    """如果數字超過2048"""
                    if self.grid.cells[i][j] > 2048:
                        """color等於預設值"""
                        bg_color = GamePanel.CELL_BACKGROUND_COLOR_DICT.get('beyond')
                        fg_color = GamePanel.CELL_COLOR_DICT.get('beyond')
                        """如果數字沒超過2048"""
                    else:
                        """color由字典取值"""
                        bg_color = GamePanel.CELL_BACKGROUND_COLOR_DICT.get(cell_text)
                        fg_color = GamePanel.CELL_COLOR_DICT.get(cell_text)
                        
                    self.cell_labels[i][j].configure(
                        text=cell_text,
                        bg=bg_color, fg=fg_color)
                    
            
"""控制整個遊戲流程"""
class Game:
    def __init__(self, grid, panel):
        self.grid = grid
        self.panel = panel
        self.start_cells_num = 2
        self.over = False
        self.won = False

    """遊戲停止(輸了或贏了)"""
    def is_game_terminated(self):
        return self.over or self.won

    """遊戲開始"""
    def start(self):
        self.add_start_cells()
        self.panel.paint()
        self.panel.window.bind('<Key>', self.key_handler)
        self.panel.window.mainloop()

    """開始遊戲後產生的格子"""
    def add_start_cells(self):
        for i in range(self.start_cells_num):
            self.grid.random_cell()

    """判斷有沒有辦法移動(合併)"""
    def can_move(self):
        return self.grid.has_empty_cells() or self.grid.can_merge()

    """當按下鍵盤時所要做的事情"""
    def key_handler(self, event):
        if self.is_game_terminated():
            return

        self.grid.clear_flags()
        key_value = event.keysym
        
        #print('{} key pressed'.format(key_value))
        
        #判斷按下的按鍵是哪個功能
        if key_value in GamePanel.UP_KEYS:
            self.up()
        elif key_value in GamePanel.LEFT_KEYS:
            self.left()
        elif key_value in GamePanel.DOWN_KEYS:
            self.down()
        elif key_value in GamePanel.RIGHT_KEYS:
            self.right()
        else:
            pass

        self.panel.paint()
        
        """如果找到2048"""
        if self.grid.found_2048():
            self.you_win()
        
        """如果已經移動完了，則產生一個隨機數字"""
        if self.grid.moved:
            self.grid.random_cell()


        self.panel.paint()
        
        """如果無法再移動"""
        if not self.can_move():
            self.over = True
            self.game_over()

    """遊戲勝利"""
    def you_win(self):
        if not self.won:
            self.won = True
            print('You Win!')

    """遊戲失敗"""
    def game_over(self):
        print('Game over!')

    def up(self):
        self.grid.up_compress()
        self.grid.up_merge()
        self.grid.moved = self.grid.compressed or self.grid.merged
        self.grid.up_compress()

    def left(self):
        self.grid.left_compress()
        self.grid.left_merge()
        self.grid.moved = self.grid.compressed or self.grid.merged
        self.grid.left_compress()

    def down(self):
        self.grid.down_compress()
        self.grid.down_merge()
        self.grid.moved = self.grid.compressed or self.grid.merged
        self.grid.down_compress()

    def right(self):
        self.grid.right_compress()
        self.grid.right_merge()
        self.grid.moved = self.grid.compressed or self.grid.merged
        self.grid.right_compress()

size = 4
grid = Grid(size)
panel = GamePanel(grid)
game2048 = Game(grid, panel)
game2048.start()


