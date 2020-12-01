ONES-INPUT=xinputONES.txt
INC-INPUT=xinputINC.txt
DEC-INPUT=xinputDEC.txt
PAL-INPUT=xinputPAL.txt

run-all: \
	clean \
	run-ones \
	run-inc \
	run-dec \

run-ones:
	python3 mainONES.py -w ONES -i $(ONES-INPUT) -l zlogONES.txt >zoutputONES.txt

run-inc:
	python3 mainINC.py -w INCREMENT -i $(INC-INPUT) -l zlogINC.txt >zoutputINC.txt

run-dec:
	python3 mainDEC.py -w DECREMENT -i $(DEC-INPUT) -l zlogDEC.txt >zoutputDEC.txt

run-pal:
	python3 mainPAL.py -w PALINDROME -i $(PAL-INPUT) -l zlogPAL.txt >zoutputPAL.txt

clean:
	find  . -name 'z*.txt' -exec rm {} \;
	find  . -name '*.pyc' -exec rm {} \;
