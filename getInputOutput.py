import urllib.request
from bs4 import BeautifulSoup

def getInputOutput(CONTEST_NO, PROBLEM_ALPHA):
    """
    This function gets the input and output of the problem specified, scraped using bs4.
    CONTEST_NO: The number of the contest that you're trying to access. For example, Problem 4A "Watermelon" has a CONTEST_NO of 4.
    PROBLEM_ALPHA: The problem letter. Problem 4A "Watermelon" has a PROBLEM_ALPHA of A.

    Returns a tuple of lists, where tuple[0] is a list of inputs, and tuple[1] is a list of outputs. It is guaranteed that if the data scraping works fine that len(tuple[0]) == len(tuple[1])
    """
    print('getting inputs and outputs for the problem '+CONTEST_NO+PROBLEM_ALPHA)
    PROBLEM_ALPHA = PROBLEM_ALPHA.upper()
    urlString = 'http://codeforces.com/problemset/problem/'+CONTEST_NO+'/'+PROBLEM_ALPHA
    fp = urllib.request.urlopen(urlString)
    mybytes = fp.read() # read in bytecode
    rawHtml = mybytes.decode("utf8") # decode mybytes using decode method and pass utf8
    # rawHtml is now the html
    fp.close() # close it since we aren't using it anymore

    soup = BeautifulSoup(rawHtml, 'html.parser')
    soupInputs = soup.find_all(attrs={'input'})
    soupOutputs = soup.find_all(attrs={'output'})
    testCaseNo = 0 # keep track of which test case it is
    for i in range(len(soupInputs)):
        inputs = str(soupInputs[i].pre).split('<br/>')
        if ('<pre>' in inputs[0]):
            inputs[0] = inputs[0].split('<pre>')[1];
        inputs = inputs[:-1]
        print('inputs: ',inputs)

        outputs = str(soupOutputs[i].pre).split('<br/>') # splitting by the only tag that seperates the outputs
        outputs = outputs[:len(outputs)-1] # remove the garbage tags from the front and the back
        outputs[0] = ''.join(list(outputs[0])[5:]) # getting rid of a <pre> tag in front of some of the output
        print('outputs: ',outputs)
        testCaseNo += 1
    return (inputs,outputs)

