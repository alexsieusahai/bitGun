import urllib.request
import json

def getVerdict():
    myObj = urllib.request.urlopen('http://codeforces.com/api/user.status?handle=itspax&from=1&count=1').read()
    return json.loads(myObj.decode('utf8'))['result'][0]['verdict']

