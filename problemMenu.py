import urllib.request
import json
import curses
import sys

import solveProblem
import showProblemDesc
import scrapeProblemData
import getSavedProblemData
from config import config

stdscr = curses.initscr()
# curses stuff
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


i = 0
for problem in problems:
    try:
        if i < maxX:
            stdscr.addstr(str(i)+'\t'+problem['name']+'\n')
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
    # clean row
    stdscr.clrtoeol()
    if c == config['keys']['down']:
        y += 1
        if y > maxX:
            y = 0
        stdscr.addstr(str(problemNo)+'\t'+problemList[problemNo][0]) # get rid of reverse
        problemNo += 1
        stdscr.move(y,0)
    if c == config['keys']['up']:
        stdscr.addstr(str(problemNo)+'\t'+problemList[problemNo][0]) # get rid of reverse
        y -= 1
        problemNo -= 1
        if y < 0:
            y = 0
        if problemNo < 0:
            problemNo = 0
        stdscr.move(y,0)
    if c == config['keys']['attempt']:
        closeCurses()
        if showProblemDesc.showProblemDesc(problemList[y][1], problemList[y][2]):
            #solveProblem.solveProblem(problemList[y][1],problemList[y][2])
            solveProblem.solveProblem('4','A')
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



    stdscr.clrtoeol()
    stdscr.addstr(str(problemNo)+'\t'+problemList[problemNo][0],curses.A_REVERSE)
    stdscr.move(y,0)
    stdscr.refresh()
