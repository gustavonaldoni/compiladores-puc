#include <stdio.h>
#include "anasint.h"

int main()
{
    token = analex();

    E();

    if (token != ';')
        erro();
    else
        printf("Sucesso!");

    return 0;
}