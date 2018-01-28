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
i = 0
for inpt in inputs:
    with open(contestNo+problemAlpha+'_'+str(i)+'.in', 'w') as f:
        f.write(inpt)
    with open(contestNo+problemAlpha+'_'+str(i)+'.out', 'w') as f:
        f.write(outputs[i])
    i += 1

def writeFile():
    subprocess.run([config['favEditor'],contestNo+problemAlpha+'.'+config['favExtension']])

def testFile():
    while True:
        i = 0
        correctOutputs = 0

        # compile the program if necessary
        subprocess.run(['g++', contestNo+problemAlpha+'.cpp', '-o', contestNo+problemAlpha])

        for inpt in inputs:
            testOutput = subprocess.check_output(['./'+contestNo+problemAlpha, '<', contestNo+problemAlpha+'_'+str(i)+'.in']).decode('utf8')
            if testOutput == outputs[i]:
                print(testOutput)
                correctOutputs += 1
            i += 1

        if correctOutputs == len(inputs):
            print('all cases passed!')
            shouldSubmit = input('do you want to submit? type in "y" to submit\n')
            if shouldSubmit == 'y':
                openContestUrl.openContestUrl(contestNo, problemAlpha)
                i = 0
                while verdict != '':
                    verdict = getVerdict.getVerdict()
                    print('The last result was: ',verdict)
                    time.sleep(1)
                    i += 1
                    if i > config['maxCalls']:
                        print('timeout; judge did not give a verdict within '+str(config['maxCalls'])+' seconds.')
                        break;
            return

        time.sleep(3)


writeFileThread = threading.Thread(target = writeFile)
writeFileThread.start()

testFileThread = threading.Thread(target = testFile)
testFileThread.start()

