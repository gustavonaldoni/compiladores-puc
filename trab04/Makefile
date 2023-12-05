ANALEX = analex
SINT = sint

LEX_FILE = $(ANALEX).l
ANALEX_FILE = $(ANALEX).c

SINT_FILE = $(SINT).y
YACC_FILE = $(SINT).c

OUTPUT_FILE = $(SINT).out
TEST_FILE = teste.txt

all:
	flex -o $(ANALEX_FILE) $(LEX_FILE)
	yacc $(SINT_FILE) -o $(YACC_FILE) -d
	gcc $(YACC_FILE) -o $(OUTPUT_FILE) -lfl

execute:
	./$(OUTPUT_FILE) $(TEST_FILE)
	java -jar mars.jar saida.asm
