# ---------------------------

# Sorting Algorithm v1.0
# By PanNino

# ---------------------------

# Extensions

import math
import random as rnd
import time
import os
import math

# ---------------------------

# Config

from settings import config as config

global data
class data:

    moves = 0 # How many moves it took to complete the sort
    score = 0 # Current score of the bars (a perfect score is 1000000)

# ---------------------------

# Variable and function set up

currentBars = []
pos = 0

# printScreen() prints out the bars

def printScreen(barList):

    if config.sys == 'windows':
        os.system('CLS')
    
    elif config.sys == 'linux':
        os.system('clear')

    barCnt = len(barList)
    printRow = ''

    for lt in range(config.bars):
        printRow = printRow + ' '

    for row in range(len(barList)): # Keeps track of how far down the row the program is

        listInd = barList.index(config.bars - (row))
        l = list(printRow)
        l[listInd] = '|'

        printRow = ''.join(l)

        print(printRow)

    if config.showList:
        print(barList)

# checkBars() checks whether or not the bars have been properly sorted

def checkBars(barList):

    theReturn = True
    data.score = 0

    for check in range(len(barList)):

        data.score += ((1000000 / config.bars) * (config.bars - (abs(barList[check] - (check + 1))))) / config.bars

        if barList[check] != check + 1:

            if config.showData == False:
                return False
            else:
                theReturn = False
    
    data.score = round(data.score)
    return theReturn

def checkColumn(barList, range1, range2):

    for check in range(range2 - range1):
        if barList[check + range1] != check + range1 + 1:
            return False
    
    return True

def move(barList, position, newPos, logic):

    if logic == 'greater':

        bar1 = barList[position]
        bar2 = barList[newPos]

        if bar1 >= newPos + 1:
            if newPos != 0:
                barList[newPos] = bar1
                barList[pos] = bar2
    
    elif logic == 'force':

        bar1 = barList[position]
        bar2 = barList[newPos]

        barList[newPos] = bar1
        barList[position] = bar2
    
    data.moves += 1

# ---------------------------

# Logic

# Setup

if config.scrambleStyle == 'random':
    for add in range(config.bars):
        currentBars.append(add + 1)

    randomize = currentBars
    currentBars = []

    for random in range(len(randomize)):
        newChoice = rnd.randint(0, (len(randomize) - 1))
        currentBars.append(randomize[newChoice])
        randomize.pop(newChoice)

elif config.scrambleStyle == 'reverse':
    for add in range(config.bars):
        currentBars.append(config.bars - add)

# THIS IS ONLY FOR COLUMN SORT

if config.algorithm == 'column':

    if config.bars < 16:
        config.bars = 16
    
    currentColumnMin = 0
    currentColumnMax = math.floor(config.bars / 8) - 1
    currentColumn = 1
    columns = 8

# Sorting

printScreen(currentBars)

while checkBars(currentBars) == False:

    # Basic sorting

    if config.pauseEvery > 0:
        if (data.moves % config.pauseEvery) == 0:
            print('Moves - ' + str(data.moves))
            print('Bar score - ' + str(data.score))
            time.sleep(config.pauseLength)

    if config.algorithm == 'basic':
        
        newPos = pos + 1
        if newPos == config.bars:
            newPos = 0
        
        move(currentBars, pos, newPos, 'greater')

        # New position

        pos += 1
        if pos == config.bars:
            pos = 0
    
    # Dice sort

    elif config.algorithm == 'dice':

        if currentBars[pos] != (pos + 1):
            newPos = rnd.randint(0, config.bars - 1)

            while currentBars[newPos] == (newPos + 1):
                newPos = rnd.randint(0, config.bars - 1)
            
            move(currentBars, pos, newPos, 'force')
        
        pos += 1
        if pos == config.bars:
            pos = 0
    
    # Optimized basic sort

    elif config.algorithm == 'optimized':

        newPos = pos + 1
        if newPos == config.bars:
            newPos = 0
        
        while currentBars[newPos] == (newPos + 1):
            newPos = newPos + 1
            if newPos == config.bars:
                newPos = 0
        
        move(currentBars, pos, newPos, 'greater')

        # New position

        pos += 1
        if pos == config.bars:
            pos = 0
    
    # Perfect sort

    elif config.algorithm == 'perfect':

        newPos = currentBars[pos] - 1
        
        move(currentBars, pos, newPos, 'force')

        pos += 1
        if pos == config.bars:
            pos = 0
        
        if currentBars[pos] == pos + 1:
            pos += 1
            if pos == config.bars:
                pos = 0
    
    # Column sort (CURRENTLY NONFUNCTIONING)

    '''
    elif config.algorithm == 'column':
        
        if checkColumn == False:
            
            newPos = pos + 1
            if newPos == currentColumnMax + 1:
                newPos = currentColumnMin
            
            move(currentBars, pos, newPos, 'greater')

            pos += 1
            if pos == currentColumnMax + 1:
                pos = currentColumnMin
        
        else:
            currentColumn += 1

            if currentColumn > columns:
                currentColumn = 1
                currentColumnMix = 0

            else:
                currentColumnMin = currentColumnMax + 1

            if (currentColumn != columns):
                currentColumnMax += math.floor(config.bars / columns) + 1
            else:
                currentColumnMax = config.bars - 1
    '''

    printScreen(currentBars)

    if config.useFrameRate:
        time.sleep(1 / config.fps)

print('Sorting complete! Program closing in 5 minutes...')

if config.showData:
    print('Moves to complete sort - ' + str(data.moves))
    print('Score - ' + str(data.score))

time.sleep(300)

# ---------------------------