
# Project Assignment by Zareh Gorjian
# Game of Life, Kathryn Dullerud, CIS 012

import random

def displayMenu():
    print("U - Press 'U' to load the 'U' pattern.\nPlay – Press 'P' to play.\nHalt - Press 'H' to halt the game.\nClear - Press 'C' to clear the grid.\nQuit – Press 'Q' to exit.\n1) Glider - Press '1' to load the glider pattern.\n2) Toad - Press '2' to load the toad pattern.\n3) Fishhook - Press '3' to load the fishhook pattern.\nManual - Press 'M' to create a pattern from the user's input (collect row and column numbers) and set each cell to a live cell.\nSave - Press 'S' to save the current live cell pattern of the currentGen to a file.\nLoad - Press 'L' to load a saved file.")

def setZeroList(lst, nrow, ncol):
    for row in range(nrow):
        for col in range(ncol):
            lst[row][col]='-'

def setInitialPatternList(parList,nrow,ncol):
    randRow = random.randint(0,nrow-6)
    randCol = random.randint(0,ncol-7)
    for row in range(randRow,randRow+5):
        parList[row][randCol]='I'
        parList[row][randCol+6]='I'
    for col in range(randCol,randCol+7):
        parList[randRow+5][col]='I'

def copyList(list1,nrow,ncol,list2):
    for row in range(nrow):
        for col in range(ncol):
            list2[row][col]=list1[row][col]

def displayList(list1,nrow):
    for row in range(nrow):
            print(str(list1[row]).strip("[").strip("]"))
            

def displaySubMenu():
    print("Play - Press 'P' to play.\nHalt – Press 'H' to halt.")

def setNextGenList(list1,list2,nrow,ncol):
    for row in range(nrow):
        for col in range(ncol):
            count = 0
            for rnum in range(max(row-1,0),min(row+2,nrow)):
                for cnum in range(max(col-1,0),min(col+2,ncol)):
                    if list2[rnum][cnum]=='I':
                        count+=1
            if list2[row][col]=='I':
                if count-1<2 or count-1>3:
                    list1[row][col]='-'
                else:
                    list1[row][col]='I'
            else:
                if count==3:
                    list1[row][col]='I'
                else:
                    list1[row][col]='-'

def setDifferentPattern(fname,list1,nrow,ncol):
    fhand = open(fname)
    count = 0
    for line in fhand:
        count=count+1
    randRow = random.randint(0,nrow-count)
    randCol = random.randint(0,ncol-count)
    fhand = open(fname)
    for newline in fhand:
        myRow,myCol=newline.split()
        row = int(myRow)
        col = int(myCol)
        list1[randRow+row][randCol+col]='I'
    fhand.close()

def saveToFile(list1,nrow,ncol):
    fname = input("Please enter what you want to name your file (include .txt): ")
    fhand = open(str(fname),'w')
    for row in range(nrow):
        for col in range(ncol):
            if list1[row][col]=='I':
                element = str(row) + " " + str(col) + "\n"
                fhand.write(element)
    fhand.close()

def loadNewFile(list1,nrow,ncol):
    fname = input("Please enter the name of the file you want to load (include .txt): ")
    fhand = open(str(fname))
    for newline in fhand:
        myRow,myCol=newline.split()
        row = int(myRow)
        col = int(myCol)
        list1[row][col]='I'
    fhand.close()

def manualPattern(list1,nrow,ncol):
    entering = True
    while entering == True:
        strRow, strCol = input("Please enter the row and column of the live cell separated by a space: ").split()
        row = int(strRow)
        col = int(strCol)
        if row<nrow and col<ncol:
            list1[row][col]='I'
        else:
            print("Row or column number has exceeded maximum.")
        more = input("More elements to enter (y or n)? ")
        if more=="N" or more=="n":
            entering = False
        
    

MAX_ROW=40
MAX_COL=80
tempGen=[[0 for i in range(MAX_COL)] for j in range(MAX_ROW)]
currentGen=[[0 for i in range(MAX_COL)] for j in range(MAX_ROW)]
play=True
while play==True:
    displayMenu()
    response=input()
    if response=="p" or response=="P":
     while response=="P" or response=="p":
            displaySubMenu()
            setNextGenList(tempGen,currentGen,MAX_ROW,MAX_COL)
            copyList(tempGen,MAX_ROW,MAX_COL,currentGen)
            displayList(currentGen,MAX_ROW)
            response=input()   
    if response=="u" or response=="U":
        displaySubMenu()
        setZeroList(tempGen,MAX_ROW,MAX_COL)
        setInitialPatternList(tempGen,MAX_ROW,MAX_COL)
        copyList(tempGen,MAX_ROW,MAX_COL,currentGen)
        displayList(currentGen,MAX_ROW)
        response=input()
        while response=="P" or response=="p":
            displaySubMenu()
            setNextGenList(tempGen,currentGen,MAX_ROW,MAX_COL)
            copyList(tempGen,MAX_ROW,MAX_COL,currentGen)
            displayList(currentGen,MAX_ROW)
            response=input()
        if response=="h" or response=="H":
            continue
    if response=="1":
        displaySubMenu()
        setZeroList(tempGen,MAX_ROW,MAX_COL)
        setDifferentPattern("glider.txt",tempGen,MAX_ROW,MAX_COL)
        copyList(tempGen,MAX_ROW,MAX_COL,currentGen)
        displayList(currentGen,MAX_ROW)
        response=input()
        while response=="P" or response=="p":
            displaySubMenu()
            setNextGenList(tempGen,currentGen,MAX_ROW,MAX_COL)
            copyList(tempGen,MAX_ROW,MAX_COL,currentGen)
            displayList(currentGen,MAX_ROW)
            response=input()
        if response=="h" or response=="H":
            continue
    if response=="2":
        displaySubMenu()
        setZeroList(tempGen,MAX_ROW,MAX_COL)
        setDifferentPattern("toad.txt",tempGen,MAX_ROW,MAX_COL)
        copyList(tempGen,MAX_ROW,MAX_COL,currentGen)
        displayList(currentGen,MAX_ROW)
        response=input()
        while response=="P" or response=="p":
            displaySubMenu()
            setNextGenList(tempGen,currentGen,MAX_ROW,MAX_COL)
            copyList(tempGen,MAX_ROW,MAX_COL,currentGen)
            displayList(currentGen,MAX_ROW)
            response=input()
        if response=="h" or response=="H":
            continue
    if response=="3":
        displaySubMenu()
        setZeroList(tempGen,MAX_ROW,MAX_COL)
        setDifferentPattern("fishhook.txt",tempGen,MAX_ROW,MAX_COL)
        copyList(tempGen,MAX_ROW,MAX_COL,currentGen)
        displayList(currentGen,MAX_ROW)
        response=input()
        while response=="P" or response=="p":
            displaySubMenu()
            setNextGenList(tempGen,currentGen,MAX_ROW,MAX_COL)
            copyList(tempGen,MAX_ROW,MAX_COL,currentGen)
            displayList(currentGen,MAX_ROW)
            response=input()
        if response=="h" or response=="H":
            continue
    if response=="L" or response=="l":
        setZeroList(tempGen,MAX_ROW,MAX_COL)
        loadNewFile(tempGen,MAX_ROW,MAX_COL)
        copyList(tempGen,MAX_ROW,MAX_COL,currentGen)
        displayList(currentGen,MAX_ROW)
        response=input()
        while response=="P" or response=="p":
            displaySubMenu()
            setNextGenList(tempGen,currentGen,MAX_ROW,MAX_COL)
            copyList(tempGen,MAX_ROW,MAX_COL,currentGen)
            displayList(currentGen,MAX_ROW)
            response=input()
        if response=="h" or response=="H":
            continue
    if response=="M" or response=="m":
        setZeroList(tempGen,MAX_ROW,MAX_COL)
        manualPattern(tempGen,MAX_ROW,MAX_COL)
        copyList(tempGen,MAX_ROW,MAX_COL,currentGen)
        displayList(currentGen,MAX_ROW)
        response=input()
        while response=="P" or response=="p":
            displaySubMenu()
            setNextGenList(tempGen,currentGen,MAX_ROW,MAX_COL)
            copyList(tempGen,MAX_ROW,MAX_COL,currentGen)
            displayList(currentGen,MAX_ROW)
            response=input()
        if response=="h" or response=="H":
            continue
    if response=="s" or response=="S":
        saveToFile(currentGen,MAX_ROW,MAX_COL)
    if response=="c" or response=="C":
        setZeroList(tempGen,MAX_ROW,MAX_COL)
        copyList(tempGen,MAX_ROW,MAX_COL,currentGen)
        displayList(currentGen,MAX_ROW)
    if response=="Q" or response=="q":
        play=False




