#include <stdio.h>
#include <ctype.h>
#include "analex.h"

void erro();
void reconhece(int token);

void E();
void E_linha();
void T();
void T_linha();
int F();

void erro()
{
    int ch = analex();

}

void reconhece(int token)
{

}

void E()
{
    T();
    E_linha();
}

void E_linha()
{
    if (tokenval == '+')
    {
        reconhece('+');
        T();
        E_linha();
    }

    else if (tokenval == '-')
    {
        reconhece('-');
        T();
        E_linha();
    }

    else
        ;
}

void T()
{
    F();
    T_linha();
}

void T_linha()
{
    if (tokenval == '*')
    {
        reconhece('*');
        F();
        T_linha();
    }

    else if (tokenval == '/')
    {
        reconhece('/');
        F();
        T_linha();
    }

    else
        ;
}

int F()
{
    if (tokenval == NUM)
        return NUM;

    else if (tokenval == '(')
        E();
    else if (tokenval == ')')
        return;
}
