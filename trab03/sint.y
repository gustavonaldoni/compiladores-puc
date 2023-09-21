%{ 
#include "analex.c" 
%}
  
%token INTEGER
%left '+' '-' 
%left '*' '/' 
%start prog  
%%  
prog : prog expr ';' 	{printf("%d\n", $2);}
     |				 	        {}
	   ;
			 
expr:
	INTEGER {$$ = $1;}
  | expr '+' expr  { $$ = $1 + $3; }
  | expr '-' expr  { $$ = $1 - $3; }
  | expr '*' expr  { $$ = $1 * $3; }
  | expr '/' expr  { $$ = $1 / $3; }
  | '(' expr ')'   { $$ = $2; }
  ;  

%%  
yyerror(char *s) {
  printf("erro sintatico na linha %d\n",line);
}

int main(void) {     
  yyparse();      
} 

