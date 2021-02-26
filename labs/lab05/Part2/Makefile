all: static_block dynamic_block

static_block: static_lib program.o
	gcc program.o static_lib.a -o static_block

dynamic_block: dynamic_lib program.o
	gcc program.o dynamic_lib.so -o dynamic_block

static_lib: block.o
	ar qc static_lib.a block.o

dynamic_lib: block.o
	gcc -shared block.o -o dynamic_lib.so

program.o: program.c
	gcc -c program.c -o program.o

block.o: source/block.c
	gcc -c source/block.c -o block.o
