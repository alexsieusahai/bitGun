import urllib.request
import json
import curses

import components/solveProblem
import components/showProblemDesc
import components/scrapeProblemData
import components/getSavedProblemData

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
problemList = []

# getting problem data
#problems = urllib.request.urlopen('http://codeforces.com/api/problemset.problems')
#response = ""
#while True:
#    data = problems.read().decode()
#    if not data:
#        break
#    response += data
#problems = json.loads(response)['result']['problems']

problems = getSavedProblemData.getSavedProblemData()

#with open('problemData.txt', 'w') as outfile:
#    json.dump(problems, outfile)

i = 0
for problem in problems:
    try:
        if i < 20:
            stdscr.addstr(problem['name']+'\n')
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
    if c == 'j':
        y += 1
        if y > 20:
            y = 0
        stdscr.addstr(problemList[problemNo][0]) # get rid of reverse
        problemNo += 1
        stdscr.move(y,0)
    if c == 'k':
        stdscr.addstr(problemList[problemNo][0]) # get rid of reverse
        y -= 1
        problemNo -= 1
        if y < 0:
            y = 0
        if problemNo < 0:
            problemNo = 0
        stdscr.move(y,0)
    if c == 'i':
        closeCurses()
        if showProblemDesc.showProblemDesc(problemList[y][1], problemList[y][2]):
            #solveProblem.solveProblem(problemList[y][1],problemList[y][2])
            solveProblem.solveProblem('4','A')
        beginCurses()
    if c == 'h':
        closeCurses()
        print('''
        k : move up
        j : move down
        i : attempt that problem
        h : help
        ''')
        beginCurses()
    if c == 'u':
        shouldUpdate = input('are you sure you want to update the current codeforces directory? this might take a while, so be patient if you do. (y/n)').strip()
        if shouldUpdate == 'y':
            print('hi')

    stdscr.clrtoeol()
    stdscr.addstr(problemList[problemNo][0],curses.A_REVERSE)
    stdscr.move(y,0)
    stdscr.refresh()
