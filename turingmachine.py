# written by Jake Bukuts 2020
import re

class TM:
    def __init__(self):
        self.step = 0

    # reads from turing machine txt file to create state dictionary
    # for machines to execute
    def read(self, name):
        # based on input instruction different machine
        # file is read
        filename = "tm_"+name+".txt"
        tmfile = open(filename)

        # we must get our start and end states from the file
        startstate = ""
        endstate = ""
        with open(filename, "r") as file:
            startstate = file.readline()
            for endstate in file:
                pass

        # store these states for the machine
        self.startState = re.split(r'\t+', startstate.rstrip('\t'))[0]
        self.endState = re.split(r'\t+', endstate.rstrip('\t'))[2]
        self.failState = 'FAILSTATE'

        # state dictionary
        self.states = {}

        # iterate over the file
        for line in tmfile:
            print(line)
            # split line to array by tabs
            splitline = re.split(r'\t+', line.rstrip('\t'))
            
            # seperate into variables
            fromState = splitline[0]
            toState = splitline[2]
            input = splitline[1]
            write = splitline[3]
            move = splitline[4].replace('\n','')

            # if read state not yet in dict
            # add it
            if fromState not in self.states.keys():
                self.states[fromState] = ["", [], "", ""]

            # put state transitions into the dictionary
            self.states[fromState][0] += input
            self.states[fromState][1].append(toState)
            self.states[fromState][2] += move
            self.states[fromState][3] += write

        tmfile.close()
        
    # returns state of the machine
    # to be called after the execution
    def getFinalState(self):
        return self.currState

    # gets the tape of the machine
    # to be called after execution
    def getEndTape(self):
        return "".join([c+" " for c in self.finaltape])

    # this will execute the input tm on the input tape from a file
    # returned is the tape after the execution
    def execute(self, tape, tapeheadpos):
        self.currState = self.startState

        # execution loop
        # runs while not in final accepting and rejecting state
        while self.currState != self.endState and self.currState != self.failState:

            # list comprehension to print output
            tapeString = "".join([l+" " for l in tape])
            posString = "".join(["  " for i in range(tapeheadpos)]) + '*'
            
            # print to standard output
            print("STEP:\t"+str(self.step)+"\tSTATE: "+self.currState)
            print("POS:\t"+posString)
            print("TAPE:\t"+tapeString+"\n")

            # change states
            c = self.states[self.currState]
            input = tape[tapeheadpos]
            v = c[0].index(input)
            self.currState = c[1][v]
            tape[tapeheadpos] = c[3][v]
            if c[2][v] == 'R':
                tapeheadpos += 1
            else:
                tapeheadpos -= 1

            # on to the next
            self.step += 1

        # list comprehension to print output
        tapeString = "".join([l+" " for l in tape])
        posString = "".join(["  " for i in range(tapeheadpos)]) + '*'

        # print to standard output
        print("STEP:\t"+str(self.step)+"\tSTATE: "+self.currState)
        print("POS:\t"+posString)
        print("TAPE:\t"+tapeString+"\n")

        self.finaltape = tape

        # return the tape
        return tape