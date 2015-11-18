# -*- coding:Utf-8 -*-
"many balls moving and bouncing on each other"

#libraries
from tkinter import *
from sys import exit
from random import choice, randint

#datas
TITLE = "Bouncing Balls !"
COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise']

#global variables
gameBalls = {}
gameBallsPrevPositions = {}
gameBallsNewPositions = {}
gameBallsMovements = {}

flagMove, flagBalls = 0, 0
nbBalls = 10
r = 10 #balls radius


#functions
def newGame():
	"clean the gameScreen and start a new game"
	global gameBalls, flagBalls, flagMove
	flagMove = 0
	flagBalls = 1
	gameScreen.delete('all')
	for i in gameBalls:
		gameScreen.delete(i)

	# create the balls of the game
	createBalls(nbBalls)

	# set the first balls movements
	for i in gameBalls:
		gameBallsMovements[i] = [randint(-10, 10), randint(-10, 10)]



def moveBalls():
	"ball movements"
	
	# DEBUG TOOL 1
	print("\n\n=============\n\nGame balls :\n", gameBalls,'\n\nMovement of each balls :\n', gameBallsMovements, '\n\nGame balls previous positions :\n', 
	gameBallsPrevPositions, '\n\nGame balls actual positions :\n', gameBallsNewPositions, "\n\n=============\n\n")

	# move each ball in a random direction
	for i in gameBalls:
		coords = gameScreen.coords(gameBalls[i])
		x, y = coords[0]+10, coords[1]+10 #coordinates of the current ball
		print('ball:', i, ": coords:", coords, "x:",x,"y:", y)
		if checkCollision():
			print("Not implemented")
			#if true, gameBallsMovements change
		else:
			#if false, continue with the same gameBallsMovements
			x = x + gameBallsMovements[i][0] # set the new x position
			y = y + gameBallsMovements[i][1] # set the new y position

		gameScreen.coords(gameBalls[i], x+10, y+10, x-10, y-10) #set the new position in canva
		print('ball:', i, ": new coords:",gameScreen.coords(gameBalls[i]), "x:",x,"y:", y)
		gameBallsPrevPositions[i] = gameBallsNewPositions[i] # set previous positions of the balls before new move being recorded
		gameBallsNewPositions[i] = gameScreen.coords(gameBalls[i]) #set the new position in gameBallsNewPositions

	# DEBUG TOOL 2
	print("\n\n=============\n\n")
	print(list(gameBalls)) # get the ball names
	print(gameBalls['ball1'])
	print("EXAMPLE ball1:", gameBalls['ball1'], 
	"\nprevious coordinates :\nx :", gameBallsPrevPositions['ball1'][0]+10, "y :", gameBallsPrevPositions['ball1'][1]+10, 
	"\nnew coordinates :\nx :", gameBallsNewPositions['ball1'][0]+10, "y :", gameBallsNewPositions['ball1'][1]+10, 
	"\nmovements :\nx :", gameBallsMovements["ball1"][0], 'y :', gameBallsMovements["ball1"][1]) #example with one ball
	print("\n\n=============\n\n")
	
	input('DEBUG MODE >>>')

	if flagMove == 1:
		root.after(50, moveBalls)


def checkCollision():
	"ball collisions"
	return False

def createCanva(w, h, c="light grey"):
	return Canvas(root, width=w, height=h, bg=c)

def createBalls(ballNumber):
	"return a list of oval objects placed in gameScreen"
	b = 1

	while b <= ballNumber:
		color = choice(COLORS)
		x = randint(20, 580)
		y = randint(20, 580)
		ball = gameScreen.create_oval(x+r, y+r, x-r, y-r, fill=color)
		gameBalls["ball"+ str(b)] = ball
		b += 1

	for i in gameBalls:
		gameBallsNewPositions[i] = gameScreen.coords(gameBalls[i])

def setWindow():
	"used to set the window, title, center"
	root.update_idletasks()
	root.title(TITLE)
	root.bind("<Escape>", exitProgram)
	width = root.winfo_width()
	height = root.winfo_height()
	x = (root.winfo_screenwidth()//2)-width//2
	y = (root.winfo_screenheight()//2)-height//2
	root.geometry("{}x{}+{}+{}".format(width, height, x, y))

def setGrid():
	"used to set the game grid"
	gameScreen.grid(row=1, column=1, columnspan=3)
	textScreen.grid(row=2, column=1, columnspan=3)
	butNew.grid(row=3, column=1)
	butStart.grid(row=3, column=2, padx=5, sticky="w")
	butStop.grid(row=3, column=2, sticky="e")
	butQuit.grid(row=3, column=3, pady=5)

def exitProgram(event=1):
	exit()

def createButton(text, command):
	return Button(root, text=text, command=command)

def startMoving():
	"initiate the balls movement"
	global flagMove
	flagMove = 1
	if flagBalls == 1: #check if the balls are created before to start move function
		moveBalls()

def stopMoving():
	"stop the balls movement"
	global flagMove
	if flagMove == 1:
		flagMove = 0


#program
if __name__ == "__main__":
	root = Tk()

	# main screen of the game
	gameScreen = createCanva(600, 600)

	# text screen of the game
	textScreen = createCanva(600, 50)


	# define the game button
	butNew = createButton("Start a new game", newGame)
	butStart = createButton("Start", startMoving)
	butStop = createButton("Stop", stopMoving)
	butQuit = createButton("Quit", root.quit)

	setGrid()
	setWindow()
	root.mainloop()