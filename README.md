# Python Turing Machine

Here is a list of the implemented functions

- Increment
- Decrement
- One's Complement
- Palindrome Checker
- Divisble by Three

## How these machines work

The states of each of the machines is stored within the text files that begin with `tm_`. These files are read based in the input of the `-w` argument passed at execution time. The states are read from the text files and stored during runtime in dictionaries with states as the keys and tuples containing 4 variables for the values of each item in the dictionary.

Each line of the state files that I've written can be interpreted as 5 tab delimited columns with each column representing:

1. Current state
2. Input read from tape
3. State to transition to
4. What to write to tape
5. Direction to move tape head

## How to run

A makefile is provided to allow for easy testing. There are a couple rules you can use:

- `make run-all`
  - Runs all the implemented TMs and writes their output
- `make run-ones`
  - Runs only the one's complement machine
- `make run-inc`
  - Runs only the increment machine
- `make run-dec`
  - Runs only the decrement machine
- `make run-pal`
  - Runs only the palindrome machine
- `make run-div`
  - Runs only the divisible by 3 machine
- `make clean`
  - Deletes all .pyc and generated output files

Running `make` will execute each rule using my own supplied test files as the default. However, command line arguments can also be passed with the make command to change the file inputs. This is done like so:

- `make ONES-INPUT="xinputONES.txt"`
- `make INC-INPUT="xinputINC.txt"`
- `make DEC-INPUT="xinputDEC.txt"`
- `make PAL-INPUT="xinputPAL.txt"`
- `make DIV-INPUT="xinputDIV.txt"`

Simply change the path to any text file you like. Of course, these can be combined with the other make rules and multiple can be changed at once when running the command.

When running the makefile it will also run a bash script that I've included (`setup.sh`). All this script does is check to see whether a needed dependency, `configargparse`, is installed. If not the script simply runs `pip3 install configargparse`.

Lastly, I have tested this makefile on a linux lab machine and there seems to be no problems using the makefile when it comes to installing modules through pip. Assuming your python 3 alias is `python3` and `pip3` is installed.

## Interpreting output

Outout from executing the makefile is seperated into two file, them being `zlog*.txt` and `zoutput*.txt` files. The difference if this:
- `zlog*.txt` files:
  - Basic output from the machines' showing the beginning input tape and tape after execution
- `zouput*.txt`
  - All text I print from standard output. Meaning each step from the machines' execution is written here

## State tables for each machine
### One's Complement
|             | 0               | 1               | b              |
|-------------|-----------------|-----------------|----------------|
| INVERTINPUT | INVERTINPUT,1,R | INVERTINPUT,0,R | RETURNLEFT,b,L |
| RETURNLEFT  | RETURNLEFT,0,L  | RETURNLEFT,1,R  | ENDSTATE,b,R   |

### Increment
|             | 0               | 1               | b              |
|-------------|-----------------|-----------------|----------------|
| SEARCHRIGHT | SEARCHRIGHT,1,L | SEARCHRIGHT,0,R | RETURNLEFT,1,L |
| RETURNLEFT  | RETURNLEFT,0,L  | RETURNLEFT,1,R  | ENDSTATE,b,R   |

### Decrement
|          | Subprocesses                                                                     |
|----------|----------------------------------------------------------------------------------|
| ONESCOMP | Execute one's complement machine. Upon completion switch to increment subprocess |
| INCREM   | After executing transtion to one's complement subprocess                         |

### Palindrome
|             | 0               | 1               | b               |
|-------------|-----------------|-----------------|-----------------|
| SEARCHSTATE | MOVEENDZERO,b,R | MOVEENDONE,b,R  | ENDSTATE,b,R    |
| MOVEENDZERO | MOVEENDZER0,0,R | MOVEENDZERO,1,R | CHECKZERO,b,L   |
| MOVEENDONE  | MOVEENDONE,0,R  | MOVEENDONE,1,R  | CHECKONE,b,L    |
| CHECKZERO   | RETURNSTART,b,L | FAILSTATE,1,L   | ENDSTATE,b,L    |
| CHECKONE    | FAILSTATE,0,L   | RETURNSTART,b,L | ENDSTATE,b,L    |
| RETURNSTART | RETURNSTART,0,L | RETURNSTATE,1,L | SEARCHSTATE,b,R |

### Divisible By Three
|             | 0               | 1               | b              |
|-------------|-----------------|-----------------|----------------|
| REMAINZERO  | REMAINZERO,0,R  | REMAINONE,1,R   | ENDSTATE,b,L   |
| REMAINONE   | REMAINTWO,0,R   | REMAINZERO,1,R  | FAILSTATE,b,L  |
| REMAINTWO   | REMAINONE,0,R   | REMAINTWO,1,R   | FAILSTATE,b,L  |