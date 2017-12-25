# coding=UTF8
# Python TicTacToe game with tkinter for gui and minimax AI
# Author: Pritesh Ranjan <pranjan341@gmail.com>

import sys
from random import randint
from tkinter import Tk, Button
from tkinter import messagebox
#import invincible

class TicTacToe:
    computer = "O"
    opponent = "X"
    size = 3

    def __init__(self):
        self.empty = "*"
        self.active_player = self.opponent
        self.move_id = {}
        self.box = {}
        self.winning = []
        self.game = Tk()
        self.game.title("The invincible Tic-Tac-Toe")
        self.game.resizable(width=False, height=False)
        button_clicked = lambda: self.play_again()
        button = Button(self.game, text='Play Again', command=button_clicked)
        button.grid(row=4, column=0, columnspan=1, sticky="WE")
        button_clicked = lambda: self.quit_game()
        button = Button(self.game, text='Quit Game', command=button_clicked)
        button.grid(row=4, column=2, columnspan=1, sticky="WE")
        self.buttons_setup()

    def buttons_setup(self):
        for x in range(self.size):
            for y in range(self.size):
                button_clicked = lambda x=x, y=y: self.on_button_click(x, y)
                self.box[x, y] = Button(self.game, text=self.empty, background="white", command=button_clicked, width=15, height=10)
                self.box[x, y].grid(row=x, column=y)
                self.move_id[x, y] = self.empty

    def on_button_click(self, x, y):
        self.set_layout(x, y)
        self.move_id[x, y] = self.active_player
        if self.check_winner(x, y):
            return True
        if self.active_player == self.opponent:
            self.active_player = self.computer
            self.autoplay()
        else:
            self.active_player = self.opponent
        self.game.title("The invincible Tic Tac Toe Game Player: {}".format(self.active_player))

    def set_layout(self, x, y):
        self.box[x, y]["text"] = self.active_player
        self.box[x, y]["state"] = "disabled"
        self.box[x, y]["background"] = "black"

    def play_again(self):
        self.game.title("The invincible Tic-Tac-Toe")
        self.active_player = self.opponent
        self.buttons_setup()

    def quit_game(self):
        #print(self.move_id)
        sys.exit()
    
    def check_draw(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.move_id[x, y] == self.empty:
                    return False
        print("tie")
        messagebox.showinfo(title="Whoaa !!", message="The game ends in a draw. Play again.")
        self.play_again()
               

    def check_winner(self, x, y):
        print(self.move_id[x, y], x, y)
        #column
        if (self.move_id[0, y] == self.move_id[1, y] == self.move_id[2, y] == self.active_player):
            self.winning = []
            self.winning = ((0, y), (1, y), (2, y))
            self.announce_winner()
            return True
        #row
        if (self.move_id[x, 0] == self.move_id[x, 1] == self.move_id[x, 2] == self.active_player):
            self.winning = []
            self.winning = ((x, 0), (x, 1), (x, 2))
            self.announce_winner()
            return True
        #diagonal1
        if (x == y and self.move_id[0, 0] == self.move_id[1, 1] == self.move_id[2, 2] == self.active_player):
            self.winning = []
            self.winning = ((0,0), (1,1), (2,2))
            self.announce_winner()
            return True
        #diagonal2
        if (x + y == 2 and self.move_id[0, 2] == self.move_id[1, 1] == self.move_id[2, 0] == self.active_player):
            self.winning = []
            self.winning = ((0, 2), (1, 1), (2, 0))
            self.announce_winner()
            return True
        else:
            self.check_draw()
            return False

    def announce_winner(self):
        print('winner is {}'.format(self.active_player))
        for x, y in self.winning:
            self.box[x, y]['disabledforeground'] = 'red'
        messagebox.showinfo(title="Congrats", message="Player {} has won".format(self.active_player))
        self.game.title("The invincible Tic Tac Toe Game")
        self.play_again()

    def autoplay(self):
        empty_boxes = []
        for x in range(self.size):
            for y in range(self.size):
                if self.move_id[x, y] == self.empty:
                    empty_boxes.append((x, y))
        rand_index = randint(0, len(empty_boxes)-1)
        self.on_button_click(*empty_boxes[rand_index])


    def mainloop(self):
        self.game.mainloop()

if __name__ == '__main__':
    TicTacToe().mainloop()
