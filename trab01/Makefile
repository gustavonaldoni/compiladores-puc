SOURCE_FILE = main.c
EXECUTABLE_NAME = main.out
TEST_FILE = test.txt

CC = gcc
CFLAGS = -Wall -Werror

all:
	$(CC) $(SOURCE_FILE) -o $(EXECUTABLE_NAME) $(CFLAGS)

execute:
	./$(EXECUTABLE_NAME) < $(TEST_FILE)