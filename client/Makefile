TARGET=dumb


$(TARGET): BLINK.ms
	microscheme -a $^

flash:
	microscheme -m UNO -u BLINK.ms -d /dev/ttyACM0

.PHONY: test
test:
	cd tests; gsi *

.PHONY: clean
clean:
	$(RM) *.s *.hex *.elf
