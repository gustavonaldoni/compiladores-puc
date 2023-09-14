SOURCE_FILE = analex.c
EXECUTABLE_NAME = analex.out

CFLEX = flex

CC = gcc
CFLAGS = -lfl

all:
	flex -o analex.c analex.l
	$(CC) $(SOURCE_FILE) -o $(EXECUTABLE_NAME) $(CFLAGS)

execute:
	./$(EXECUTABLE_NAME) teste.c