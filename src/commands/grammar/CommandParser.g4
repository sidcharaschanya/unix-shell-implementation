parser grammar CommandParser;
options {tokenVocab = CommandLexer;}

cmdline: command? EOF;

command: pipe | command SEQ command | call;

pipe: call PIPE call | pipe PIPE call;

call: WS? (redirection WS)* argument (WS atom)* WS?;

atom: redirection | argument;

argument: (quoted | UNQUOTED)+;

redirection: LT WS? argument | GT WS? argument;

quoted: singleQuoted | doubleQuoted | backQuoted;

singleQuoted: SQ SQ_CONTENT SQ;

backQuoted: BQ BQ_CONTENT BQ;

doubleQuoted: DQ (backQuoted | DQ_CONTENT)* DQ;
