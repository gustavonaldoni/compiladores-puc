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

#ifndef YY_YY_SINT_H_INCLUDED
# define YY_YY_SINT_H_INCLUDED
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
    AUTO = 260,                    /* AUTO  */
    DOUBLE = 261,                  /* DOUBLE  */
    INT = 262,                     /* INT  */
    STRUCT = 263,                  /* STRUCT  */
    BREAK = 264,                   /* BREAK  */
    ELSE = 265,                    /* ELSE  */
    LONG = 266,                    /* LONG  */
    SWITCH = 267,                  /* SWITCH  */
    CASE = 268,                    /* CASE  */
    ENUM = 269,                    /* ENUM  */
    REGISTER = 270,                /* REGISTER  */
    TYPEDEF = 271,                 /* TYPEDEF  */
    CHAR = 272,                    /* CHAR  */
    EXTERN = 273,                  /* EXTERN  */
    RETURN = 274,                  /* RETURN  */
    UNION = 275,                   /* UNION  */
    CONST = 276,                   /* CONST  */
    FLOAT = 277,                   /* FLOAT  */
    SHORT = 278,                   /* SHORT  */
    UNSIGNED = 279,                /* UNSIGNED  */
    CONTINUE = 280,                /* CONTINUE  */
    FOR = 281,                     /* FOR  */
    SIGNED = 282,                  /* SIGNED  */
    VOID = 283,                    /* VOID  */
    DEFAULT = 284,                 /* DEFAULT  */
    SIZEOF = 285,                  /* SIZEOF  */
    VOLATILE = 286,                /* VOLATILE  */
    DO = 287,                      /* DO  */
    IF = 288,                      /* IF  */
    STATIC = 289,                  /* STATIC  */
    WHILE = 290,                   /* WHILE  */
    PRINT = 291,                   /* PRINT  */
    PRINTLN = 292,                 /* PRINTLN  */
    READ = 293,                    /* READ  */
    AND = 294,                     /* AND  */
    OR = 295,                      /* OR  */
    GE = 296,                      /* GE  */
    LE = 297,                      /* LE  */
    EQ = 298,                      /* EQ  */
    NE = 299,                      /* NE  */
    NOT = 300                      /* NOT  */
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
#define AUTO 260
#define DOUBLE 261
#define INT 262
#define STRUCT 263
#define BREAK 264
#define ELSE 265
#define LONG 266
#define SWITCH 267
#define CASE 268
#define ENUM 269
#define REGISTER 270
#define TYPEDEF 271
#define CHAR 272
#define EXTERN 273
#define RETURN 274
#define UNION 275
#define CONST 276
#define FLOAT 277
#define SHORT 278
#define UNSIGNED 279
#define CONTINUE 280
#define FOR 281
#define SIGNED 282
#define VOID 283
#define DEFAULT 284
#define SIZEOF 285
#define VOLATILE 286
#define DO 287
#define IF 288
#define STATIC 289
#define WHILE 290
#define PRINT 291
#define PRINTLN 292
#define READ 293
#define AND 294
#define OR 295
#define GE 296
#define LE 297
#define EQ 298
#define NE 299
#define NOT 300

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
union YYSTYPE
{
#line 1 "sint.y"

  struct no {
    int place;
	char *code;
  } node;
  int place;

#line 165 "sint.h"

};
typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_SINT_H_INCLUDED  */
