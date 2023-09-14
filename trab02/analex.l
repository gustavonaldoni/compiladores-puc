%{
#include <stdio.h>
#include "tokens.h" 
#include "tabsimb.h"
int line=1;

int yyerror(char *s) { 
  fprintf(stderr, "%s na linha %d\n",s,line); 
}
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
">=" { return GE; } 
"<=" { return LE; } 
"==" { return EQ; } 
"!=" { return NE; }
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
[a-zA-Z][a-zA-Z0-9]*   { insere(yytext); return ID; }
\        { ; }
\n       { line++; }     
\t       { ; }
"//".*\n { }             
.        { yyerror("illegal token"); }
%%
#ifndef yywrap
int yywrap() { return 1; }
#endif

void main(int argc, char** argv) {
int token;	
	yyin = fopen(argv[1],"r");
	token = yylex();
	while(token) {
		printf("%d -> %s\n", token, yytext);
		token = yylex(); 
	}
	imprime();
}


