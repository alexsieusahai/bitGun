import subprocess
import argparse
import string
import os

import getInputOutput
import buildContestDir

from config import config


#   if no argument is supplied, the files in the directory are scanned and an "intelligent" choice is made

# handle parsing of the contest
parser = argparse.ArgumentParser()
parser.add_argument('--contest_id','-cid', default = '4A') # takes in an argument like '491a'
args = parser.parse_args()
print(args)

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

print('current dir as from main.py: '+str(os.getcwd()));
subprocess.run([config['favEditor'],problemAlpha+'.'+config['favExtension']])
# what i have to do now is run a thread with the editor, and run aother thread that tries to compile the prog, and if it can it will run the test cases against it
