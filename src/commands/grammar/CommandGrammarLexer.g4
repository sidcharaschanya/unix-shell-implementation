lexer grammar CommandGrammarLexer ;
tokens {SQ, BQ, DQ}

SEQ : ';' ;
PIPE : '|' ;
NON_KW : ~[\n'"`;|]+ ;

SQ : '\'' -> type(SQ), pushMode(SINGLE_QUOTED) ;
BQ : '`' -> type(BQ), pushMode(BACKQUOTED) ;
DQ : '"' -> type(DQ), pushMode(DOUBLE_QUOTED) ;

mode SINGLE_QUOTED;
SQ_CONTENT : ~[\n']+ ;
SQ_END : SQ -> type(SQ), popMode ;

mode BACKQUOTED ;
BQ_CONTENT : ~[\n`'"]+ ;
BQ_END : BQ -> type(BQ), popMode ;
SQ_IN_BQ : SQ -> type(SQ), pushMode(SINGLE_QUOTED) ;
DQ_IN_BQ : DQ -> type(DQ), pushMode(DOUBLE_QUOTED) ;

mode DOUBLE_QUOTED ;
DQ_CONTENT : ~[\n"`]+ ;
DQ_END : DQ -> type(DQ), popMode ;
BQ_IN_DQ : BQ -> type(BQ), pushMode(BACKQUOTED) ;
