%{
#include <stdio.h>
#include "tokens.h" 
int line=1;
%}
%%
"if"  { return IF; }
"else" { return ELSE;}
"while" { return WHILE;}
"do"  { return DO;}
"int" { return INT;}
">="  { return GE;}
"<="  { return LE;}
"=="  { return EQ;}
"!="  { return NE;}
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
yywrap() { return 1; }
#endif

int yyerror(char *s) { 
  fprintf(stderr, "%s na linha %d\n",s,line); 
}

main(int argc, char** argv) {
int token;	
	yyin = fopen(argv[1],"r");
	token = yylex();
	while(token) {
		printf("%d -> %s\n", token, yytext);
		token = yylex(); 
	}
}


