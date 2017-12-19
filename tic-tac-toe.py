# coding=UTF8

# Author: Pritesh Ranjan

import sys
if sys.version_info >= (3, 0):
  from tkinter import Tk, Button
  from tkinter.font import Font
  from tkinter import messagebox
else:
  from Tkinter import Tk, Button
  from tkFont import Font
  from Tkinter import messagebox


#Global Variables
computer = 'O'
opponent = 'X'
ActivePlayer = opponent
p={} #what current player  selects
turns=0

root = Tk()
root.resizable(width=False, height=False)
root.title("The Undefeatable Tic Tac Toe Game")

but = {}
def Gui():
	for x in range(3):
		for y in range(3):
			func = lambda x=x,y=y: ButtonClick(x,y)
			but[x,y]= Button(root, text=' ', command=func, width=15, height=10)
			but[x,y].grid(row=y, column=x)
			p[x,y]='.'

	func=lambda : PlayAgain()
	button = Button(root, text='Play Again', command=func)
	button.grid(row=4, column=0, columnspan=1, sticky="WE")
	
	func=lambda : QuitGame()
	button = Button(root, text='Quit Game', command=func)
	button.grid(row=4, column=2, columnspan=1, sticky="WE")
			
def QuitGame():
	print(p)
	sys.exit()
	
def PlayAgain():
	Gui()

# function
def ButtonClick(y,x):
	global ActivePlayer, p, turns
	if (ActivePlayer==opponent):
		turns=turns+1
		SetLayout(x,y,ActivePlayer)
		p[x,y] = ActivePlayer
		root.title("The Undefeatable Tic Tac Toe Game Player: X")
		a,b=CheckWinner(x,y)
		if a:
			turns=0
			winner(ActivePlayer,b)
		ActivePlayer= computer
	else:
		turns=turns+1
		SetLayout(x,y,ActivePlayer)
		p[x,y] = computer
		root.title("The Undefeatable Tic Tac Toe Game Player: O")
		a,b=CheckWinner(x,y)
		if a:
			turns=0
			winner(ActivePlayer,b)
		ActivePlayer=opponent

	if turns==9:
		print('tie')
		messagebox.showinfo(title="Whoaa !!", message="The game ends in a draw. Play again.")
		PlayAgain()



def SetLayout(y, x, PlayerSymbol):
	but[x,y]['text'] = PlayerSymbol
	but[x,y]['state'] = 'disabled'
	but[x,y]['background'] ='black'


def winner(ActivePlayer, winning):
	print('winner is {}'.format(ActivePlayer))
	for x,y in winning:
		but[y,x]['disabledforeground'] = 'red'
	messagebox.showinfo(title="Congrats", message="Player {} has won".format(ActivePlayer))
	PlayAgain()



def CheckWinner(x,y):
	print(p[x,y], x, y)
	#column
	if (p[0,y] == p[1,y] == p[2,y] == ActivePlayer):
		winning=[]
		winning=((0,y),(1,y),(2,y))
		return True, winning

	#row
	if (p[x,0] == p[x,1] == p[x,2] == ActivePlayer):
		winning=[]
		winning=((x,0),(x,1),(x,2))
		return True, winning

    #diagonal1
	if (x == y and p[0,0] == p[1,1] == p[2,2] == ActivePlayer):
		winning=[]
		winning=((0,0),(1,1),(2,2))
		return True, winning

    #diagonal2
	if (x + y == 2 and p[0,2] == p[1,1] == p[2,0] == ActivePlayer):
		winning=[]
		winning=((0,2),(1,1),(2,0))
		return True, winning

	return False, None  

			

Gui()
root.mainloop()