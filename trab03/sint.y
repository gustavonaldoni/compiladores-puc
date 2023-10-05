%{ 
#include "analex.c"
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
Prog : Statement_Seq
	;
	
	
Statement_Seq :
	Statement Statement_Seq
	|
	;
	
Args:
	  Args ',' Exp
	| Exp
	|
	;
		
Statement: 
		Atribuicao
	|	If_Statement
	| 	While_Statement
	|   Do_While_Statement
	|   ID '(' Args ')' ';'
	|   Dec_Var
	;

Dec_Var:
	Tipo ID '=' Exp ';'
	;

Tipo:
	  INT
	| CHAR
	| FLOAT
	| VOID
	;
	
Atribuicao : ID '=' Exp ';' 
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
			
Exp : Exp '+' Exp  
	| Exp '-' Exp  
	| Exp '*' Exp  
	| Exp '/' Exp  
	| Exp '>' Exp  
	| Exp '<' Exp 
	| Exp GE Exp  
	| Exp LE Exp   
	| Exp EQ Exp   
	| Exp NE Exp   
	| Exp AND Exp  
	| Exp OR Exp   
	| '(' Exp ')'  
	| NUM		   
	| ID           
	;   
	
%%  
int main(int argc, char **argv) {     
  yyin = fopen(argv[1],"r");
  yyparse();      
} 
