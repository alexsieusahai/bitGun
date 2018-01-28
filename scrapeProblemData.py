import urllib.request
import json

def scrapeProblemData():
    problems = urllib.request.urlopen('http://codeforces.com/api/problemset.problems')
    response = ""
    while True:
        data = problems.read().decode()
        if not data:
            break
        response += data

    problems = json.loads(response)['result']['problems']

    # store it for later use
    with open('problemData.json', 'w') as outfile:
        json.dump(problems, outfile)

    return problems

