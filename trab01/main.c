#include <stdio.h>
#include "analex.h"

int main()
{
    int token;
    token = analex();

    while (token != 'q')
        token = analex();

    return 0;
}