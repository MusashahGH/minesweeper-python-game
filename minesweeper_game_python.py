#Minesweeper Game In Python
import random
import os

from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

#board user can NOT SEE(solution)
board=[[0,0,0,0,0],  #0 =no bomb
       [0,0,0,0,0],  #1 =bomb
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0]]
#board user can SEE
boardDisplay=[[-1,-1,-1,-1,-1], #-1= unknown
       [-1,-1,-1,-1,-1],
       [-1,-1,-1,-1,-1],
       [-1,-1,-1,-1,-1],
       [-1,-1,-1,-1,-1]]

def checkMineAround(row,column):
    t=0
    i=row-1
    while i<= row+1:
        if i>=0 and i<5:
            j=column-1
            while j<=column+1:
                if j>=0 and j<5:
                    t=t+board[i][j]
                j=j+1
        i=i+1
    return t

#add Mines
numMine = 0
while numMine < 1 or numMine > 24:
    numMine = int(input("How many mines? (1 to 24): "))
    if numMine < 1 or numMine > 24:
        print("Impossible! Please enter a number between 1 and 24.")

print("You selected " + str(numMine) + " mines.")
num=0

while num < numMine:
    row = random.randint(0,4) #build-in module 
    column = random.randint(0,4) #build-in module 
    if board[row][column] == 0:
        board[row][column] = 1 #add a mine
        num += 1 #incrementation

def displaySol():  #function to show solution
    for row in range(0,5): #For loop(row)
        for column in range(0,5):
            print(board[row][column], end=" ") #end is use to stay on the line
        print(" ") #This is for next line

def displayBoard():

    table = Table(
        title="MINESWEEPER",
        box=box.DOUBLE,
        show_header=True,
        header_style="bold cyan"
    )

    # First empty column
    table.add_column("", justify="center")
    
    for i in range(5): # Column numbers
        table.add_column(str(i + 1), justify="center")

    for row in range(5):# Board
        cells = []
        for column in range(5):
            value = boardDisplay[row][column]
            if value == -1:
                cells.append("■")
            else:
                cells.append(str(value))
        table.add_row(str(row + 1), *cells)
    console.print(table) 


displayBoard()

guess = 0
while guess < (25 - numMine):
    row = int(input("Guess a row(1-5): ")) - 1
    column = int(input("Guess a column(1-5): ")) - 1
    if board[row][column] == 1:
        print("Booom!!!! You hit a mine.")
        displaySol()
        break
    else:
        if boardDisplay[row][column] == -1:
            boardDisplay[row][column] = checkMineAround(row, column)
            guess += 1
        else:
            print("Already revealed! Try another cell.")

        os.system("cls") #clear screen
        displayBoard()
        if guess == (25 - numMine):
            print("🎉 Congratulations! You Win!")
            break
