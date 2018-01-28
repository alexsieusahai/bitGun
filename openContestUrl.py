import subprocess

from config import config

def openContestUrl(contestNo, problemAlpha):
    urlString = 'http://codeforces.com/problemset/problem/'+contestNo+'/'+problemAlpha
    subprocess.run([config['favBrowser'],urlString])
    print('done!')

