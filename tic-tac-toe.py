# coding=UTF8

# Author: Pritesh Ranjan pranjan341@gmail.com

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

root = Tk()
root.resizable(width=False, height=False)
root.title("The Undefeatable Tic Tac Toe Game")

but = {}
def Gui():
	for x in range(3):
		for y in range(3):
			func = lambda x=x,y=y: ButtonClick(x,y)
			but[x,y]= Button(root,  command=func, width=15, height=10)
			but[x,y].grid(row=y, column=x)

	func=lambda : PlayAgain()
	button = Button(root, text='Play Again', command=func)
	button.grid(row=4, column=0, columnspan=1, sticky="WE")
	
	func=lambda : QuitGame()
	button = Button(root, text='Quit Game', command=func)
	button.grid(row=4, column=2, columnspan=1, sticky="WE")
			
def QuitGame():
	sys.exit()
	
def PlayAgain():
	Gui()

# function
def ButtonClick(y,x):
	global ActivePlayer, p
	if (ActivePlayer==opponent):
		SetLayout(x,y,ActivePlayer)
		p[x,y] = ActivePlayer
		print(p[x,y], x, y)
		root.title("The Undefeatable Tic Tac Toe Game Player: X")
		ActivePlayer= computer

	else:
		SetLayout(x,y,ActivePlayer)
		p[x,y] = computer
		print(p[x,y], x, y)
		root.title("The Undefeatable Tic Tac Toe Game Player: O")
		ActivePlayer=opponent

	#CheckWinner()		

def SetLayout(y, x, PlayerSymbol):
	but[x,y]['text'] = PlayerSymbol
	but[x,y]['state'] = 'disabled'
	but[x,y]['background'] ='black'

#def CheckWinner():
	#row



Gui()
root.mainloop()