import json

import scrapeProblemData

def getSavedProblemData():
    try:
        with open('problemData.json', 'r') as f:
            problems = json.load(f)
    except:
        problems = scrapeProblemData.scrapeProblemData()

    return problems
