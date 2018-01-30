#  bitGun
A codeforces test suite.   
## todo
- build an editor for _config.yml_
- incorporate tutorials for problems and some interface for the user to access it (maybe a keyword?)
- find a solution for compiling and running for an arbitrary specified language that's better than what I have now
- let the user sort the problems by tags
- find a better solution for finding if the editor thread is closed
- **important;** figure out a way to submit without having the user go to codeforces and login manually if possible
- implement a fuzzy search for name comparison

## what's done so far
- have a solution for building a directory for contests specified
- touches and creates the file with the specified extension
- grabbed the input and output data using beautifulsoup from codeforces
- yaml is being used as a config solution
- using threading
    - to check if the program runs without errors
    - if it does, run it against all the input that you scraped from codeforces
    - if it agrees with the test cases, it prompts the user to submit the solution online
    - then checks the verdict by requesting the data from the _Codeforces_ api
- using _curses_ and _codeforces api_, a way to view and scroll through all the problems was implemented
- the problem description is now scraped from the website and the user is prompted with a confirmation that this is the problem that they want to work on
- stored the json data and i'm loading that stored data instead of scraping it everytime
- search by name implemented
- search by contest id and index implemented
- using _codeforces api_ to find the problems the user with the specified handle in _config.yml_ has solved, then displaying that with the terminal scrolling
- implemented page switching for faster access

## to eventually do
- instead of grabbing just problem, grab problem and statistics so you could search for instance, B difficulty problems sorted in descending order
- build something to move solutions of a list of files with some naming scheme (like `913a.cpp` or `modularExponentiation.cpp`, for instance) to the bitGun directory
- scrape the user's github and get their preferred language by looking at what language they use the most (i think github api makes this easy)
- automatically update every so often (ask the user before actually updating)
- fuzzy search for the name 
