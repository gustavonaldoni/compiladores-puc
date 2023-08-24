#include <stdio.h>
#include <stdlib.h>
#include "analex.h"
#include "pilha.h"

int token;
pilha p;

int a = 0;
int b = 0;

void erro();
void reconhecer(int tok);

void E();
void T();
void E_linha();
void T_linha();
void F();

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

        printf("+ ");

        // Análise semântica
        a = p_remove(&p);
        b = p_remove(&p);

        p_insere(&p, a + b);

        E_linha();
    }
    else if (token == '-')
    {
        reconhecer('-');
        T();

        printf("- ");

        // Análise semântica
        a = p_remove(&p);
        b = p_remove(&p);

        p_insere(&p, b - a);

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

        printf("* ");

        // Análise semântica
        a = p_remove(&p);
        b = p_remove(&p);

        p_insere(&p, a * b);

        T_linha();
    }
    else if(token == '/')
    {
        reconhecer('/');
        F();

        printf("/ ");

        // Análise semântica
        a = p_remove(&p);
        b = p_remove(&p);

        p_insere(&p, b / a);
    
        T_linha();
    }
}

void F()
{
    if(token == NUM)
    {
        printf("%d ", tokenval);

        p_insere(&p, tokenval);
        reconhecer(NUM);
    }
        
    else if (token == '(')
    {
        reconhecer('(');
        E();
        reconhecer(')');
    }

    else
        erro();
}
