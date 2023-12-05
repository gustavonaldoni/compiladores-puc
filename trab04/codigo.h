#include <stdio.h>
#include "lista.h"
#include "sint.h"

char instrucao[30];

int temp = -1;
int label = 0;

int newTemp();
int newLabel();

void getName(int, char *);

void atribuicao(struct no *, int, struct no);
void loadImmediate(struct no*, int);
void expressaoAritmetica(int, int, int, int);
void expressaoRelacional(int, int, int, int);

void readInt();

void print(int);
void println(int);

int newTemp()
{
    return temp--;
}

int newLabel()
{
    return label++;
}

void getName(int num, char *name)
{
    if (num >= 0)
        sprintf(name, "$s%d", num);
    else
        sprintf(name, "$t%d", -(num + 1));
}

void atribuicao(struct no *Atrib, int $1, struct no $3)
{
    char orig[10];
    char dest[10];

    getName($3.place, orig);
    getName($1, dest);

    sprintf(instrucao, "\tmove %s, %s\n", dest, orig);
    
    createCode(&Atrib->code);
	insertCode(&Atrib->code,$3.code);
	insertCode(&Atrib->code,instrucao);
}

void loadImmediate(struct no* Exp, int num)
{
    char dest[5];
    
    createCode(&Exp->code);

    getName(temp, dest);
    sprintf(instrucao, "\tli %s, %d\n", dest, num);
    
    insertCode(&Exp->code, instrucao);
}

void expressaoAritmetica(int op, int temp, int reg1, int reg2)
{
    char nameReg1[5];
    char nameReg2[5];
    char nameTemp[5];

    getName(reg1, nameReg1);
    getName(reg2, nameReg2);
    getName(temp, nameTemp);

    switch (op)
    {
    case '+':
        printf("\tadd %s, %s, %s\n", nameTemp, nameReg1, nameReg2);
        break;

    case '-':
        printf("\tsub %s, %s, %s\n", nameTemp, nameReg1, nameReg2);
        break;

    case '*':
        printf("\tmul %s, %s, %s\n", nameTemp, nameReg1, nameReg2);
        break;

    case '/':
        printf("\tdiv %s, %s, %s\n", nameTemp, nameReg1, nameReg2);
        break;

    default:
        break;
    }
}

void expressaoRelacional(int op, int temp, int reg1, int reg2)
{
    char nameReg1[5];
    char nameReg2[5];
    char nameTemp[5];

    getName(reg1, nameReg1);
    getName(reg2, nameReg2);
    getName(temp, nameTemp);

    newLabel();

    printf("\tli %s, 1\n", nameTemp);

    switch (op)
    {
    case '>':
        printf("\tbgt %s, %s, L%d\n", nameReg1, nameReg2, label);
        break;

    case '<':
        printf("\tblt %s, %s, L%d\n", nameReg1, nameReg2, label);
        break;

    case GE:
        printf("\tbge %s, %s, L%d\n", nameReg1, nameReg2, label);
        break;

    case LE:
        printf("\tble %s, %s, L%d\n", nameReg1, nameReg2, label);
        break;

    default:
        break;
    }

    printf("\tli %s, 0\n", nameTemp);
    printf("L%d:", label);
}

void print(int reg)
{
    char nameReg[5];

    getName(reg, nameReg);

    printf("\tli v0, 1\n");
    printf("\tmove $a0, %s\n", nameReg);
    printf("\tsyscall\n");
}

void println(int reg)
{
    char nameReg[5];

    getName(reg, nameReg);

    printf("\tli $v0, 1\n");
    printf("\tmove $a0, %s\n", nameReg);
    printf("\tsyscall\n");
}

void readInt(int reg)
{
	char nameReg[5];
	
	printf("\tli $v0, 5\n");
    printf("\tsyscall\n");
    
    getName(reg, nameReg);
    
    printf("\tmove %s, $v0\n", nameReg);
}
