lexer grammar CommandLexer;
tokens {BQ_START}

fragment SQ_CHAR: '\'';
fragment BQ_CHAR: '`';
fragment DQ_CHAR: '"';

SEQ: ';';
PIPE: '|';
WS: [\t ]+;
UNQUOTED: ~[\t '"`\n;|<>]+;
LT: '<';
GT: '>';

SQ_START: SQ_CHAR -> pushMode(SINGLE_QUOTED);
BQ: BQ_CHAR -> type(BQ_START), pushMode(BACK_QUOTED);
DQ_START: DQ_CHAR -> pushMode(DOUBLE_QUOTED);

mode SINGLE_QUOTED;
SQ_CONTENT: ~[\n']+;
SQ_END: SQ_CHAR -> popMode;

mode BACK_QUOTED;
BQ_CONTENT: ~[\n`]+;
BQ_END: BQ_CHAR -> popMode;

mode DOUBLE_QUOTED;
DQ_CONTENT: ~[\n"`]+;
DQ_END: DQ_CHAR -> popMode;
BQ_IN_DQ: BQ_CHAR -> type(BQ_START), pushMode(BACK_QUOTED);
