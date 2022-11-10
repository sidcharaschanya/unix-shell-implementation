parser grammar CommandParser;
options {tokenVocab = CommandLexer;}

command: pipe | command SEQ command | call;

pipe: call PIPE call | pipe PIPE call;

call: WS? (redirection WS)* argument (WS atom)* WS?;

atom: redirection | argument;

argument: (quoted | UNQUOTED)+;

redirection: LT WS? argument | GT WS? argument;

quoted: single_quoted | double_quoted | back_quoted;

single_quoted: SQ SQ_CONTENT SQ;

back_quoted: BQ BQ_CONTENT BQ;

double_quoted: DQ (back_quoted | DQ_CONTENT)* DQ;
