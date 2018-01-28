import os
import subprocess

# load config
from config import config

# assuming we don't have the contest set up

# need to import favEditor, extensions, favLang from config file

def buildContestDir(CONTEST_NO, PROBLEM_ALPHA=None, chooseFileExtension = False):
    filename = CONTEST_NO+PROBLEM_ALPHA
    """
    Builds the directory for the contest, then automatically navigates the user to
        - the problem specified
        - the first problem in the contest specified
    and opens the file in their favorite editor

    CONTEST_NO: String which is the contest number for the contest specified
    PROBLEM_ALPHA: String which is the problem alpha

    Example:
    Watermelon, problem 4A on codeforces, has the CONTEST_NO of 4 and the PROBLEM_ALPHA of A.
    """
    if str(os.getcwd()).split('/')[-1] != str(CONTEST_NO):
        try:
            os.makedirs(CONTEST_NO)
        except:
            print('Folder for that contest already made. Will continue without doing anything...')
        os.chdir(CONTEST_NO)

    if PROBLEM_ALPHA == None:
        for i in range(65,70):
            subprocess.call(['touch',CONTEST_NO+chr(i)]) # creates a file with the function

    else:
        # create a file with your preferred language extension
        # can I open my ide here and let this program run in background?
        # if not I can use python to run bash to do so

        # remember to account for letting user set their own extension
        subprocess.call(['touch',CONTEST_NO+PROBLEM_ALPHA+'.'+config['favExtension']])
        #subprocess.call([favEditor,CONTEST_NO+PROBLEM_ALPHA+extensions[favLang]])
        # need to figure out config solution first

