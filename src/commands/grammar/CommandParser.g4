parser grammar CommandParser;
options {tokenVocab = CommandLexer;}

command: pipe | command SEQ command | call;
pipe: call PIPE call | pipe PIPE call;
call: WS? (redirection WS)* argument (WS atom)* WS?;
atom: redirection | argument;
argument: (quoted | UNQUOTED)+;
redirection: LT WS? argument | GT WS? argument;

quoted: single_quoted | double_quoted | backquoted;
single_quoted: SQ SQ_CONTENT SQ;
backquoted: BQ (single_quoted | double_quoted | BQ_CONTENT)+ BQ;
double_quoted: DQ (backquoted | DQ_CONTENT)* DQ;
