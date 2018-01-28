import urllib.request
import json
import curses
import sys

import solveProblem
import showProblemDesc
import scrapeProblemData
import getSavedProblemData
import getSolvedProblems
from config import config

correctDict = getSolvedProblems.getSolvedProblems()

# string formatting for printing
def fancyString(problemNum,problemList):
    solved = False
    if str(problemList[problemNum][1])+problemList[problemNum][2] in correctDict:
        solved = True
    nicestr=str(problemNum)+'\t'+str(solved)+'\t'+problemList[problemNum][2]+'\t'+problemList[problemNum][0]
    return nicestr

# curses stuff
stdscr = curses.initscr()
def beginCurses():
    stdscr = curses.initscr()
    stdscr.keypad(1)
    curses.noecho()
    curses.cbreak()

def closeCurses():
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()

beginCurses()
[maxX, maxY] = stdscr.getmaxyx()
maxX -= 5
problemList = []
problems = getSavedProblemData.getSavedProblemData()
correctDict = getSolvedProblems.getSolvedProblems()

i = 0
# tells the user what everything is
stdscr.move(maxX+2,0)
stdscr.addstr('Problem\tSolved\tIndex\tName')
stdscr.move(0,0)
for problem in problems:
    solved = False
    if str(problem['contestId'])+problem['index'] in correctDict:
        solved = True
    try:
        if i < maxX+1:
            stdscr.addstr(str(i)+'\t'+str(solved)+'\t'+problem['index']+'\t'+problem['name']+'\n')
            stdscr.refresh()
        problemList.append((problem['name'],str(problem['contestId']),problem['index']))
    except:
        continue
    i += 1

x = 0
y = 0
problemNo = 0
stdscr.move(0,0)
while True:
    c = stdscr.getkey()
    stdscr.clrtoeol()
    if c == config['keys']['down']:
        y += 1
        if y > maxX:
            y = 0
            # render all the next ones
            problemNoRender = problemNo
            yRender = y
            for i in range(maxX+2):
                stdscr.clrtoeol()
                stdscr.addstr(fancyString(problemNoRender, problemList))
                stdscr.move(yRender,0)
                yRender += 1
                problemNoRender += 1
            stdscr.move(y,0)
        stdscr.addstr(fancyString(problemNo, problemList))
        problemNo += 1
        stdscr.move(y,0)

    if c == config['keys']['rskip']:
        problemNo += maxX+1
        problemNoRender = problemNo-1
        problemNo += y
        yRender = 0
        for i in range(maxX+2):
            stdscr.clrtoeol()
            stdscr.addstr(fancyString(problemNoRender, problemList))
            stdscr.move(yRender,0)
            yRender += 1
            problemNoRender += 1
        stdscr.move(y,0)

    if c == config['keys']['up']:
        stdscr.addstr(fancyString(problemNo, problemList))
        y -= 1
        problemNo -= 1
        if y < 0:
            y = 0
            problemNo += 1
            if problemNo == 0:
                # not a perfect solution, just test it to see what I mean
                continue
            #render the ones from before
            yRender = maxX
            for i in range(maxX+1,0,-1):
                stdscr.clrtoeol()
                stdscr.addstr(fancyString(problemNo, problemList))
                stdscr.move(yRender,0)
                yRender -= 1
                problemNo-= 1
            stdscr.move(maxX,0)

        if problemNo < 0:
            problemNo = 0
        stdscr.move(y,0)

    if c == config['keys']['lskip']:
        yRender = maxX
        for i in range(maxX+1,0,-1):
            stdscr.clrtoeol()
            stdscr.addstr(fancyString(problemNo, problemList))
            stdscr.move(yRender,0)
            yRender -= 1
            problemNo-= 1
        stdscr.move(y,0)

    if c == config['keys']['jump']:
        y = 0
        closeCurses()
        toJump = int(input("Please input just the number that you want to jump to.\n"))
        beginCurses()
        stdscr.move(0,0)
        problemNo = toJump
        for i in range(maxX):
            stdscr.clrtoeol()
            stdscr.addstr(fancyString(problemNo, problemList))
            stdscr.move(y,0)
            y += 1
            problemNo += 1
        stdscr.move(0,0)
        problemNo = toJump-1

    if c == config['keys']['attempt']:
        closeCurses()
        if showProblemDesc.showProblemDesc(problemList[y][1], problemList[y][2]):
            solveProblem.solveProblem(problemList[y][1],problemList[y][2])
            getSolvedProblems.getSolvedProblems() # refresh the correct dict
        beginCurses()

    if c == config['keys']['update']:
        closeCurses()
        shouldUpdate = input('are you sure you want to update the current codeforces directory? this might take a while, so be patient if you do. (y/n)').strip()
        if shouldUpdate == 'y':
            scrapeProblemData.scrapeProblemData() # refreshes the problem data
        beginCurses()

    if c == config['keys']['close']:
        closeCurses()
        sys.exit()

    if c == config['keys']['searchIdInd']:
        closeCurses()
        print("if you don't want to specify anything for that input, just put '*'")
        contestNo = input('enter contest number\n')
        ind = input('enter index of the problem\n').upper()
        for problem in problems:
            if str(problem['contestId']) == contestNo and problem['index'] == ind.upper():
                if showProblemDesc.showProblemDesc(str(problem['contestId']), problem['index']):
                    solveProblem.solveProblem(str(problem['contestId']), problem['index'])
                break
            elif str(problem['contestId']) == contestNo and ind == '*':
                if showProblemDesc.showProblemDesc(str(problem['contestId']), problem['index']):
                    solveProblem.solveProblem(str(problem['contestId']), problem['index'])
                break
            elif contestNo == '*' and problem['index'] == ind:
                if showProblemDesc.showProblemDesc(str(problem['contestId']), problem['index']):
                    solveProblem.solveProblem(str(problem['contestId']), problem['index'])
                break
        beginCurses()


    if c == config['keys']['searchName']:
        closeCurses()
        searchName = input('please enter the name of the problem you want to find.\n').strip().lower()
        for problem in problems:
            if problem['name'].lower() == searchName:
                if showProblemDesc.showProblemDesc(str(problem['contestId']), problem['index']):
                    solveProblem.solveProblem(str(problem['contestId']), problem['index'])
                break
        beginCurses()


    solved = False
    if str(problemList[problemNo][1])+problemList[problemNo][2] in correctDict:
        solved = True
    stdscr.clrtoeol()
    stdscr.addstr(str(problemNo)+'\t'+str(solved)+'\t'+problemList[problemNo][2]+'\t'+problemList[problemNo][0],curses.A_REVERSE)
    stdscr.move(y,0)
    stdscr.refresh()
