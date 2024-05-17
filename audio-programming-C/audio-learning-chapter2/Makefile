sf2float: sf2float.o libportsf.a
	gcc -g -o sf2float sf2float.o libportsf.a -lm
sf2float.o: sf2float.cpp portsf.h
		gcc -c -g sf2float.cpp
libportsf.a: portsf.c ieee80.c portsf.h ieee80.h
		cc -c -g portsf.c
		cc -c -g ieee80.c
		ar rv libportsf.a portsf.o ieee80.o
		rm portsf.o ieee80.o
clean:
		rm -f sf2float sf2float.o libportsf.a