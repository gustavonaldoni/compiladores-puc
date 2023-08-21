#include <stdio.h>
#include <stdlib.h>
#include "analex.h"

int token;

void E();
void T();
void E_linha();
void T_linha();
void F();
void erro();
void reconhecer(int tok);

void erro()
{
    printf("Erro sintatico na linha: %d\n", linha);
    exit(1);
}

void reconhecer(int tok)
{
    if (tok == token)
        token = analex();
    else
        erro();
}

void E()
{
    T();
    E_linha();
}

void E_linha()
{
    if(token == '+')
    {
        reconhecer('+');
        T();
        E_linha();

    }
    else if (token == '-')
    {
        reconhecer('-');
        T();
        E_linha();

    }
}

void T()
{
    F();
    T_linha();
}

void T_linha()
{
    if(token == '*')
    {
        reconhecer('*');
        F();
        T_linha();

    }
    else if(token == '/')
    {
        reconhecer('/');
        F();
        T_linha();

    }
}

void F()
{
    if(token == NUM)
    {
        reconhecer(NUM);
    }
    else if (token == '(')
    {
        reconhecer('(');
        E();
        reconhecer(')');
    }
}
