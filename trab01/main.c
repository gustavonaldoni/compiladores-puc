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
        p_mostrar(p);

    return 0;
}