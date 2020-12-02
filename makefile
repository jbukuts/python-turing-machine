ONES-INPUT=xinputONES.txt
INC-INPUT=xinputINC.txt
DEC-INPUT=xinputDEC.txt
PAL-INPUT=xinputPAL.txt
DIV-INPUT=xinputDIV.txt

run-all: \
	clean \
	run-ones \
	run-inc \
	run-dec \
	run-pal \
	run-div \

install-dep:
	bash ./setup.sh

run-ones: \
	install-dep
	python3 mainONES.py -w ONES -i $(ONES-INPUT) -l zlogONES.txt >zoutputONES.txt

run-inc: \
	install-dep
	python3 mainINC.py -w INCREMENT -i $(INC-INPUT) -l zlogINC.txt >zoutputINC.txt

run-dec: \
	install-dep
	python3 mainDEC.py -w DECREMENT -i $(DEC-INPUT) -l zlogDEC.txt >zoutputDEC.txt

run-pal: \
	install-dep
	python3 mainPAL.py -w PALINDROME -i $(PAL-INPUT) -l zlogPAL.txt >zoutputPAL.txt

run-div: \
	install-dep
	python3 mainDIV.py -w DIVISIBLE -i $(DIV-INPUT) -l zlogDIV.txt >zoutputDIV.txt

clean:
	find  . -name 'z*.txt' -exec rm {} \;
	find  . -name '*.pyc' -exec rm {} \;
