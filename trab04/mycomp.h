/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_MYCOMP_H_INCLUDED
# define YY_YY_MYCOMP_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    NUM = 258,                     /* NUM  */
    ID = 259,                      /* ID  */
    AND = 260,                     /* AND  */
    OR = 261,                      /* OR  */
    NOT = 262,                     /* NOT  */
    EQ = 263,                      /* EQ  */
    LE = 264,                      /* LE  */
    GE = 265,                      /* GE  */
    NE = 266,                      /* NE  */
    IF = 267,                      /* IF  */
    WHILE = 268,                   /* WHILE  */
    ELSE = 269,                    /* ELSE  */
    DO = 270,                      /* DO  */
    INT = 271,                     /* INT  */
    READ = 272,                    /* READ  */
    PRINTLN = 273,                 /* PRINTLN  */
    PRINT = 274,                   /* PRINT  */
    CHAR = 275,                    /* CHAR  */
    VOID = 276                     /* VOID  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif
/* Token kinds.  */
#define YYEMPTY -2
#define YYEOF 0
#define YYerror 256
#define YYUNDEF 257
#define NUM 258
#define ID 259
#define AND 260
#define OR 261
#define NOT 262
#define EQ 263
#define LE 264
#define GE 265
#define NE 266
#define IF 267
#define WHILE 268
#define ELSE 269
#define DO 270
#define INT 271
#define READ 272
#define PRINTLN 273
#define PRINT 274
#define CHAR 275
#define VOID 276

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
union YYSTYPE
{
#line 1 "mycomp.y"

  struct no {
    int place;
	char *code;
  } node;
  int place;

#line 117 "mycomp.h"

};
typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_MYCOMP_H_INCLUDED  */
