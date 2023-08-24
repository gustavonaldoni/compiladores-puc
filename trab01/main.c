#include <stdio.h>
#include "anasint.h"

int main()
{
    p_criar(&p);
    token = analex();
   
    E();

    if (token != ';')
        erro();
    else
        printf("\nResultado = %d\n", p_topo(p));

    return 0;
}