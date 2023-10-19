%{
#include <stdio.h>
#include "sint.h"
int line=1;
%}
%%
"auto" { return AUTO; } 
"double" { return DOUBLE; } 
"int" { return INT; } 
"struct" { return STRUCT; } 
"break" { return BREAK; } 
"else" { return ELSE; } 
"long" { return LONG; } 
"switch" { return SWITCH; } 
"case" { return CASE; } 
"enum" { return ENUM; } 
"register" { return REGISTER; } 
"typedef" { return TYPEDEF; } 
"char" { return CHAR; } 
"extern" { return EXTERN; } 
"return" { return RETURN; } 
"union" { return UNION; } 
"const" { return CONST; } 
"float" { return FLOAT; } 
"short" { return SHORT; } 
"unsigned" { return UNSIGNED; } 
"continue" { return CONTINUE; } 
"for" { return FOR; } 
"signed" { return SIGNED; } 
"void" { return VOID; } 
"default" { return DEFAULT; } 
"sizeof" { return SIZEOF; } 
"volatile" { return VOLATILE; } 
"do" { return DO; } 
"if" { return IF; } 
"static" { return STATIC; } 
"while" { return WHILE; }
"print" { return PRINT; }
"println" { return PRINTLN; }
"read" { return READ; }
"&&" { return AND; }
"||" { return OR; }
">=" { return GE; } 
"<=" { return LE; } 
"==" { return EQ; } 
"!=" { return NE; }
"!" { return NOT; }
">"   { return '>';}
"<"   { return '<';}
"="   { return '='; }
"+"   { return '+'; }
"-"   { return '-'; }
"*"   { return '*'; }
"/"   { return '/'; }
";"   { return ';'; }
"("   { return '('; }
")"   { return ')'; }
"{"   { return '{'; }
"}"   { return '}'; }
","   { return ','; }
[0-9]+("."[0-9]+)?   { return NUM; }
[a-zA-Z][a-zA-Z0-9]*   { return ID; }
\        { ; }
\n       { line++; }     
\t       { ; }
"//".*\n { }             
.        { yyerror("illegal token"); }
%%
#ifndef yywrap
int yywrap() { return 1; }
#endif
