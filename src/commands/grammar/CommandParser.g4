parser grammar CommandParser;
options {tokenVocab = CommandLexer;}

cmdline: command? EOF;

command: pipe #pipeCommand | left=command SEQ right=command #seq | call #callCommand;

pipe: left=call PIPE right=call #singlePipe | left=pipe PIPE right=call #nestedPipe;

call: WS? (redirections+=redirection WS)* app=argument (WS atoms+=atom)* WS?;

atom: redirection | argument;

argument: elements+=argumentElement+;

argumentElement: quoted #quotedArgElem | UNQUOTED #unquoted ;

redirection: op=LT WS? argument | op=GT WS? argument;

quoted: singleQuoted | doubleQuoted | backQuoted;

singleQuoted: SQ SQ_CONTENT SQ;

backQuoted: BQ BQ_CONTENT BQ;

doubleQuoted: DQ elements+=doubleQuotedElement* DQ;

doubleQuotedElement: backQuoted #bqDqElem | DQ_CONTENT #dqContent;
