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
ActivePlayer=1
p1=[] #what player 1 selects
p2=[] #what player 2 selects

root = Tk()
root.title("The Undefeatable Tic Tac Toe Game")
but = {}
def Gui():
	for x in range(3):
		for y in range(3):
			handler = lambda x=x,y=y: ButtonClick(x,y)
			but[x,y]= Button(root,  command=handler, width=15, height=10)
			but[x,y].grid(row=y, column=x)

	handler=lambda : PlayAgain()
	button = Button(root, text='Play Again', command=handler)
	button.grid(row=4, column=0, columnspan=1, sticky="WE")
	
	handler=lambda : QuitGame()
	button = Button(root, text='Quit Game', command=handler)
	button.grid(row=4, column=2, columnspan=1, sticky="WE")
			
def QuitGame():
	sys.exit()
	
def PlayAgain():
	Gui()

# function
def ButtonClick(y,x):
	global ActivePlayer, p1, p2
	if (ActivePlayer==1):
		SetLayout(x,y,"X")
		root.title("The Undefeatable Tic Tac Toe Game Player: X")
		ActivePlayer=2
	else:
		SetLayout(x,y,"O")
		root.title("The Undefeatable Tic Tac Toe Game Player: O")
		ActivePlayer=1		

def SetLayout(y, x, PlayerSymbol):
	but[x,y]['text'] = PlayerSymbol
	but[x,y]['state'] = 'disabled'
	but[x,y]['background'] ='black'




Gui()
root.mainloop()