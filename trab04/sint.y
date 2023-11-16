%{ 
#include "analex.c"
#include "codigo.h"
void yyerror(char *s) {
	printf("erro sintatico na linha %d", line);
}
%}
%token NUM
%token ID
%token AUTO
%token DOUBLE
%token INT
%token STRUCT
%token BREAK
%token ELSE
%token LONG
%token SWITCH
%token CASE
%token ENUM
%token REGISTER
%token TYPEDEF
%token CHAR
%token EXTERN
%token RETURN
%token UNION
%token CONST
%token FLOAT
%token SHORT
%token UNSIGNED
%token CONTINUE
%token FOR
%token SIGNED
%token VOID
%token DEFAULT
%token SIZEOF
%token VOLATILE
%token DO
%token IF
%token STATIC
%token WHILE
%token PRINT
%token PRINTLN
%token READ
%token AND
%token OR
%token GE
%token LE
%token EQ
%token NE
%token NOT
%left AND OR
%left '>' '<' NE EQ GE LE
%left '+' '-'
%left '*' '/'
%start Prog
%%
Prog : 
      Statement_Seq
	;

Function_Dec :
	  Tipo ID '(' Args_Dec ')' Compound_Statement_Func
	;

Args_Dec :
	  Args_Dec ',' Tipo ID
	| Tipo ID
	|
	;

Compound_Statement_Func :
	  '{' Statement_Seq_Func '}'
	;

Statement_Seq_Func :
	  Statement Statement_Seq_Func
	|
	;

Function_Call :
	  ID '(' Args ')'
	;

Args:
	  Args ',' Exp
	| Exp
	|
	;

Statement_Seq :
	  Statement Statement_Seq
	|
	;
		
Statement: 
	  Atribuicao
	| If_Statement
	| While_Statement
	| Do_While_Statement
	| ID '(' Args ')' ';'
	| Var_Dec
	| Function_Dec
	| Function_Call
	| PRINT '(' Exp ')' ';'		{ print($3); }
	| PRINTLN '(' Exp ')' ';'	{ println($3); }
	| RETURN Exp ';'
	;

Var_Dec:
	  Tipo ID ';'
	| Tipo ID '=' Exp ';'
	| Tipo ID ',' Rest_Var_Dec ';'
	| Tipo ID '=' Exp ',' Rest_Var_Dec ';'
	;

Rest_Var_Dec:
	  ID Other_Var_Dec
	| ID ',' Other_Var_Dec
	| ID '=' Exp Other_Var_Dec
	| ID '=' Exp ',' Other_Var_Dec
	;

Other_Var_Dec : 
	  ID Other_Var_Dec
	| ID ',' Other_Var_Dec 
	| ID '=' Exp ',' Other_Var_Dec
	| ID '=' Exp Other_Var_Dec
	|
	;

Tipo:
	  INT
	| CHAR
	| FLOAT
	| VOID
	;
	
Atribuicao : ID '=' Exp ';' { atrib($$, $1, $3); }
	;

Compound_Statement :
	  Statement
	| '{' Statement_Seq '}'
	;
	
If_Statement:
	  IF '(' Exp ')' Compound_Statement Else_Part
	;
		
Else_Part:
	  ELSE Compound_Statement
	|
	;
		
While_Statement:
	  WHILE '(' Exp ')' Compound_Statement  
	;

Do_While_Statement:
	  DO Compound_Statement WHILE '(' Exp ')' ';'   
	;
			
Exp : Exp '+' Exp  	{$$ = newTemp(); expressaoAritmetica('+', $$, $1, $3);}
	| Exp '-' Exp  	{$$ = newTemp(); expressaoAritmetica('-', $$, $1, $3);}
	| Exp '*' Exp  	{$$ = newTemp(); expressaoAritmetica('*', $$, $1, $3);}
	| Exp '/' Exp  	{$$ = newTemp(); expressaoAritmetica('/', $$, $1, $3);}
	| Exp '>' Exp  	{$$ = newTemp(); expressaoRelacional('>', $$, $1, $3);}
	| Exp '<' Exp  	{$$ = newTemp(); expressaoRelacional('<', $$, $1, $3);}
	| Exp GE Exp   	{$$ = newTemp(); expressaoRelacional(GE, $$, $1, $3);}
	| Exp LE Exp	{$$ = newTemp(); expressaoRelacional(LE, $$, $1, $3);}
	| Exp EQ Exp   
	| Exp NE Exp   
	| Exp AND Exp  
	| Exp OR Exp   
	| '(' Exp ')'  
	| NUM			{$$ = newTemp(); li($$, $1);}   
	| ID
	| Function_Call          
	;   
	
%%  
int main(int argc, char **argv) {     
  yyin = fopen(argv[1],"r");
  yyparse();      
} 
