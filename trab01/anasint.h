#include <stdio.h>
#include <stdlib.h>
#include "analex.h"
#include "pilha.h"

int token;
pilha p;

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
        p_insere(&p, '+');
        E_linha();
    }
    else if (token == '-')
    {
        reconhecer('-');
        T();
        p_insere(&p, '-');
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
        p_insere(&p, '*');
        T_linha();
    }
    else if(token == '/')
    {
        reconhecer('/');
        F();
        p_insere(&p, '/');
        T_linha();
    }
}

void F()
{
    if(token == NUM)
    {
        reconhecer(NUM);
        p_insere(&p, NUM);
    }
        
    else if (token == '(')
    {
        reconhecer('(');
        E();
        reconhecer(')');
    }
}
