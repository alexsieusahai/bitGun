def suboptimalSol():
    while True:
        cmd = input('''\n
                "diff" : see difference between output and your answer\n
                "write" : write to your file using your preferred editor \n
                "submit" : opens submission url for the specified problem\n
                "verdict" : gets the verdict of the problem you submitted last\n
                "exit" : exits program. alternatively, press "ctrl+c" to exit\n\n''')
        if cmd == 'write':
            subprocess.run([config['favEditor'],contestNo+problemAlpha+'.'+config['favExtension']])
            subprocess.run(['g++', contestNo+problemAlpha+'.cpp', '-o', contestNo+problemAlpha])
        if cmd == 'diff':
            for inpt in inputs:
                myOutput = subprocess.check_output(["./"+contestNo+problemAlpha, inpt]).decode('utf8')
                with open(contestNo+problemAlpha+'.ans', 'w') as f:
                    f.write(myOutput)
                subprocess.run(['diff',contestNo+problemAlpha+'.ans', contestNo+problemAlpha+'.out'])
        if cmd == 'exit':
            sys.exit()
        if cmd == 'submit':
            openContestUrl.openContestUrl(contestNo,problemAlpha)
            input("press enter once you've submitted...")
            verdict = ''
            while verdict != '':
                verdict = getVerdict.getVerdict()
                if verdict != '':
                    print('The last result was: ',verdict)
                else:
                    print("The judge didn't finish evaluating...")
                    time.sleep(1)
        if cmd == 'verdict':
            print('The last result was: ',getVerdict.getVerdict())

