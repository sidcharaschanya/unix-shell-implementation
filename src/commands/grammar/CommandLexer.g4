lexer grammar CommandLexer;
tokens {SQ, BQ, DQ}

fragment SQ_CHAR: '\'';
fragment BQ_CHAR: '`';
fragment DQ_CHAR: '"';

SEQ: ';';
PIPE: '|';
WS: [\t ]+;
UNQUOTED: ~[\t '"`\n;|<>]+;
LT: '<';
GT: '>';

SQ_START: SQ_CHAR -> type(SQ), pushMode(SINGLE_QUOTED);
BQ_START: BQ_CHAR -> type(BQ), pushMode(BACKQUOTED);
DQ_START: DQ_CHAR -> type(DQ), pushMode(DOUBLE_QUOTED);

mode SINGLE_QUOTED;
SQ_CONTENT: ~[\n']+;
SQ_END: SQ_CHAR -> type(SQ), popMode;

mode BACKQUOTED;
BQ_CONTENT: ~[\n`'"]+;
BQ_END: BQ_CHAR -> type(BQ), popMode;
SQ_IN_BQ: SQ_CHAR -> type(SQ), pushMode(SINGLE_QUOTED);
DQ_IN_BQ: DQ_CHAR -> type(DQ), pushMode(DOUBLE_QUOTED);

mode DOUBLE_QUOTED;
DQ_CONTENT: ~[\n"`]+;
DQ_END: DQ_CHAR -> type(DQ), popMode;
BQ_IN_DQ: BQ_CHAR -> type(BQ), pushMode(BACKQUOTED);
