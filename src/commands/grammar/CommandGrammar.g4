grammar CommandGrammar;

// Parser

command : pipe | command ';' command | call ;
pipe : call '|' call | pipe '|' call;
call : (NON_KEYWORD | quoted)* ;

quoted : SINGLE_QUOTED | DOUBLE_QUOTED | BACKQUOTED ;

// Lexer

NON_KEYWORD : ~[\n'"`;|]+ ;
SINGLE_QUOTED : '\'' ~[\n']+ '\'' ;
BACKQUOTED : '`' ~[\n`]+ '`' ;
fragment DQ_CONTENT : ~[\n"`]+ ;
DOUBLE_QUOTED : '"' (BACKQUOTED | DQ_CONTENT)* '"' ;
