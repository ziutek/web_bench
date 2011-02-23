include $(GOROOT)/src/Make.inc

ALL=http webgo twister

all: $(ALL)

clean:
	rm -rf *.[68] $(ALL) *.pyc

%: %.go
	$(GC) $*.go
	$(LD) -o $@ $@.$O
