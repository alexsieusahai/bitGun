# byteGun 
_Inspired by Terminal Leetcode._  
A codeforces test suite. Still building, and as such a lot of design decisions are not made.
##todo
- build an editor for _config.yml_
- find a solution for compiling and running for an arbitrary specified language that's better than the garbage one I have now
- let the user search for a problem based on name _(try obvious O(n) solution)_
- let the user sort the problems by difficulty
- let the user sort the problems by tags
- find a better solution for finding if the editor thread is closed
- **important;** figure out a way to submit without having the user go to codeforces and login manually if possible

##what's done so far
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
