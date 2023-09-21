%{
#include "sint.h"
int line=1;
int tokenval;
%}

%%
"+"   { return '+'; }
"-"   { return '-'; }
"*"   { return '*'; }
"/"   { return '/'; }
")"   { return ')'; }
"("   { return '('; }
";"   { return ';'; }
[0-9]+   { yylval = atoi(yytext); return INTEGER; }
\        { ; }
\n       { line++; }              
\t       { ; }    
.        { printf("token ilegal!!\n"); }

%%
#ifndef yywrap
yywrap() { return 1; }
#endif


