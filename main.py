import subprocess
import argparse
import string
import os
import threading
import sys
import time

import json
import urllib.request

import getInputOutput
import buildContestDir
import openContestUrl
import getVerdict
from config import config


#   if no argument is supplied, the files in the directory are scanned and an "intelligent" choice is made

# handle parsing of the contest
parser = argparse.ArgumentParser()
parser.add_argument('--contest_id','-cid', default = '4A') # takes in an argument like '491a'
args = parser.parse_args()

# get from the args the contest number and problem alpha, O(n), n is small
contestNo = ''
problemAlpha = ''
for i in args.contest_id:
    if i in string.digits:
        contestNo += i
    else:
        problemAlpha += i

# first, build up the path if it doesn't exist for the contest
buildContestDir.buildContestDir(contestNo,problemAlpha)


# to run bash commands using subprocess module:
# myStr = subprocess.check_output(["./helloWorld", "1"]).decode("utf8") #decode for unicode

# suboptimal solution; better to run the editor and use another thread to check it periodically

# get solutions and store in directory
(inputs,outputs) = getInputOutput.getInputOutput(contestNo, problemAlpha)
with open(contestNo+problemAlpha+'.in', 'w') as f:
    for inpt in inputs:
        f.write(inpt)
with open(contestNo+problemAlpha+'.out', 'w') as f:
    for output in outputs:
        f.write(output)

print(threading.current_thread())

def writeFile():
        subprocess.run([config['favEditor'],contestNo+problemAlpha+'.'+config['favExtension']])

def suboptimalSol():
    while True:
        cmd = input('''\n
                "diff" : see difference between output and your answer\n
                "write" : write to your file using your preferred editor \n
                "submit" : opens submission url for the specified problem\n
                "verdict" : gets the verdict of the problem you submitted last\n
                "exit" : exits program. alternatively, press "ctrl+c" to exit\n\n''')
        if cmd == 'write':
            subprocess.run([config['favEditor'],contestNo+problemAlpha+'.'+config['favExtension']])
            subprocess.run(['g++', contestNo+problemAlpha+'.cpp', '-o', contestNo+problemAlpha])
        if cmd == 'diff':
            for inpt in inputs:
                myOutput = subprocess.check_output(["./"+contestNo+problemAlpha, inpt]).decode('utf8')
                with open(contestNo+problemAlpha+'.ans', 'w') as f:
                    f.write(myOutput)
                subprocess.run(['diff',contestNo+problemAlpha+'.ans', contestNo+problemAlpha+'.out'])
        if cmd == 'exit':
            sys.exit()
        if cmd == 'submit':
            openContestUrl.openContestUrl(contestNo,problemAlpha)
            input("press enter once you've submitted...")
            verdict = ''
            while verdict != '':
                verdict = getVerdict.getVerdict()
                if verdict != '':
                    print('The last result was: ',verdict)
                else:
                    print("The judge didn't finish evaluating...")
                    time.sleep(1)
        if cmd == 'verdict':
            print('The last result was: ',getVerdict.getVerdict())

def myfunc0():
    print('sleeping 5 sec from thread')
    time.sleep(5)
    print('done sleeping')

t0 = threading.Thread(target = myfunc0)
t0.start()

writeFileThread = threading.Thread(target = writeFile)
t.start()

