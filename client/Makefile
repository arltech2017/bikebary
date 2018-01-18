TARGET=dumb


$(TARGET): BLINK.ms
	microscheme -a $^

flash:
	microscheme -u BLINK.ms -d /dev/ttyACM0 -m UNO

.PHONY: clean
clean:
	$(RM) *.s *.hex *.elf
