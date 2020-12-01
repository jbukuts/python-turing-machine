# Python Turing Machine

Here is a list of the implemented functions

- Increment
- Decrement
- One's Complement

## How these machines work

The states of each of the machines is stored within the text files that begin with `tm_`. These files are read based in the input of the `-w` argument passed at execution time. The states are read from the text files and stored during runtime in dictionaries with states as the keys and tuples containing 4 variables for the values of each item in the dictionary.

Each line of the state files that I've written can be interpreted as 5 tab delimited columns with them representing:

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
- `make clean`
  - Deletes all .pyc and generated output files

Running `make` will execute each rule using my own supplied test files as the default. However, command line arguments can also be passed with the make command to change the file inputs. This is done like so:

- `make ONES-INPUT="xinputONES.txt"`
- `make INC-INPUT="xinputINC.txt"`
- `make DEC-INPUT="xinputDEC.txt"`

Simply change the path to any text file you like. Of course, these can be combined with the other make rules and multiple can be changed at once when running the command.
