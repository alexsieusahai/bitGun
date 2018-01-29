import urllib.request
from bs4 import BeautifulSoup

import getInputOutput

def showProblemDesc(contestNo, problemAlpha):
    urlString = 'http://codeforces.com/problemset/problem/'+contestNo+'/'+problemAlpha
    with urllib.request.urlopen(urlString) as problem:
        rawHtml = problem.read().decode("utf8")

    soup = BeautifulSoup(rawHtml, 'html.parser')
    soupText = soup.find_all('p')
    print('PROBLEM: ',contestNo+problemAlpha)
    print('PROBLEM DESC:')
    for i in soupText:
        try:
            toPrint = i.text
            if len(toPrint) > 20 and toPrint[-1] != ':':
                print(i.text)
        except:
            continue
    [inputs,outputs] = getInputOutput.getInputOutput(contestNo,problemAlpha)
    print('INPUT: ')
    for i in range(len(inputs)):
        print(inputs[i])
    print('OUTPUT: ')
    for i in outputs:
        print(i)
    toReturn = input('\nDo you want to attempt to solve this problem? (y/n)\n')
    return toReturn == 'y'

