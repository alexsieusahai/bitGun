import json
import urllib.request

from config import config

def getSolvedProblems():
    try:
        with open('correctlySolvedProblems.json', 'r') as f:
            correctDict = json.load(f)
    except:
        correctDict = {}
        mybytes = urllib.request.urlopen('http://codeforces.com/api/user.status?handle='+config['handle']+'&from=1').read()
        mydata = json.loads(mybytes.decode())['result']
        for i in mydata:
            if i['verdict'] == 'OK':
                problem = str(i['problem']['contestId'])+i['problem']['index']
                correctDict[problem] = True

        with open('correctlySolvedProblems.json', 'w') as outfile:
            json.dump(correctDict, outfile)

    return correctDict
